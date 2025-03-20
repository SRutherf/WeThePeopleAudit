# WeThePeopleAudit
Project for tracking and scoring government spending at the state level.

# Installation
## Backend
Backend package management uses pip.  In root folder run
- cd backend/
- pip install -r requirements.txt

Create a .env file in the backend repo and add your own keys.
```
LEGISCAN_API_KEY=
SOCRATA_APP_TOKEN=
```
For Legiscan access this link (https://legiscan.com/legiscan) and create an account to generate an API key.  Free tier should be fine.

For Socrata access this link (https://dev.socrata.com/foundry/cthru.data.socrata.com/pegc-naaa) and click on "Sign up for an app token"
# Architecture
- Ingestion Layer: AWS Lambda, Databricks (Notebooks/Jobs)
- Storage: AWS S3 (Raw & Processed Data)
- Processing & Transformation: Databricks (ETL [extract, transform, load], data linking), Spark
- Analysis & Reporting: Databricks Notebooks, Tableau (Easily integrated with DB), SparkSQL
- Deployment & Automation: AWS Step Functions, Databricks Workflows

# Useful Data Links
## Spending

- Proposed Spending: https://www.mass.gov/how-to/view-the-fiscal-year-2025-budget
- Offers downloads but will also require web scraping
    - The governor's proposed budget for the next year.
    - The Budget Recommendation comes at the beginning of the year.  This page includes a full budget proposal and some links explaining it's content which could help us determine spending intent.  Examples include the Governor's Proposal Letter or the Fiscal Health and Prospects page.  
    - The Budget comes out around the middle of the year.  This page includes an updated budget proposal and some links explaining why changes were made which could help us determine spending intent.  Examples include the Veto Documents pdfs which explains why each line item was reduced, vetoed, or increased.   
    - The Budget Recommendation doesn't offer simple excel downloads but the Budget page does.  
- Actual Spending: https://cthruspending.mass.gov/#!/year/2025/
- Full data is available as download.  Can also filter on site first and then download.
    - You can view the data online through the gui and export filtered data with the export button.
    - Or for the full report you can click "View Data in Worksheet" at the bottom right and download all the data as a csv.

## Legislation
- Legislation data: https://malegislature.gov/
- Lesiglation API: Don't see a way to bulk download.  Need to download pdfs from individual bills.
    - Each bill has some useful information on their repsective pages such as who created the bill, who supported it, similar bills, important dates, etc...  Also lets you download the bill as a pdf.
    -  Also let's you download the budget as a pdf.
- https://pluralpolicy.com/open/
    - A site which lets you download legislation from numerous states in a unified format.  Might be helpful but haven't looked into it much.
- https://legiscan.com/MA/datasets
- https://legiscan.com/MA/legislation/2025?type=bill
    - This has api and contains all the data we need, go with this.  Cost $25 for one state.

## Performance
- State Metrics Data: https://data.mass.gov/
    - An assortment of datasets, reports, and APIS.  Links to 3rd party sites so while the original site tells you whether you can access the data as csv/pdf/html/other you still need to figure out the individual ways to access it.
- State Map Data: https://gis.data.mass.gov/
    - Map based data.  Mostly related to housing/census/and geographic data.  Might not be relevant but could have some juicy info.