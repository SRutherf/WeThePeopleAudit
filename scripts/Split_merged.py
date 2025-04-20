import os
import pandas as pd
from pathlib import Path
from tqdm import tqdm
import psutil
import logging
"""
This script would be the last script that runs, once all the data is accurately placed and clear. We would split everything
by using what we currenty have. However, the code has to be change due to PC memory side as, error tend to occur when memory is low.
When this happen then we would need to rerun the script to ensure that all row are collected. 

"""
#logging of the configs so we understand why there's an error
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#Spliting of the files due to databrick limiting sizing of the data
def find_project(project_name="WeThePeopleAudit"):
    """Hunt down our project folder"""
    here = Path.cwd()

    #if here returns values
    if here.name == project_name:
        return here
    #check all folders
    for parent in here.parents:
        if parent.name == project_name:
            return parent
    #research
    for root, dirs, _ in os.walk(Path.home()):
        if project_name in dirs:
            return Path(root) / project_name
    #Print the error here
    raise FileNotFoundError(f"Can't find the '{project_name}' folder anywhere")


def split_big_csv_file(project_name="WeThePeopleAudit"):
    try:
        project = find_project(project_name)
        big_file = project / "data" / "merged_spending_politicians_with_party.csv"
        parts = [project / "data" / f"part{i}.csv" for i in range(1, 8)]

        logging.info(f"Looking for file: {big_file}")
        if not big_file.exists():
            raise FileNotFoundError(f"Can't find input file: {big_file}")
        disk = psutil.disk_usage(str(project))
        mem = psutil.virtual_memory()
        logging.info(f"Free disk space: {disk.free / (1024 ** 3):.2f} GB")
        logging.info(f"Available memory: {mem.available / (1024 ** 3):.2f} GB")
#-------Total GB making sure limit is less than 14gb
        if disk.free / (1024 ** 3) < 14:
            raise RuntimeError("Not enough disk space (need 14+ GB). Free up some space first.")
        if mem.available / (1024 ** 3) < 2:
            logging.warning("Memory is low (< 2GB). This might be slow.")
        logging.info("Testing file format...")
        try:
            pd.read_csv(big_file, nrows=5, dtype=str, encoding='utf-8')
            encoding = 'utf-8'
        except (UnicodeDecodeError, pd.errors.ParserError) as e:
            logging.warning(f"Can't read with utf-8: {e}. Trying latin1 instead...")
            try:
                pd.read_csv(big_file, nrows=5, dtype=str, encoding='latin1')
                encoding = 'latin1'
            except Exception as e:
                logging.error(f"File seems corrupted: {e}. Fix it first.")
                return False

 #-------Figure out how many rows we're dealing with
        logging.info("Counting rows...")
        total_rows = sum(1 for _ in open(big_file)) - 1  #
        logging.info(f"Found {total_rows} rows")
#-------Siding of the data is needed
        rows_per_part = 1_970_026
        processed = 0
        start_part = 0
        for i, part_file in enumerate(parts):
            if part_file.exists():
                rows = sum(1 for _ in open(part_file)) - 1
                processed += rows
                start_part = i + 1
                logging.info(f"Found existing part{i + 1}.csv with {rows} rows")
            else:
                break
        if start_part >= 7:
            logging.info("All 7 parts already exist. Nothing to do.")
            return True
        logging.info(f"Starting with part {start_part + 1} (skipping {processed} rows)...")
        chunk_size = 10000
        if processed > 0:
            chunks = pd.read_csv(big_file, dtype=str, chunksize=chunk_size,
                                 encoding=encoding, skiprows=processed)
        else:
            chunks = pd.read_csv(big_file, dtype=str, chunksize=chunk_size, encoding=encoding)

        current_rows = 0
        part_index = start_part
        part_data = []
        total_processed = processed
        expected_chunks = ((total_rows - processed) // chunk_size) + 1
        for chunk in tqdm(chunks, desc="Processing file", total=expected_chunks):
            logging.debug(f"Read chunk: {len(chunk)} rows")
            part_data.append(chunk)
            current_rows += len(chunk)
            total_processed += len(chunk)


            if current_rows >= rows_per_part and part_index < 6:
                part_df = pd.concat(part_data)
                output_file = parts[part_index]
                logging.info(f"Saving part {part_index + 1} with {len(part_df)} rows...")
                part_df.to_csv(output_file, index=False)
                part_index += 1
                current_rows = 0
                part_data = []
                del part_df  # Free memory


        if part_data and part_index == 6:
            output_file = parts[part_index]
            logging.info(f"Saving final part with remaining {current_rows} rows...")
            with open(output_file, 'w', encoding=encoding) as f:
                header = part_data[0].columns.tolist()
                pd.DataFrame(columns=header).to_csv(f, index=False, lineterminator='\n')
                for chunk in part_data:
                    chunk.to_csv(f, mode='a', header=False, index=False, lineterminator='\n')

            part_index += 1
            part_data = []

        if part_index < 7:
            header_df = pd.read_csv(big_file, nrows=0, encoding=encoding)
            for i in range(part_index, 7):
                output_file = parts[i]
                logging.info(f"Creating empty file for part {i + 1}...")
                header_df.to_csv(output_file, index=False)

#------------Results progresstion Bar
        logging.info(f"Split complete! Created 7 parts:")
        saved_rows = 0
        for i, part_file in enumerate(parts, 1):
            if part_file.exists():
                rows = sum(1 for _ in open(part_file)) - 1
                saved_rows += rows
                size_gb = os.path.getsize(part_file) / (1024 ** 3)
                logging.info(f"Part {i}: {part_file.name} ({rows:,} rows, {size_gb:.2f} GB)")
            else:
                logging.info(f"Part {i}: {part_file.name} (missing)")

        logging.info(f"Total: {saved_rows:,} rows saved")

        # Final check
        if saved_rows != total_rows:
            logging.error(f"Row count mismatch! Saved {saved_rows}, expected {total_rows}")
            return False

        return True
#-----------List of execptions
    except FileNotFoundError as e:
        logging.error(f"File problem: {e}")
        return False
    except MemoryError:
        logging.error("Ran out of memory. Try using smaller chunks.")
        return False
    except (UnicodeDecodeError, pd.errors.ParserError) as e:
        logging.error(f"Can't read CSV: {e}")
        return False
    except OSError as e:
        logging.error(f"System error: {e} (disk full or permissions issue?)")
        return False
    except Exception as e:
        logging.error(f"Something went wrong: {e}")
        return False

#starts the defs
success = split_big_csv_file()
if success:
    logging.info("File split successfully!")
else:
    logging.error("Splitting failed.")