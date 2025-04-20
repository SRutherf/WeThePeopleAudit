import pandas as pd
from tqdm import tqdm
import os
from pathlib import Path

"""
This script would be the second to last to run, so it will be number 4. For this , we're basically giving all the data that is unassigned an unknown values.
The reason why we do this is to split it away from the other values. Splits unknown from out of states, so when we get data for it - there will be more details.
"""
def fix_unassigned_districts(project_name="WeThePeopleAudit"):
    try:
        project = fix_unassigned_districts(project_name)
        data_file = project / "data" / "merged_spending_politicians_with_party.csv"

        print(f"Looking for file: {data_file}")
        if not data_file.exists():
            raise FileNotFoundError(f"Can't find the data file: {data_file}")

        print("Reading and fixing data...")
        chunk_size = 10000
        chunks = pd.read_csv(data_file, dtype=str, chunksize=chunk_size)
        fixed_chunks = []

        for chunk in tqdm(chunks, desc="Processing chunks"):
            chunk.loc[chunk['state'] == 'UNASSIGNED',
            ['Congressional_District', 'Senate_District', 'House_District']] = 'Unknown'
            fixed_chunks.append(chunk)

        fixed_data = pd.concat(fixed_chunks)
        print(f"Fixed {len(fixed_data)} records")
        print(f"Saving back to {data_file}...")
        chunk_size = 10000
        total_chunks = (len(fixed_data) // chunk_size) + 1

        with tqdm(total=total_chunks, desc="Saving file", unit="chunk") as progress:
            for i in range(0, len(fixed_data), chunk_size):
                if i == 0:
                    fixed_data[i:i + chunk_size].to_csv(data_file, mode='w', index=False)
                else:
                    fixed_data[i:i + chunk_size].to_csv(data_file, mode='a', header=False, index=False)
                progress.update(1)

        print(f"Done! Saved {len(fixed_data)} fixed records")
        return fixed_data

    except Exception as e:
        print(f"Problem: {e}")
        return None

df = fix_unassigned_districts()
if df is not None and not df.empty:
    print("\nHere's what the data looks like now:")
    print(df.head())