import os
import json
from pathlib import Path
import logging
from collections import defaultdict
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()


def load_json_file(file_path):
    """Load a JSON file and return its contents."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from {file_path}")
        return None
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return None


def save_json_file(data, file_path):
    """Save data as a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        logger.error(f"Error writing to {file_path}: {e}")
        return False


def connect_bill_people_vote(bills_dir, output_dir=None):
    """
    :param bills_dir: Path to the bills directory
    :param output_dir: Path to output directory for summary data (defaults to bills_dir/connected_data)
    :return: Dictionary containing the connected data
    """
    bills_path = Path(bills_dir)
    if not bills_path.exists():
        logger.error(f"Bills directory does not exist: {bills_path}")
        return None

    if output_dir is None:
        output_dir = bills_path / "connected_data"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(exist_ok=True, parents=True)
    logger.info(f"Central output directory: {output_dir}")

    connected_data = {
        "years": {},
        "all_bills": {},
        "all_people": {},
        "all_votes": {},
        "bill_people_relationships": [],
        "bill_vote_relationships": [],
        "people_vote_relationships": []
    }

    # Process each year directory
    year_dirs = [d for d in bills_path.iterdir() if d.is_dir() and d.name.isdigit()]
    logger.info(f"Found {len(year_dirs)} year directories")

    for year_dir in year_dirs:
        year = year_dir.name
        logger.info(f"Processing year: {year}")

        year_data = {
            "bills": {},
            "people": {},
            "votes": {},
            "bill_people_relationships": [],
            "bill_vote_relationships": [],
            "people_vote_relationships": []
        }

        connected_data["years"][year] = year_data
        bill_dir = year_dir / "bill"
        if bill_dir.exists():
            bill_files = list(bill_dir.glob("*.json"))
            logger.info(f"Found {len(bill_files)} bill files in {year}")

            for bill_file in bill_files:
                bill_json = load_json_file(bill_file)
                if bill_json and "bill" in bill_json:
                    bill_data = bill_json["bill"]
                    bill_id = bill_data.get("bill_id")

                    if bill_id:
                        year_data["bills"][bill_id] = bill_data
                        connected_data["all_bills"][bill_id] = bill_data
                        for sponsor in bill_data.get("sponsors", []):
                            people_id = sponsor.get("people_id")
                            if people_id:
                                relationship = {
                                    "bill_id": bill_id,
                                    "people_id": people_id,
                                    "relationship_type": "sponsor",
                                    "sponsor_type": sponsor.get("sponsor_type_id", 0),
                                    "sponsor_order": sponsor.get("sponsor_order", 0)
                                }
                                year_data["bill_people_relationships"].append(relationship)
                                connected_data["bill_people_relationships"].append(relationship)

        people_dir = year_dir / "people"
        if people_dir.exists():
            people_files = list(people_dir.glob("*.json"))
            logger.info(f"Found {len(people_files)} people files in {year}")

            for people_file in people_files:
                person_json = load_json_file(people_file)
                if person_json and "person" in person_json:
                    person_data = person_json["person"]
                    people_id = person_data.get("people_id")

                    if people_id:
                        year_data["people"][people_id] = person_data
                        connected_data["all_people"][people_id] = person_data
        vote_dir = year_dir / "vote"
        if vote_dir.exists() and vote_dir.is_dir():
            vote_files = list(vote_dir.glob("*.json"))
            logger.info(f"Found {len(vote_files)} vote files in {year}")

            for vote_file in vote_files:
                vote_json = load_json_file(vote_file)
                if vote_json and "roll_call" in vote_json:
                    roll_call_data = vote_json["roll_call"]
                    roll_call_id = roll_call_data.get("roll_call_id")
                    bill_id = roll_call_data.get("bill_id")

                    if roll_call_id:
                        year_data["votes"][roll_call_id] = roll_call_data
                        connected_data["all_votes"][roll_call_id] = roll_call_data
                        if bill_id:
                            relationship = {
                                "roll_call_id": roll_call_id,
                                "bill_id": bill_id,
                                "date": roll_call_data.get("date", ""),
                                "chamber": roll_call_data.get("chamber", ""),
                                "passed": roll_call_data.get("passed", 0)
                            }
                            year_data["bill_vote_relationships"].append(relationship)
                            connected_data["bill_vote_relationships"].append(relationship)
                        for vote in roll_call_data.get("votes", []):
                            people_id = vote.get("people_id")
                            if people_id:
                                relationship = {
                                    "roll_call_id": roll_call_id,
                                    "people_id": people_id,
                                    "vote_id": vote.get("vote_id", 0),
                                    "vote_text": vote.get("vote_text", "")
                                }
                                year_data["people_vote_relationships"].append(relationship)
                                connected_data["people_vote_relationships"].append(relationship)
    logger.info("Saving connected data...")
    summary = {
        "total_bills": len(connected_data["all_bills"]),
        "total_people": len(connected_data["all_people"]),
        "total_votes": len(connected_data["all_votes"]),
        "bill_people_relationships": len(connected_data["bill_people_relationships"]),
        "bill_vote_relationships": len(connected_data["bill_vote_relationships"]),
        "people_vote_relationships": len(connected_data["people_vote_relationships"]),
        "years_processed": list(connected_data["years"].keys())
    }

    save_json_file(summary, output_dir / "summary.json")
    save_json_file(connected_data, output_dir / "full_connected_data.json")
    save_json_file(connected_data["bill_people_relationships"], output_dir / "bill_people_relationships.json")
    save_json_file(connected_data["bill_vote_relationships"], output_dir / "bill_vote_relationships.json")
    save_json_file(connected_data["people_vote_relationships"], output_dir / "people_vote_relationships.json")
    for year, year_data in connected_data["years"].items():
        central_year_dir = output_dir / year
        central_year_dir.mkdir(exist_ok=True)

        save_json_file(year_data["bills"], central_year_dir / "bills.json")
        save_json_file(year_data["people"], central_year_dir / "people.json")
        save_json_file(year_data["votes"], central_year_dir / "votes.json")
        save_json_file(year_data["bill_people_relationships"], central_year_dir / "bill_people_relationships.json")
        save_json_file(year_data["bill_vote_relationships"], central_year_dir / "bill_vote_relationships.json")
        save_json_file(year_data["people_vote_relationships"], central_year_dir / "people_vote_relationships.json")

        summary = {
            "total_bills": len(connected_data["all_bills"]),
            "total_people": len(connected_data["all_people"]),
            "total_votes": len(connected_data["all_votes"]),
            "bill_people_relationships": len(connected_data["bill_people_relationships"]),
            "bill_vote_relationships": len(connected_data["bill_vote_relationships"]),
            "people_vote_relationships": len(connected_data["people_vote_relationships"]),
            "years_processed": list(connected_data["years"].keys())
        }
    save_json_file(summary, output_dir / "summary.json")

    logger.info(f"Connected data saved to {output_dir}")
    return connected_data


def create_database_format(connected_data, output_dir, bills_dir):
    """
    :param connected_data: Connected data from connect_bill_people_vote
    :param output_dir: Central directory to save CSV files
    :param bills_dir: Original bills directory path
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)
    bills_path = Path(bills_dir)

    bills_rows = []
    for bill_id, bill_data in connected_data["all_bills"].items():
        bills_rows.append({
            "bill_id": bill_id,
            "state": bill_data.get("state", ""),
            "bill_number": bill_data.get("bill_number", ""),
            "title": bill_data.get("title", ""),
            "description": bill_data.get("description", ""),
            "session_id": bill_data.get("session_id", ""),
            "year_start": bill_data.get("session", {}).get("year_start", ""),
            "year_end": bill_data.get("session", {}).get("year_end", ""),
            "status": bill_data.get("status", ""),
            "status_date": bill_data.get("status_date", "")
        })

    people_rows = []
    for people_id, person_data in connected_data["all_people"].items():
        people_rows.append({
            "people_id": people_id,
            "name": person_data.get("name", ""),
            "party": person_data.get("party", ""),
            "role": person_data.get("role", ""),
            "district": person_data.get("district", ""),
            "state_id": person_data.get("state_id", "")
        })

    votes_rows = []
    for vote_id, vote_data in connected_data["all_votes"].items():
        votes_rows.append({
            "roll_call_id": vote_id,
            "bill_id": vote_data.get("bill_id", ""),
            "date": vote_data.get("date", ""),
            "description": vote_data.get("desc", ""),
            "chamber": vote_data.get("chamber", ""),
            "yea": vote_data.get("yea", 0),
            "nay": vote_data.get("nay", 0),
            "passed": vote_data.get("passed", 0)
        })

    import pandas as pd
    bills_df = pd.DataFrame(bills_rows)
    people_df = pd.DataFrame(people_rows)
    votes_df = pd.DataFrame(votes_rows)
    bill_people_df = pd.DataFrame(connected_data["bill_people_relationships"])
    bill_vote_df = pd.DataFrame(connected_data["bill_vote_relationships"])
    people_vote_df = pd.DataFrame(connected_data["people_vote_relationships"])

    bills_df.to_csv(output_path / "bills.csv", index=False)
    people_df.to_csv(output_path / "people.csv", index=False)
    votes_df.to_csv(output_path / "votes.csv", index=False)
    bill_people_df.to_csv(output_path / "bill_people.csv", index=False)
    bill_vote_df.to_csv(output_path / "bill_vote.csv", index=False)
    people_vote_df.to_csv(output_path / "people_vote.csv", index=False)

    logger.info(f"CSV files saved to {output_path}")
    for year, year_data in connected_data["years"].items():
        year_dir = bills_path / year
        if year_dir.exists():
            year_csv_dir = year_dir / "connected_data" / "csv"
            year_csv_dir.mkdir(exist_ok=True, parents=True)
            year_bill_ids = list(year_data["bills"].keys())
            year_people_ids = list(year_data["people"].keys())
            year_vote_ids = list(year_data["votes"].keys())
            year_bills_df = bills_df[bills_df["bill_id"].isin(year_bill_ids)]
            year_people_df = people_df[people_df["people_id"].isin(year_people_ids)]
            year_votes_df = votes_df[votes_df["roll_call_id"].isin(year_vote_ids)]
            year_bills_df.to_csv(year_csv_dir / "bills.csv", index=False)
            year_people_df.to_csv(year_csv_dir / "people.csv", index=False)
            year_votes_df.to_csv(year_csv_dir / "votes.csv", index=False)
            pd.DataFrame(year_data["bill_people_relationships"]).to_csv(year_csv_dir / "bill_people.csv", index=False)
            pd.DataFrame(year_data["bill_vote_relationships"]).to_csv(year_csv_dir / "bill_vote.csv", index=False)
            pd.DataFrame(year_data["people_vote_relationships"]).to_csv(year_csv_dir / "people_vote.csv", index=False)

            logger.info(f"Year-specific CSV files saved to {year_csv_dir}")


def main():
    # Get path to bills directory
    bills_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "bills")
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "connected_data")

    logger.info(f"Bills directory: {bills_dir}")
    logger.info(f"Output directory: {output_dir}")
    print("=" * 80)
    print(f"This script will:")
    print(f"1. Process all bill, people, and vote JSON files in {bills_dir}")
    print(f"2. Create connections between bills, people, and votes")
    print(f"3. Save the connected data to {output_dir}")
    print("=" * 80)
    print("Do you want to proceed? (y/n)")

    user_input = input().strip().lower()
    if user_input != 'y':
        print("Operation cancelled by user")
        return
    connected_data = connect_bill_people_vote(bills_dir, output_dir)

    if connected_data:
        create_database_format(connected_data, os.path.join(output_dir, "csv"), bills_dir)

        print("=" * 80)
        print("PROCESS COMPLETED SUCCESSFULLY:")
        print(f"Processed {len(connected_data['all_bills'])} bills")
        print(f"Processed {len(connected_data['all_people'])} people")
        print(f"Processed {len(connected_data['all_votes'])} votes")
        print(f"Created {len(connected_data['bill_people_relationships'])} bill-people relationships")
        print(f"Created {len(connected_data['bill_vote_relationships'])} bill-vote relationships")
        print(f"Created {len(connected_data['people_vote_relationships'])} people-vote relationships")
        print(f"Data has been saved to {output_dir}")
        print("=" * 80)
    else:
        print("Process failed. Please check the log for details")


if __name__ == "__main__":
    main()