import os
import pandas as pd
from pathlib import Path
from tqdm import tqdm

"""
This would be the 3 script to run after the data_readding is fully ran.(we're linking everything together with this scrip to get the overall 13m records counts for the dashboard) 
we are linking updated_spending_with_districts.csv & all_politicians.csv, this way we can get the naming and data of the politicans on to the spendings data. Then we can 
view which politicans would have the most spending or which party have the most pending etc.
"""
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


def merge_spending_with_politicians(project_name="WeThePeopleAudit"):
    try:
        project = find_project(project_name)
        spending_file = project / "data" / "updated_spending_with_districts.csv"
        politicians_file = project / "data" / "all_politicians.csv"
        output_file = project / "data" / "merged_spending_politicians_with_party.csv"

        print(f"Looking for files: {spending_file}, {politicians_file}")
        if not politicians_file.exists():
            raise FileNotFoundError(f"Missing politicians file: {politicians_file}")
        if not spending_file.exists():
            raise FileNotFoundError(f"Missing spending file: {spending_file}")

        print("Loading spending data...")
        chunk_size = 10000
        chunks = pd.read_csv(spending_file, dtype=str, chunksize=chunk_size)
        spending_chunks = []
        chunk_count = 0

        for chunk in tqdm(chunks, desc="Reading spending chunks"):
            spending_chunks.append(chunk)
            chunk_count += 1

        spending = pd.concat(spending_chunks)
        print(f"Loaded {len(spending)} spending records in {chunk_count} chunks")
        print("Loading politicians data...")
        with tqdm(total=1, desc="Reading politicians data", unit="file") as progress:
            politicians = pd.read_csv(politicians_file, dtype=str)
            progress.update(1)
        print(f"Loaded {len(politicians)} politician records")

        print("Cleaning district info...")
        with tqdm(total=2, desc="Fixing district columns", unit="column") as progress:
            spending['House_District'] = spending['House_District'].fillna("").astype(str).str.strip()
            progress.update(1)
            politicians['district'] = politicians['district'].fillna("").astype(str).str.strip()
            progress.update(1)



#making sure that we are doing the matching correctly
        print("Finding representatives...")
        with tqdm(total=1, desc="Filtering for representatives", unit="step") as progress:
            house_reps = politicians[politicians['role'].str.contains('Rep', case=False, na=False)].copy()
            progress.update(1)
        print(f"Found {len(house_reps)} representatives")
        print("Merging data...")
        with tqdm(total=1, desc="Combining spending and politicians", unit="step") as progress:
            merged = spending.merge(
                house_reps[['people_id', 'name', 'party', 'role', 'district']],
                how='left',
                left_on='House_District',
                right_on='district'
            )
            progress.update(1)
        print(f"Created {len(merged)} merged records")

        print("Adding political party info...")
        with tqdm(total=1, desc="Creating party column", unit="step") as progress:
            merged['political_party'] = merged['party'].fillna('Unknown')
            merged['political_party'] = merged['political_party'].map({
                'D': 'Democrat',
                'R': 'Republican',
                'I': 'Independent',
                '': 'Unknown'
            }).fillna('Unknown')
            progress.update(1)

#pritns to get the gaps and make sure eveything is correct. Keep the progression bar going so we dont lose track - since the files is 5gb
        print("Filling gaps...")
        with tqdm(total=4, desc="Handling missing data", unit="column") as progress:
            merged['people_id'] = merged['people_id'].fillna('Unknown')
            progress.update(1)
            merged['name'] = merged['name'].fillna('Unknown')
            progress.update(1)
            merged['role'] = merged['role'].fillna('Unknown')
            progress.update(1)
            merged['district'] = merged['district'].fillna('Unknown')
            progress.update(1)

        print("Cleaning up...")
        with tqdm(total=1, desc="Removing duplicate column", unit="step") as progress:
            merged = merged.drop(columns=['district'], errors='ignore')
            progress.update(1)

        print("Saving file...")
        with tqdm(total=1, desc="Writing to CSV", unit="file") as progress:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            merged.to_csv(output_file, index=False)
            progress.update(1)

        print(f"\nDone! Created {output_file} with {len(merged)} records.")
        return merged

    except Exception as e:
        print(f"Problem: {e}")
        return None

#------run the process
df = merge_spending_with_politicians()
if df is not None and not df.empty:
    print("\nFirst few rows:")
    print(df.head())