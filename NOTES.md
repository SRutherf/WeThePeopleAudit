Bill history goes back to 2009, but maybe we can go back 10 years for the POC
186th (2009 - 2010) (7787)
185th (2007 - 2008) (1)


Structure of the CTHRU spending data/what each column means
    Identifiers & Metadata
    Base_Id / base_id – A unique identifier for each spending record.
    Encumbrance_Id – An identifier for funds that have been committed but not yet spent.
    Payment_Id – A unique identifier for each payment transaction.
    Vendor_Id – A unique identifier for each vendor receiving payment.
    Budget & Fiscal Information
    Budget_Fiscal_Year / budget_fiscal_year – The fiscal year in which the spending occurred.
    Fiscal_Period / fiscal_period – The specific period within the fiscal year (e.g., month or quarter).
    Date / date – The date when the spending transaction took place.
    Create_Date / create_date – The date when the record was created in the system.
    Government Entities
    Cabinet_Secretariat / cabinet_secretariat – The overseeing secretariat responsible for the expenditure.
    Department / department – The specific state department responsible for the spending.
    Department_Code – A code representing the department.
    Fund & Appropriations
    Appropriation_Type – The type of budgetary appropriation (e.g., general fund, special fund).
    Appropriation_Name – The name of the appropriation from which funds were drawn.
    Appropriation_Code – A code identifying the appropriation.
    Fund – The specific fund from which the money was allocated.
    Fund_Code – A code representing the fund.
    Expense Classification
    Object_Class – A broad classification of the type of expenditure (e.g., personnel, equipment).
    Object_Code – A more granular classification of expenditures.
    Object – A further description of the spending category.
    Payment & Vendor Details
    Vendor / vendor – The name of the vendor receiving payment.
    Payment_Method – The method used for the payment (e.g., check, electronic transfer).
    Geographical Information
    State / state – The state where the payment or spending occurred.
    City / city – The city associated with the payment.
    Zip_Code / zip_code – The ZIP code associated with the transaction.
    Financial Data

Same thing for the bill data
    Top-Level Keys
    bill (object) – Contains all information about the bill, including metadata, status, history, sponsors, related bills, and supporting documents.
    Bill Metadata
    bill_id (integer) – Unique identifier for this bill in the LegiScan system.
    change_hash (string) – A hash value representing the current state of the bill's data.
    session_id (integer) – Unique identifier for the legislative session in which the bill was introduced.
    Session Information
    session (object) – Information about the legislative session.
    session_id (integer) – Unique ID for the session.
    state_id (integer) – Unique ID for the state (Massachusetts).
    year_start / year_end (integer) – Start and end year of the session.
    prefile (boolean, 0/1) – Indicates if the bill was prefiled before the session started.
    sine_die (boolean, 0/1) – Indicates if the session ended without setting a new meeting date.
    prior (boolean, 0/1) – Indicates if this session follows a previous legislative session.
    special (boolean, 0/1) – Indicates if this is a special session.
    session_tag (string) – Label for the session (e.g., "Regular Session").
    session_title (string) – Full name of the session.
    session_name (string) – Another representation of the session name.
    Bill Status & Progress
    url (string) – LegiScan URL for the bill.
    state_link (string) – Official Massachusetts legislature URL for the bill.
    completed (boolean, 0/1) – Indicates whether the bill has completed the legislative process.
    status (integer) – Current status of the bill (e.g., 4 = signed into law).
    status_date (string, YYYY-MM-DD) – Date when the bill last changed status.
    progress (array) – Tracks the bill's progress with timestamps.
    date (string, YYYY-MM-DD) – When the event happened.
    event (integer) – Numerical code representing a legislative event (e.g., introduction, passage).
    Bill Details
    state (string) – State abbreviation (MA for Massachusetts).
    state_id (integer) – Unique identifier for the state.
    bill_number (string) – Official bill number (e.g., "H58").
    bill_type (string) – The type of bill (e.g., "B" for budget).
    bill_type_id (integer) – Numeric identifier for the bill type.
    body (string) – Chamber where the bill was introduced ("H" for House).
    body_id (integer) – Numeric ID for the legislative chamber.
    current_body (string) – The chamber currently handling the bill ("H" for House).
    current_body_id (integer) – Numeric ID for the current chamber.
    title (string) – The bill's official title.
    description (string) – A brief summary of the bill.
    Committee & Legislative Actions
    pending_committee_id (integer) – If the bill is pending in a committee, this ID identifies it.
    committee (array) – Committees involved in the bill (empty if no active committee).
    referrals (array) – Information on committee referrals.
    date (string, YYYY-MM-DD) – Date of referral.
    committee_id (integer) – Unique committee identifier.
    chamber (string) – Legislative chamber ("H" for House, "S" for Senate).
    chamber_id (integer) – Numeric ID for the chamber.
    name (string) – Name of the committee.
    Bill History
    history (array) – Chronological actions taken on the bill.
    date (string, YYYY-MM-DD) – Date of the action.
    action (string) – Description of the legislative action.
    chamber (string) – Legislative chamber where the action occurred.
    chamber_id (integer) – Numeric ID for the chamber.
    importance (integer) – Numeric ranking of how significant the action is.
    Bill Sponsors
    sponsors (array) – Lists legislators or committees sponsoring the bill.
    people_id (integer) – Unique ID for the sponsor.
    person_hash (string) – Hash value for the sponsor's identity.
    party_id (integer) – Unique ID for the political party.
    state_id (integer) – ID of the sponsor’s state.
    party (string) – Political party (empty for committee sponsors).
    role_id (integer) – Role identifier.
    role (string) – The sponsor's role (e.g., "Rep").
    name (string) – Sponsor’s name.
    committee_sponsor (boolean, 0/1) – Whether the sponsor is a committee.
    committee_id (integer) – Unique ID of the sponsoring committee.
    Related Bills
    sasts (array) – Related bills (e.g., replacements, similar bills).
    type_id (integer) – Type of relationship (e.g., replaces, similar to).
    type (string) – Description of the relationship.
    sast_bill_number (string) – Bill number of the related bill.
    sast_bill_id (integer) – Unique identifier of the related bill.
    Subjects
    subjects (array) – Categories/topics associated with the bill (empty in this case).
    Bill Text Versions
    texts (array) – Available versions of the bill text.
    doc_id (integer) – Unique ID for the document.
    date (string, YYYY-MM-DD) – Date of publication.
    type (string) – Document type (e.g., "Introduced").
    type_id (integer) – Numeric ID for the document type.
    mime (string) – File format (e.g., PDF).
    mime_id (integer) – Numeric ID for the MIME type.
    url (string) – URL to download the document.
    state_link (string) – Official state legislature URL for the document.
    text_size (integer) – File size in bytes.
    text_hash (string) – Hash value of the document content.
    Voting Records
    votes (array) – Records of roll-call votes.
    roll_call_id (integer) – Unique identifier for the vote.
    date (string, YYYY-MM-DD) – Date of the vote.
    desc (string) – Description of the vote.
    yea / nay (integer) – Number of legislators who voted "Yes" or "No".
    nv / absent (integer) – Number of non-voters or absentees.
    total (integer) – Total number of votes.
    passed (boolean, 0/1) – Whether the vote passed.
    chamber (string) – Chamber where the vote took place.
    chamber_id (integer) – Numeric ID for the chamber.
    url (string) – LegiScan URL for the vote.
    state_link (string) – Official state legislature URL for the vote record.
    Additional Information
    amendments (array) – Amendments to the bill (empty in this case).
    supplements (array) – Additional documents related to the bill (empty in this case).
    calendar (array) – Scheduling details for bill hearings or votes (empty in this case).