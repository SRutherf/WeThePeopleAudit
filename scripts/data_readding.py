import pandas as pd
from tqdm import tqdm
import os
from pathlib import Path
"""
This would be the 2 script to run after the spending_cleaning files is fully ran.(This showcase and assignment of the districts and correct values) 
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

district_mapping = {
    # District 1
    'ADAMS': 'District 1', 'ALFORD': 'District 1', 'BECKET': 'District 1', 'CHESHIRE': 'District 1',
    'CLARKSBURG': 'District 1', 'DALTON': 'District 1', 'EGREMONT': 'District 1', 'FLORIDA': 'District 1',
    'GREAT BARRINGTON': 'District 1', 'HANCOCK': 'District 1', 'HINSDALE': 'District 1', 'LANESBOROUGH': 'District 1',
    'LEE': 'District 1', 'LENOX': 'District 1', 'MONTEREY': 'District 1', 'MOUNT WASHINGTON': 'District 1',
    'NEW ASHFORD': 'District 1', 'NEW MARLBOROUGH': 'District 1', 'NORTH ADAMS': 'District 1', 'OTIS': 'District 1',
    'PERU': 'District 1', 'PITTSFIELD': 'District 1', 'RICHMOND': 'District 1', 'SANDISFIELD': 'District 1',
    'SAVOY': 'District 1', 'SHEFFIELD': 'District 1', 'STOCKBRIDGE': 'District 1', 'TYRINGHAM': 'District 1',
    'WASHINGTON': 'District 1', 'WEST STOCKBRIDGE': 'District 1', 'WILLIAMSTOWN': 'District 1', 'WINDSOR': 'District 1',

    # District 2
    'ASHFIELD': 'District 2', 'BERNARDSTON': 'District 2', 'BUCKLAND': 'District 2', 'COLRAIN': 'District 2',
    'CONWAY': 'District 2', 'DEERFIELD': 'District 2', 'ERVING': 'District 2', 'GILL': 'District 2',
    'GREENFIELD': 'District 2', 'HEATH': 'District 2', 'LEVERETT': 'District 2', 'LEYDEN': 'District 2',
    'MONTAGUE': 'District 2', 'NEW SALEM': 'District 2', 'NORTHFIELD': 'District 2', 'ORANGE': 'District 2',
    'SHELBURNE': 'District 2', 'SHUTESBURY': 'District 2', 'SUNDERLAND': 'District 2', 'WARWICK': 'District 2',
    'WENDELL': 'District 2', 'WHATELY': 'District 2',

    # District 3
    'HAVERHILL': 'District 3', 'LAWRENCE': 'District 3', 'METHUEN': 'District 3', 'ACTON': 'District 3',
    'ASHBY': 'District 3', 'AYER': 'District 3', 'BILLERICA': 'District 3', 'BOXBOROUGH': 'District 3',
    'CARLISLE': 'District 3', 'CHELMSFORD': 'District 3', 'CONCORD': 'District 3', 'DRACUT': 'District 3',
    'DUNSTABLE': 'District 3', 'GROTON': 'District 3', 'HUDSON': 'District 3', 'LITTLETON': 'District 3',
    'LOWELL': 'District 3', 'MARLBOROUGH': 'District 3', 'PEPPERELL': 'District 3', 'SHIRLEY': 'District 3',
    'STOW': 'District 3', 'TOWNSEND': 'District 3', 'TYNGSBOROUGH': 'District 3', 'WESTFORD': 'District 3',
    'ASHBURNHAM': 'District 3', 'BERLIN': 'District 3', 'BOLTON': 'District 3', 'CLINTON': 'District 3',
    'FITCHBURG': 'District 3', 'GARDNER': 'District 3', 'HARVARD': 'District 3', 'LANCASTER': 'District 3',
    'LUNENBURG': 'District 3', 'WESTMINSTER': 'District 3', 'WINCHENDON': 'District 3',

    # District 4
    'ATTLEBORO': 'District 4', 'BERKLEY': 'District 4', 'DIGHTON': 'District 4', 'FALL RIVER': 'District 4',
    'FREETOWN': 'District 4', 'MANSFIELD': 'District 4', 'NORTH ATTLEBOROUGH': 'District 4', 'NORTON': 'District 4',
    'RAYNHAM': 'District 4', 'REHOBOTH': 'District 4', 'SEEKONK': 'District 4', 'SOMERSET': 'District 4',
    'SWANSEA': 'District 4', 'TAUNTON': 'District 4', 'NEWTON': 'District 4', 'SHERBORN': 'District 4',
    'BELLINGHAM': 'District 4', 'BROOKLINE': 'District 4', 'DOVER': 'District 4', 'FOXBOROUGH': 'District 4',
    'FRANKLIN': 'District 4', 'MEDFIELD': 'District 4', 'MILLIS': 'District 4', 'NEEDHAM': 'District 4',
    'NORFOLK': 'District 4', 'PLAINVILLE': 'District 4', 'SHARON': 'District 4', 'WELLESLEY': 'District 4',
    'WRENTHAM': 'District 4', 'LAKEVILLE': 'District 4', 'BLACKSTONE': 'District 4', 'HOPEDALE': 'District 4',
    'MENDON': 'District 4', 'MILFORD': 'District 4', 'MILLVILLE': 'District 4',

    # District 5
    'ARLINGTON': 'District 5', 'BEDFORD': 'District 5', 'BELMONT': 'District 5', 'CAMBRIDGE': 'District 5',
    'FRAMINGHAM': 'District 5', 'LEXINGTON': 'District 5', 'LINCOLN': 'District 5', 'MALDEN': 'District 5',
    'MAYNARD': 'District 5', 'MEDFORD': 'District 5', 'MELROSE': 'District 5', 'NATICK': 'District 5',
    'STONEHAM': 'District 5', 'SUDBURY': 'District 5', 'WALTHAM': 'District 5', 'WATERTOWN': 'District 5',
    'WAYLAND': 'District 5', 'WESTON': 'District 5', 'WINCHESTER': 'District 5', 'WOBURN': 'District 5',
    'WELLESLEY': 'District 5', 'REVERE': 'District 5', 'WINTHROP': 'District 5',

    # District 6
    'AMESBURY': 'District 6', 'ANDOVER': 'District 6', 'BEVERLY': 'District 6', 'BOXFORD': 'District 6',
    'DANVERS': 'District 6', 'ESSEX': 'District 6', 'GEORGETOWN': 'District 6', 'GLOUCESTER': 'District 6',
    'GROVELAND': 'District 6', 'HAMILTON': 'District 6', 'IPSWICH': 'District 6', 'LYNN': 'District 6',
    'LYNNFIELD': 'District 6', 'MANCHESTER-BY-THE-SEA': 'District 6', 'MARBLEHEAD': 'District 6',
    'MERRIMAC': 'District 6', 'MIDDLETON': 'District 6', 'NAHANT': 'District 6', 'NEWBURY': 'District 6',
    'NEWBURYPORT': 'District 6', 'NORTH ANDOVER': 'District 6', 'PEABODY': 'District 6', 'ROCKPORT': 'District 6',
    'ROWLEY': 'District 6', 'SALEM': 'District 6', 'SALISBURY': 'District 6', 'SAUGUS': 'District 6',
    'SWAMPSCOTT': 'District 6', 'TOPSFIELD': 'District 6', 'WENHAM': 'District 6', 'WEST NEWBURY': 'District 6',
    'BEDFORD': 'District 6', 'BILLERICA': 'District 6', 'BURLINGTON': 'District 6', 'NORTH READING': 'District 6',
    'READING': 'District 6', 'TEWKSBURY': 'District 6', 'WAKEFIELD': 'District 6', 'WILMINGTON': 'District 6',

    # District 7
    'CAMBRIDGE': 'District 7', 'EVERETT': 'District 7', 'SOMERVILLE': 'District 7', 'MILTON': 'District 7',
    'RANDOLPH': 'District 7', 'BOSTON': 'District 7', 'CHELSEA': 'District 7',

    # District 8
    'EASTON': 'District 8', 'AVON': 'District 8', 'BRAINTREE': 'District 8', 'CANTON': 'District 8',
    'DEDHAM': 'District 8', 'HOLBROOK': 'District 8', 'MILTON': 'District 8', 'NORWOOD': 'District 8',
    'QUINCY': 'District 8', 'STOUGHTON': 'District 8', 'WALPOLE': 'District 8', 'WESTWOOD': 'District 8',
    'WEYMOUTH': 'District 8', 'ABINGTON': 'District 8', 'BROCKTON': 'District 8', 'EAST BRIDGEWATER': 'District 8',
    'HINGHAM': 'District 8', 'HULL': 'District 8', 'WEST BRIDGEWATER': 'District 8', 'WHITMAN': 'District 8',

    # District 9
    'BARNSTABLE': 'District 9', 'BOURNE': 'District 9', 'BREWSTER': 'District 9', 'CHATHAM': 'District 9',
    'DENNIS': 'District 9', 'EASTHAM': 'District 9', 'FALMOUTH': 'District 9', 'HARWICH': 'District 9',
    'MASHPEE': 'District 9', 'ORLEANS': 'District 9', 'PROVINCETOWN': 'District 9', 'SANDWICH': 'District 9',
    'TRURO': 'District 9', 'WELLFLEET': 'District 9', 'YARMOUTH': 'District 9', 'ACUSHNET': 'District 9',
    'DARTMOUTH': 'District 9', 'FAIRHAVEN': 'District 9', 'NEW BEDFORD': 'District 9', 'RAYNHAM': 'District 9',
    'WESTPORT': 'District 9', 'AQUINNAH': 'District 9', 'CHILMARK': 'District 9', 'EDGARTOWN': 'District 9',
    'GOSNOLD': 'District 9', 'OAK BLUFFS': 'District 9', 'TISBURY': 'District 9', 'WEST TISBURY': 'District 9',
    'NANTUCKET': 'District 9', 'COHASSET': 'District 9', 'BRIDGEWATER': 'District 9', 'CARVER': 'District 9',
    'DUXBURY': 'District 9', 'HALIFAX': 'District 9', 'HANOVER': 'District 9', 'HANSON': 'District 9',
    'KINGSTON': 'District 9', 'MARION': 'District 9', 'MARSHFIELD': 'District 9', 'MATTAPOISETT': 'District 9',
    'MIDDLEBOROUGH': 'District 9', 'NORWELL': 'District 9', 'PEMBROKE': 'District 9', 'PLYMOUTH': 'District 9',
    'PLYMPTON': 'District 9', 'ROCHESTER': 'District 9', 'ROCKLAND': 'District 9', 'SCITUATE': 'District 9',
    'WAREHAM': 'District 9'
}

senate_mapping = {
    #Berkshire, Hampden, Franklin, and Hampshire
    "ADAMS": "SD-BERKSH",
    "ALFORD": "SD-BERKSH",
    "ASHFIELD": "SD-BERKSH",
    "BECKET": "SD-BERKSH",
    "BLANDFORD": "SD-BERKSH",
    "BUCKLAND": "SD-BERKSH",
    "CHARLEMONT": "SD-BERKSH",
    "CHESHIRE": "SD-BERKSH",
    "CHESTER": "SD-BERKSH",
    "CHESTERFIELD": "SD-BERKSH",
    "CLARKSBURG": "SD-BERKSH",
    "COLRAIN": "SD-BERKSH",
    "CONWAY": "SD-BERKSH",
    "CUMMINGTON": "SD-BERKSH",
    "DALTON": "SD-BERKSH",
    "EGREMONT": "SD-BERKSH",
    "FLORIDA": "SD-BERKSH",
    "GOSHEN": "SD-BERKSH",
    "GRANVILLE": "SD-BERKSH",
    "GREAT BARRINGTON": "SD-BERKSH",
    "HANCOCK": "SD-BERKSH",
    "HAWLEY": "SD-BERKSH",
    "HEATH": "SD-BERKSH",
    "HINSDALE": "SD-BERKSH",
    "HUNTINGTON": "SD-BERKSH",
    "LANESBOROUGH": "SD-BERKSH",
    "LEE": "SD-BERKSH",
    "LENOX": "SD-BERKSH",
    "MIDDLEFIELD": "SD-BERKSH",
    "MONROE": "SD-BERKSH",
    "MONTEREY": "SD-BERKSH",
    "MOUNT WASHINGTON": "SD-BERKSH",
    "NEW ASHFORD": "SD-BERKSH",
    "NEW MARLBOROUGH": "SD-BERKSH",
    "NORTH ADAMS": "SD-BERKSH",
    "OTIS": "SD-BERKSH",
    "PERU": "SD-BERKSH",
    "PITTSFIELD": "SD-BERKSH",
    "PLAINFIELD": "SD-BERKSH",
    "RICHMOND": "SD-BERKSH",
    "ROWE": "SD-BERKSH",
    "SANDISFIELD": "SD-BERKSH",
    "SAVOY": "SD-BERKSH",
    "SHEFFIELD": "SD-BERKSH",
    "SHELBURNE": "SD-BERKSH",
    "SOUTHWICK": "SD-BERKSH",
    "STOCKBRIDGE": "SD-BERKSH",
    "TOLLAND": "SD-BERKSH",
    "TYRINGHAM": "SD-BERKSH",
    "WASHINGTON": "SD-BERKSH",
    "WEST STOCKBRIDGE": "SD-BERKSH",
    "WESTHAMPTON": "SD-BERKSH",
    "WHATELY": "SD-BERKSH",
    "WILLIAMSBURG": "SD-BERKSH",
    "WILLIAMSTOWN": "SD-BERKSH",
    "WINDSOR": "SD-BERKSH",
    "WORTHINGTON": "SD-BERKSH",
    #Bristol and Norfolk
    "ATTLEBORO": "SD-BRISTO",
    "CANTON": "SD-BRISTO",
    "FOXBOROUGH": "SD-BRISTO",
    "MANSFIELD": "SD-BRISTO",
    "NORTH ATTLEBOROUGH": "SD-BRISTO",
    "NORTON": "SD-BRISTO",
    "SHARON": "SD-BRISTO",
    #First Bristol and Plymouth
    "FALL RIVER": "SD-01-PLY",
    "FREETOWN": "SD-01-PLY",
    "LAKEVILLE": "SD-01-PLY",
    "ROCHESTER": "SD-01-PLY",
    "SOMERSET": "SD-01-PLY",
    "SWANSEA": "SD-01-PLY",
    "WESTPORT": "SD-01-PLY",
    #Second Bristol and Plymouth
    "ACUSHNET": "SD-02-PLY",
    "DARTMOUTH": "SD-02-PLY",
    "FAIRHAVEN": "SD-02-PLY",
    "MATTAPOISETT": "SD-02-PLY",
    "NEW BEDFORD": "SD-02-PLY",
    #Third Bristol and Plymouth
     "BERKLEY": "SD-03-PLY",
    "CARVER": "SD-03-PLY",
    "DIGHTON": "SD-03-PLY",
    "MARION": "SD-03-PLY",
    "MIDDLEBOROUGH": "SD-03-PLY",
    "RAYNHAM": "SD-03-PLY",
    "REHOBOTH": "SD-03-PLY",
    "SEEKONK": "SD-03-PLY",
    "TAUNTON": "SD-03-PLY",
    "WAREHAM": "SD-03-PLY",
    #Cape and Islands
     "AQUINNAH": "SD-CAPE",
    "BARNSTABLE": "SD-CAPE",
    "BREWSTER": "SD-CAPE",
    "CHATHAM": "SD-CAPE",
    "CHILMARK": "SD-CAPE",
    "DENNIS": "SD-CAPE",
    "EASTHAM": "SD-CAPE",
    "EDGARTOWN": "SD-CAPE",
    "GOSNOLD": "SD-CAPE",
    "HARWICH": "SD-CAPE",
    "NANTUCKET": "SD-CAPE",
    "OAK BLUFFS": "SD-CAPE",
    "ORLEANS": "SD-CAPE",
    "PROVINCETOWN": "SD-CAPE",
    "TISBURY": "SD-CAPE",
    "TRURO": "SD-CAPE",
    "WELLFLEET": "SD-CAPE",
    "WEST TISBURY": "SD-CAPE",
    "YARMOUTH": "SD-CAPE",
    #First Essex
    "HAVERHILL, WARD 1 PRECINCT 1": "SD-01-ESS",
    "HAVERHILL, WARD 1 PRECINCT 2": "SD-01-ESS",
    "HAVERHILL, WARD 1 PRECINCT 3": "SD-01-ESS",
    "HAVERHILL, WARD 2 PRECINCT 3": "SD-01-ESS",
    "HAVERHILL, WARD 3 PRECINCT 1": "SD-01-ESS",
    "HAVERHILL, WARD 3 PRECINCT 2": "SD-01-ESS",
    "HAVERHILL, WARD 3 PRECINCT 3": "SD-01-ESS",
    "HAVERHILL, WARD 5 PRECINCT 1A": "SD-01-ESS",
    "HAVERHILL, WARD 6 PRECINCT 2A": "SD-01-ESS",
    "HAVERHILL, WARD 7 PRECINCT 2A": "SD-01-ESS",
    "LAWRENCE": "SD-01-ESS",
    "METHUEN": "SD-01-ESS",
    #Second Essex
    "BEVERLY": "SD-02-ESS",
    "DANVERS": "SD-02-ESS",
    "PEABODY": "SD-02-ESS",
    "SALEM": "SD-02-ESS",
    #Third Essex
    "LYNN": "SD-03-ESS",
    "LYNNFIELD": "SD-03-ESS",
    "MARBLEHEAD": "SD-03-ESS",
    "NAHANT": "SD-03-ESS",
    "SAUGUS": "SD-03-ESS",
    "SWAMPSCOTT": "SD-03-ESS",
    #First Essec and Middlesex
    "BOXFORD": "First Essex and Middlesex",
    "ESSEX": "First Essex and Middlesex",
    "GEORGETOWN": "First Essex and Middlesex",
    "GLOUCESTER": "First Essex and Middlesex",
    "GROVELAND": "First Essex and Middlesex",
    "HAMILTON": "First Essex and Middlesex",
    "IPSWICH": "First Essex and Middlesex",
    "MANCHESTER-BY-THE-SEA": "First Essex and Middlesex",
    "MIDDLETON": "First Essex and Middlesex",
    "NEWBURY": "First Essex and Middlesex",
    "NEWBURYPORT": "First Essex and Middlesex",
    "NORTH ANDOVER, PRECINCTS 7, 8": "First Essex and Middlesex",
    "NORTH READING": "First Essex and Middlesex",
    "ROCKPORT": "First Essex and Middlesex",
    "ROWLEY": "First Essex and Middlesex",
    "SALISBURY": "First Essex and Middlesex",
    "TOPSFIELD": "First Essex and Middlesex",
    "WENHAM": "First Essex and Middlesex",
    "WEST NEWBURY": "First Essex and Middlesex",
    #Second Essex and Middle Essex
    "AMESBURY": "Second Essex and Middlesex",
    "ANDOVER": "Second Essex and Middlesex",
    "HAVERHILL, WARD 1 PRECINCTS 2A, 3A": "Second Essex and Middlesex",
    "HAVERHILL, WARD 2 PRECINCTS 1, 2": "Second Essex and Middlesex",
    "HAVERHILL, WARD 4 PRECINCTS 1, 2, 3": "Second Essex and Middlesex",
    "HAVERHILL, WARD 5 PRECINCTS 1, 2, 3, 3A": "Second Essex and Middlesex",
    "HAVERHILL, WARD 6 PRECINCTS 1, 2, 3": "Second Essex and Middlesex",
    "HAVERHILL, WARD 7 PRECINCTS 1, 2, 3, 3A": "Second Essex and Middlesex",
    "MERRIMAC": "Second Essex and Middlesex",
    "NORTH ANDOVER, PRECINCTS 1, 2, 3, 4, 5, 6": "Second Essex and Middlesex",
    "TEWKSBURY": "Second Essex and Middlesex",
    "WILMINGTON": "Second Essex and Middlesex",
    #Hampden
     "CHICOPEE, WARD 2 PRECINCTS A, B": "SD-HAMPDE",
    "CHICOPEE, WARD 3 PRECINCTS A, A1, B": "SD-HAMPDE",
    "CHICOPEE, WARD 4 PRECINCTS A, B": "SD-HAMPDE",
    "CHICOPEE, WARD 5 PRECINCTS A, B": "SD-HAMPDE",
    "CHICOPEE, WARD 7 PRECINCT B": "SD-HAMPDE",
    "CHICOPEE, WARD 8 PRECINCT A": "SD-HAMPDE",
    "SPRINGFIELD, WARD 1": "SD-HAMPDE",
    "SPRINGFIELD, WARD 2": "SD-HAMPDE",
    "SPRINGFIELD, WARD 3": "SD-HAMPDE",
    "SPRINGFIELD, WARD 4": "SD-HAMPDE",
    "SPRINGFIELD, WARD 5": "SD-HAMPDE",
    "SPRINGFIELD, WARD 6 PRECINCTS A, C, D1, E, F, G, H": "SD-HAMPDE",
    "SPRINGFIELD, WARD 7 PRECINCTS A, A1, B1, H": "SD-HAMPDE",
    "SPRINGFIELD, WARD 8": "SD-HAMPDE",
    #Hampden and Hampshire
    "HAMPDEN AND HAMPSHIRE, AGAWAM": "Hampden and Hampshire",
    "CHICOPEE, WARD 7 PRECINCT A": "Hampden and Hampshire",
    "CHICOPEE, WARD 9 PRECINCT A": "Hampden and Hampshire",
    "EASTHAMPTON": "Hampden and Hampshire",
    "HOLYOKE": "Hampden and Hampshire",
    "MONTGOMERY": "Hampden and Hampshire",
    "RUSSELL": "Hampden and Hampshire",
    "SOUTHAMPTON": "Hampden and Hampshire",
    "WEST SPRINGFIELD": "Hampden and Hampshire",
    "WESTFIELD": "Hampden and Hampshire",
    #Hampden, Hampshire, and Worcester
     "HAMPDEN, HAMPSHIRE, AND WORCESTER, BELCHERTOWN": "Hampden, Hampshire, and Worcester",
    "CHICOPEE, WARD 1 PRECINCTS A, B": "Hampden, Hampshire, and Worcester",
    "CHICOPEE, WARD 6": "Hampden, Hampshire, and Worcester",
    "CHICOPEE, WARD 8 PRECINCT B": "Hampden, Hampshire, and Worcester",
    "CHICOPEE, WARD 9 PRECINCT B": "Hampden, Hampshire, and Worcester",
    "EAST LONGMEADOW": "Hampden, Hampshire, and Worcester",
    "GRANBY": "Hampden, Hampshire, and Worcester",
    "HAMPDEN": "Hampden, Hampshire, and Worcester",
    "LONGMEADOW": "Hampden, Hampshire, and Worcester",
    "LUDLOW": "Hampden, Hampshire, and Worcester",
    "PALMER": "Hampden, Hampshire, and Worcester",
    "SOUTH HADLEY": "Hampden, Hampshire, and Worcester",
    "SPRINGFIELD, WARD 6 PRECINCTS B, D": "Hampden, Hampshire, and Worcester",
    "SPRINGFIELD, WARD 7 PRECINCTS B, C, D, E, F, G, H1": "Hampden, Hampshire, and Worcester",
    "WARREN": "Hampden, Hampshire, and Worcester",
    "WILBRAHAM": "Hampden, Hampshire, and Worcester",
    #"Hampshire, Franklin, and Worcester
    "AMHERST": "SD-HAMPSH",
    "ASHBURNHAM": "SD-HAMPSH",
    "ATHOL": "SD-HAMPSH",
    "BERNARDSTON": "SD-HAMPSH",
    "DEERFIELD": "SD-HAMPSH",
    "ERVING": "SD-HAMPSH",
    "GILL": "SD-HAMPSH",
    "GREENFIELD": "SD-HAMPSH",
    "HADLEY": "SD-HAMPSH",
    "HATFIELD": "SD-HAMPSH",
    "LEVERETT": "SD-HAMPSH",
    "LEYDEN": "SD-HAMPSH",
    "MONTAGUE": "SD-HAMPSH",
    "NEW SALEM": "SD-HAMPSH",
    "NORTHAMPTON": "SD-HAMPSH",
    "NORTHFIELD": "SD-HAMPSH",
    "ORANGE": "SD-HAMPSH",
    "PELHAM": "SD-HAMPSH",
    "PETERSHAM": "SD-HAMPSH",
    "ROYALSTON": "SD-HAMPSH",
    "SHUTESBURY": "SD-HAMPSH",
    "SUNDERLAND": "SD-HAMPSH",
    "WARWICK": "SD-HAMPSH",
    "WENDELL": "SD-HAMPSH",
    "WINCHENDON": "SD-HAMPSH",
    #First Middlesex
    "DRACUT": "SD-01-MID",
    "DUNSTABLE": "SD-01-MID",
    "LOWELL": "SD-01-MID",
    "PEPPERELL": "SD-01-MID",
    "TYNGSBOROUGH": "SD-01-MID",
    #Second Middlesex
    "CAMBRIDGE": {
        "WARD 7 PRECINCT 1": "SD-02-MID",
        "WARD 8 PRECINCT 1": "SD-02-MID",
        "WARD 10": "SD-02-MID",
        "WARD 11": "SD-02-MID"
    },
    "MEDFORD": "SD-02-MID",
    "SOMERVILLE": "SD-02-MID",
    "WINCHESTER": {
        "PRECINCTS 4, 5, 6, 7": "SD-02-MID"
    },
    #Third Middlesex
    "BEDFORD": "SD-03-MID",
    "CARLISLE": "SD-03-MID",
    "CHELMSFORD": "SD-03-MID",
    "CONCORD": "SD-03-MID",
    "LEXINGTON": {
        "PRECINCTS 3, 8, 9": "SD-03-MID"
    },
    "LINCOLN": "SD-03-MID",
    "WALTHAM": "SD-03-MID",
    "WESTON": "SD-03-MID",
    #Fourth Middlesex
    "ARLINGTON": "SD-04-MID",
    "BILLERICA": "SD-04-MID",
    "BURLINGTON": "SD-04-MID",
    "LEXINGTON": {
        "PRECINCTS 1, 2, 4, 5, 6, 7": "SD-04-MID"
    },
    "WOBURN": "SD-04-MID",
    #Fifth Middlesex
    "MALDEN": "SD-05-MID",
    "MELROSE": "SD-05-MID",
    "READING": "SD-05-MID",
    "STONEHAM": "SD-05-MID",
    "WAKEFIELD": "SD-05-MID",
    "WINCHESTER": {
        "PRECINCTS 1, 2, 3, 8": "SD-05-MID"
    },
    #Middlesex and Norfolk
    "ASHLAND": "Middlesex and Norfolk",
    "FRAMINGHAM": "Middlesex and Norfolk",
    "HOLLISTON": "Middlesex and Norfolk",
    "HOPKINTON": "Middlesex and Norfolk",
    "MEDWAY": "Middlesex and Norfolk",
    "NATICK": "Middlesex and Norfolk",
    #Middlesex and Suffolk
    "BOSTON": {
        "WARD 2": "SD-MIDDLE"
    },
    "CAMBRIDGE": {
        "WARD 1": "SD-MIDDLE",
        "WARD 2": "SD-MIDDLE",
        "WARD 3": "SD-MIDDLE",
        "WARD 4": "SD-MIDDLE",
        "WARD 5": "SD-MIDDLE",
        "WARD 6": "SD-MIDDLE",
        "WARD 7 PRECINCTS 2, 2A, 3": "SD-MIDDLE",
        "WARD 8 PRECINCT 3": "SD-MIDDLE"
    },
    "CHELSEA": "SD-MIDDLE",
    "EVERETT": "SD-MIDDLE",
    #Middlesex and Worcester
    "ACTON": "Middlesex and Worcester",
    "AYER": "Middlesex and Worcester",
    "BOXBOROUGH": "Middlesex and Worcester",
    "HARVARD": "Middlesex and Worcester",
    "HUDSON": "Middlesex and Worcester",
    "LITTLETON": "Middlesex and Worcester",
    "MARLBOROUGH": "Middlesex and Worcester",
    "MAYNARD": "Middlesex and Worcester",
    "SOUTHBOROUGH": "Middlesex and Worcester",
    "STOW": "Middlesex and Worcester",
    "SUDBURY": "Middlesex and Worcester",
    "WAYLAND": "Middlesex and Worcester",
    #Norfolk and Middlesex
    "BROOKLINE": "Norfolk and Middlesex",
    "NEWTON": "Norfolk and Middlesex",
    "WELLESLEY": "Norfolk and Middlesex",
    #Norfolk and Plymouth
    "ABINGTON": "Norfolk and Plymouth",
    "BRAINTREE": {
        "PRECINCTS 3B, 4B, 6A": "Norfolk and Plymouth"
    },
    "HANOVER": "Norfolk and Plymouth",
    "HOLBROOK": "Norfolk and Plymouth",
    "QUINCY": "Norfolk and Plymouth",
    "ROCKLAND": "Norfolk and Plymouth",
    "BRAINTREE": {
        "PRECINCTS 1A, 1B, 2A, 2B, 3A, 4A, 5A, 5B, 6B": "Norfolk, Plymouth, and Bristol"
    },
    #Norfolk, Plymouth, Bristol
    "BRIDGEWATER": "Norfolk, Plymouth, and Bristol",
    "EASTON": "Norfolk, Plymouth, and Bristol",
    "MILTON": "Norfolk, Plymouth, and Bristol",
    "RANDOLPH": {
        "PRECINCTS 4, 5, 6, 9, 10, 11, 12": "Norfolk, Plymouth, and Bristol"
    },
    "STOUGHTON": "Norfolk, Plymouth, and Bristol",
    "WEST BRIDGEWATER": "Norfolk, Plymouth, and Bristol",
    #Norfolk and Suffolk
    "BOSTON": {
        "WARD 18 PRECINCTS 9, 10, 11, 12, 16, 17, 19, 20, 22, 23": "SD-NORFOL",
        "WARD 19 PRECINCTS 2, 3, 5, 8, 9, 10, 11, 13": "SD-NORFOL",
        "WARD 20": "SD-NORFOL"
    },
    "DEDHAM": "SD-NORFOL",
    "NORWOOD": "SD-NORFOL",
    "WALPOLE": "SD-NORFOL",
    "WESTWOOD": "SD-NORFOL",
    #Norfolk, Worcester, and Middlesex
    "BELLINGHAM": "Norfolk, Worcester, and Middlesex",
    "DOVER": "Norfolk, Worcester, and Middlesex",
    "FRANKLIN": "Norfolk, Worcester, and Middlesex",
    "MEDFIELD": "Norfolk, Worcester, and Middlesex",
    "MILFORD": "Norfolk, Worcester, and Middlesex",
    "MILLIS": "Norfolk, Worcester, and Middlesex",
    "NEEDHAM": "Norfolk, Worcester, and Middlesex",
    "NORFOLK": "Norfolk, Worcester, and Middlesex",
    "PLAINVILLE": "Norfolk, Worcester, and Middlesex",
    "SHERBORN": "Norfolk, Worcester, and Middlesex",
    "WRENTHAM": "Norfolk, Worcester, and Middlesex",
    #Plymouth and Barnstable
    "BOURNE": "SD-PLYMOU",
    "FALMOUTH": "SD-PLYMOU",
    "KINGSTON": "SD-PLYMOU",
    "MASHPEE": "SD-PLYMOU",
    "PEMBROKE": "SD-PLYMOU",
    "PLYMOUTH": "SD-PLYMOU",
    "PLYMPTON": "SD-PLYMOU",
    "SANDWICH": "SD-PLYMOU",
    #First Plymouth and Norfole
    "COHASSET": "SD-01-NOR",
    "DUXBURY": "SD-01-NOR",
    "HINGHAM": "SD-01-NOR",
    "HULL": "SD-01-NOR",
    "MARSHFIELD": "SD-01-NOR",
    "NORWELL": "SD-01-NOR",
    "SCITUATE": "SD-01-NOR",
    "WEYMOUTH": "SD-01-NOR",
    #Second Plymouth and Norfol
    "AVON": "SD-02-NOR",
    "BROCKTON": "SD-02-NOR",
    "EAST BRIDGEWATER": "SD-02-NOR",
    "HALIFAX": "SD-02-NOR",
    "HANSON": "SD-02-NOR",
    "RANDOLPH": {
        "PRECINCTS 1, 2, 3, 7, 8": "SD-02-NOR"
    },
    "WHITMAN": "SD-02-NOR",
    #First Suffolk
    "BOSTON": {
        "WARD 1 PRECINCT 15": "SD-01-SUF",
        "WARD 3 PRECINCTS 7, 8, 14, 15, 16": "SD-01-SUF",
        "WARD 4 PRECINCTS 1, 2, 3, 4, 5": "SD-01-SUF",
        "WARD 5 PRECINCTS 1, 13, 14": "SD-01-SUF",
        "WARD 6": "SD-01-SUF",
        "WARD 7": "SD-01-SUF",
        "WARD 8 PRECINCTS 1, 2, 6": "SD-01-SUF",
        "WARD 9 PRECINCTS 1, 2": "SD-01-SUF",
        "WARD 13 PRECINCTS 3, 5, 6, 7, 8, 9, 10": "SD-01-SUF",
        "WARD 15": "SD-01-SUF",
        "WARD 16": "SD-01-SUF",
        "WARD 17": "SD-01-SUF",
    },
    #Second Suffolk
    "BOSTON": {
        "WARD 4 PRECINCTS 9, 11": "SD-02-SUF",
        "WARD 8 PRECINCTS 3, 4, 5": "SD-02-SUF",
        "WARD 9 PRECINCTS 3, 4, 5, 6, 7": "SD-02-SUF",
        "WARD 10": "SD-02-SUF",
        "WARD 11": "SD-02-SUF",
        "WARD 12": "SD-02-SUF",
        "WARD 13 PRECINCTS 1, 2, 4": "SD-02-SUF",
        "WARD 14": "SD-02-SUF",
        "WARD 18 PRECINCTS 1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 15, 18, 21": "SD-02-SUF",
        "WARD 19 PRECINCTS 1, 4, 6, 7, 12": "SD-02-SUF"
    },
    #Third Suffolk
    "BOSTON": {
        "WARD 1 PRECINCTS 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14": "SD-03-SUF",
        "WARD 3 PRECINCTS 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 17": "SD-03-SUF",
        "WARD 4 PRECINCTS 6, 7, 8": "SD-03-SUF",
        "WARD 5 PRECINCTS 3, 4, 5, 6, 7, 8, 9, 11": "SD-03-SUF"
    },
    "REVERE": "SD-03-SUF",
    "WINTHROP": "SD-03-SUF",
    #Suffolk and Middlesex
    "BELMONT": "SD-SUFFOL",
    "BOSTON": {
        "WARD 4 PRECINCTS 10, 12": "SD-SUFFOL",
        "WARD 5 PRECINCTS 2, 10, 12, 15": "SD-SUFFOL",
        "WARD 21": "SD-SUFFOL",
        "WARD 22": "SD-SUFFOL"
    },
    "CAMBRIDGE": {
        "WARD 8 PRECINCT 2": "SD-SUFFOL",
        "WARD 9": "SD-SUFFOL"
    },
    "WATERTOWN": "SD-SUFFOL",
    #First Worcester
    "BERLIN": "SD-01-WOR",
    "BOLTON": "SD-01-WOR",
    "BOYLSTON": "SD-01-WOR",
    "NORTHBOROUGH": "SD-01-WOR",
    "WEST BOYLSTON": "SD-01-WOR",
    "WORCESTER": {
        "WARD 1": "SD-01-WOR",
        "WARD 2": "SD-01-WOR",
        "WARD 3": "SD-01-WOR",
        "WARD 4 PRECINCTS 2, 2B, 3": "SD-01-WOR",
        "WARD 6 PRECINCT 3": "SD-01-WOR",
        "WARD 7 PRECINCTS 1, 3": "SD-01-WOR",
        "WARD 8 PRECINCTS 1, 2, 3, 4, 6": "SD-01-WOR",
        "WARD 9 PRECINCTS 1, 2, 5, 6": "SD-01-WOR",
        "WARD 10": "SD-01-WOR",
    },
    #Second Worcester
    "AUBURN": "SD-02-WOR",
    "GRAFTON": "SD-02-WOR",
    "MILLBURY": "SD-02-WOR",
    "SHREWSBURY": "SD-02-WOR",
    "WESTBOROUGH": "SD-02-WOR",
    "WORCESTER": {
        "WARD 4 PRECINCTS 1, 2A, 4, 5, 6": "SD-02-WOR",
        "WARD 5": "SD-02-WOR",
        "WARD 6 PRECINCTS 1, 2, 4, 5, 6": "SD-02-WOR",
        "WARD 7 PRECINCT 5A": "SD-02-WOR",
        "WARD 8 PRECINCT 5": "SD-02-WOR"
    },
    #Worcester and Hampden
    "BLACKSTONE": "Worcester and Hampden",
    "BRIMFIELD": "Worcester and Hampden",
    "CHARLTON": "Worcester and Hampden",
    "DOUGLAS": "Worcester and Hampden",
    "DUDLEY": "Worcester and Hampden",
    "HOLLAND": "Worcester and Hampden",
    "HOPEDALE": "Worcester and Hampden",
    "MENDON": "Worcester and Hampden",
    "MILLVILLE": "Worcester and Hampden",
    "MONSON": "Worcester and Hampden",
    "NORTHBRIDGE": "Worcester and Hampden",
    "OXFORD": "Worcester and Hampden",
    "SOUTHBRIDGE": "Worcester and Hampden",
    "STURBRIDGE": "Worcester and Hampden",
    "SUTTON": "Worcester and Hampden",
    "UPTON": "Worcester and Hampden",
    "UXBRIDGE": "Worcester and Hampden",
    "WALES": "Worcester and Hampden",
    "WEBSTER": "Worcester and Hampden",
    #Worcester and Hampshire
    "BARRE": "Worcester and Hampshire",
    "BROOKFIELD": "Worcester and Hampshire",
    "EAST BROOKFIELD": "Worcester and Hampshire",
    "GARDNER": "Worcester and Hampshire",
    "HARDWICK": "Worcester and Hampshire",
    "HOLDEN": "Worcester and Hampshire",
    "HUBBARDSTON": "Worcester and Hampshire",
    "LEICESTER": "Worcester and Hampshire",
    "NEW BRAINTREE": "Worcester and Hampshire",
    "NORTH BROOKFIELD": "Worcester and Hampshire",
    "OAKHAM": "Worcester and Hampshire",
    "PAXTON": "Worcester and Hampshire",
    "PHILLIPSTON": "Worcester and Hampshire",
    "PRINCETON": "Worcester and Hampshire",
    "RUTLAND": "Worcester and Hampshire",
    "SPENCER": "Worcester and Hampshire",
    "STERLING": "Worcester and Hampshire",
    "TEMPLETON": "Worcester and Hampshire",
    "WARE": "Worcester and Hampshire",
    "WEST BROOKFIELD": "Worcester and Hampshire",
    "WESTMINSTER": "Worcester and Hampshire",
    "WORCESTER": {
        "WARD 7 PRECINCTS 2, 4, 5, 6": "Worcester and Hampshire",
        "WARD 9 PRECINCTS 3, 4": "Worcester and Hampshire"
    },
    #Worcester and Middlesex
    "ASHBY": "SD-WORCES",
    "CLINTON": "SD-WORCES",
    "FITCHBURG": "SD-WORCES",
    "GROTON": "SD-WORCES",
    "LANCASTER": "SD-WORCES",
    "LEOMINSTER": "SD-WORCES",
    "LUNENBURG": "SD-WORCES",
    "SHIRLEY": "SD-WORCES",
    "TOWNSEND": "SD-WORCES",
    "WESTFORD": "SD-WORCES"
}


house_mapping = {
    #First Barnstable
    "BREWSTER": "HD-01-BAR",
    "DENNIS": "HD-01-BAR",
    "YARMOUTH-1": "HD-01-BAR",
    "YARMOUTH-2": "HD-01-BAR",
    "YARMOUTH-3": "HD-01-BAR",
    "YARMOUTH-4": "HD-01-BAR",
    "YARMOUTH-7": "HD-01-BAR",
    "YARMOUTH-8": "HD-01-BAR",
    #Second Barnstable
    "BARNSTABLE-1": "HD-02-BAR",
  "BARNSTABLE-2": "HD-02-BAR",
  "BARNSTABLE-3": "HD-02-BAR",
  "BARNSTABLE-4": "HD-02-BAR",
  "BARNSTABLE-5": "HD-02-BAR",
  "BARNSTABLE-6": "HD-02-BAR",
  "BARNSTABLE-7": "HD-02-BAR",
  "BARNSTABLE-8": "HD-02-BAR",
  "BARNSTABLE-9": "HD-02-BAR",
  "BARNSTABLE-13": "HD-02-BAR",
  "YARMOUTH-5": "HD-02-BAR",
  "YARMOUTH-6": "HD-02-BAR",
  "YARMOUTH-8A": "HD-02-BAR",
    # Third Barnstable
    "BOURNE-4": "HD-03-BAR",
  "BOURNE-5": "HD-03-BAR",
  "BOURNE-6": "HD-03-BAR",
  "FALMOUTH-3": "HD-03-BAR",
  "FALMOUTH-4": "HD-03-BAR",
  "FALMOUTH-5": "HD-03-BAR",
  "FALMOUTH-7": "HD-03-BAR",
  "FALMOUTH-8": "HD-03-BAR",
  "FALMOUTH-9": "HD-03-BAR",
  "MASHPEE": "HD-03-BAR",
    # Fourth Barnstable
    "CHATHAM": "HD-04-BAR",
  "EASTHAM": "HD-04-BAR",
  "HARWICH": "HD-04-BAR",
  "ORLEANS": "HD-04-BAR",
  "PROVINCETOWN": "HD-04-BAR",
  "TRURO": "HD-04-BAR",
  "WELLFLEET": "HD-04-BAR",
    # Fifth Barnstable
    "BARNSTABLE-10": "HD-05-BAR",
  "BARNSTABLE-11": "HD-05-BAR",
  "BARNSTABLE-12": "HD-05-BAR",
  "BOURNE-1": "HD-05-BAR",
  "BOURNE-2": "HD-05-BAR",
  "BOURNE-3": "HD-05-BAR",
  "BOURNE-5A": "HD-05-BAR",
  "BOURNE-7": "HD-05-BAR",
  "SANDWICH": "HD-05-BAR",
    #Barnstable, Dukes, and Nantucket
    "AQUINNAH": "HD-BARNST",
    "CHILMARK": "HD-BARNST",
    "EDGARTOWN": "HD-BARNST",
    "FALMOUTH-1": "HD-BARNST",
    "FALMOUTH-2": "HD-BARNST",
    "FALMOUTH-6": "HD-BARNST",
    "GOSNOLD": "HD-BARNST",
    "NANTUCKET": "HD-BARNST",
    "OAK BLUFFS": "HD-BARNST",
    "TISBURY": "HD-BARNST",
    "WEST TISBURY": "HD-BARNST",
    #First Berkshire
    "ADAMS": "HD-01-BER",
    "CHESHIRE": "HD-01-BER",
    "CLARKSBURG": "HD-01-BER",
    "FLORIDA": "HD-01-BER",
    "HANCOCK": "HD-01-BER",
    "HINSDALE": "HD-01-BER",
    "LANESBOROUGH": "HD-01-BER",
    "NEW ASHFORD": "HD-01-BER",
    "NORTH ADAMS": "HD-01-BER",
    "PERU": "HD-01-BER",
    "SAVOY": "HD-01-BER",
    "WILLIAMSTOWN": "HD-01-BER",
    "WINDSOR": "HD-01-BER",
    # Second Berkshire
    "PITTSFIELD": "HD-02-BER",
    # Third Berkshire
    "ALFORD": "HD-03-BER",
    "BECKET": "HD-03-BER",
    "DALTON": "HD-03-BER",
    "EGREMONT": "HD-03-BER",
    "GREAT BARRINGTON": "HD-03-BER",
    "LEE": "HD-03-BER",
    "LENOX": "HD-03-BER",
    "MONTEREY": "HD-03-BER",
    "MOUNT WASHINGTON": "HD-03-BER",
    "NEW MARLBOROUGH": "HD-03-BER",
    "OTIS": "HD-03-BER",
    "RICHMOND": "HD-03-BER",
    "SANDISFIELD": "HD-03-BER",
    "SHEFFIELD": "HD-03-BER",
    "STOCKBRIDGE": "HD-03-BER",
    "TYRINGHAM": "HD-03-BER",
    "WASHINGTON": "HD-03-BER",
    "WEST STOCKBRIDGE": "HD-03-BER",
    #First Bristol
    "FOXBOROUGH": "HD-01-BRI",
    "MANSFIELD": "HD-01-BRI",
    "MANSFIELD PRECINCTS": "HD-01-BRI",
    "NORTON": "HD-01-BRI",
    "NORTON PRECINCTS": "HD-01-BRI",
    #Second Bristol
    "ATTLEBORO": "HD-02-BRI",
    "ATTLEBORO WARDS": "HD-02-BRI",
   # Third Bristol
"EASTON": "HD-03-BRI",
"EASTON PRECINCTS": "HD-03-BRI: 4A, 5, 6",
"TAUNTON": "HD-03-BRI",
"TAUNTON WARDS": "HD-03-BRI: Ward 1 Precincts A, B, Ward 2, Ward 5, Ward 7, Ward 8",

# Fourth Bristol
"REHOBOTH": "HD-04-BRI",
"SEEKONK": "HD-04-BRI",
"SWANSEA": "HD-04-BRI",
"SWANSEA PRECINCTS": "HD-04-BRI: 4, 5",

# Fifth Bristol
"DIGHTON": "HD-05-BRI",
"SOMERSET": "HD-05-BRI",
"SOMERSET SWANSEA": "HD-05-BRI: Precincts 1, 2, 3",

# Sixth Bristol
"FALL RIVER": "HD-06-BRI",
"FALL RIVER WARDS": "HD-06-BRI: Ward 5 Precincts B, C, Ward 6 Precinct C, Ward 7, Ward 8, Ward 9",
"FREETOWN": "HD-06-BRI",
"FREETOWN PRECINCTS": "HD-06-BRI: Precinct 1",

# Seventh Bristol
"FALL RIVER WARD 1": "HD-07-BRI: Ward 1 Precincts B, C",
"FALL RIVER WARD 2": "HD-07-BRI: Ward 2",
"FALL RIVER WARD 3": "HD-07-BRI: Ward 3",
"FALL RIVER WARD 4": "HD-07-BRI: Ward 4",
"FALL RIVER WARD 5": "HD-07-BRI: Ward 5 Precinct A",

# Eighth Bristol
"ACUSHNET": "HD-08-BRI",
"ACUSHNET PRECINCTS": "HD-08-BRI: 2, 3",
"FALL RIVER WARD 1": "HD-08-BRI: Ward 1 Precinct A",
"FALL RIVER WARD 6": "HD-08-BRI: Ward 6 Precincts A, B",
"FREETOWN PRECINCTS": "HD-08-BRI: 2, 3",
"NEW BEDFORD": "HD-08-BRI",
"NEW BEDFORD WARD 1": "HD-08-BRI: Ward 1 Precincts B1, C",
"WESTPORT": "HD-08-BRI",

# Ninth Bristol
"DARTMOUTH": "HD-09-BRI",
"NEW BEDFORD WARD 1": "HD-09-BRI: Ward 1 Precincts D, E, F",

# Tenth Bristol
"FAIRHAVEN": "HD-10-BRI",
"MARION": "HD-10-BRI",
"MATTAPOISETT": "HD-10-BRI",
"NEW BEDFORD WARD 1": "HD-10-BRI: Ward 1 Precincts A, B, C1",
"ROCHESTER": "HD-10-BRI",

# Eleventh Bristol
"NEW BEDFORD WARD 1": "HD-11-BRI: Ward 1 Precinct A1",
"NEW BEDFORD WARD 2": "HD-11-BRI: Ward 2",
"NEW BEDFORD WARD 3": "HD-11-BRI: Ward 3 Precincts A, B, C, D, F1",
"NEW BEDFORD WARD 4": "HD-11-BRI: Ward 4 Precincts A1, B, C, D, F",

# Twelfth Bristol
"BERKLEY": "HD-12-BRI",
"LAKEVILLE": "HD-12-BRI",
"MIDDLEBOROUGH": "HD-12-BRI",
"MIDDLEBOROUGH PRECINCTS": "HD-12-BRI: 2, 4, 5, 7",
"TAUNTON WARD 3": "HD-12-BRI: Ward 3 Precincts A, B",
"TAUNTON WARD 4": "HD-12-BRI: Ward 4 Precincts A, B",

# Thirteenth Bristol
"NEW BEDFORD WARD 3": "HD-13-BRI: Ward 3 Precincts E, F",
"NEW BEDFORD WARD 4": "HD-13-BRI: Ward 4 Precincts A, E",
"NEW BEDFORD WARD 5": "HD-13-BRI: Ward 5",
"NEW BEDFORD WARD 6": "HD-13-BRI: Ward 6",

# Fourteenth Bristol
"ATTLEBORO WARD 3": "HD-14-BRI: Ward 3 Precinct B",
"MANSFIELD PRECINCTS": "HD-14-BRI: 1, 2A, 5",
"NORTH ATTLEBOROUGH": "HD-14-BRI",
    # First Essex
"AMESBURY": "HD-01-ESS",
"AMESBURY PRECINCTS": "HD-01-ESS: 2, 3, 4, 5",
"MERRIMAC": "HD-01-ESS",
"NEWBURYPORT": "HD-01-ESS",
"SALISBURY": "HD-01-ESS",

# Second Essex
"GEORGETOWN": "HD-02-ESS",
"HAMILTON": "HD-02-ESS",
"IPSWICH": "HD-02-ESS",
"NEWBURY": "HD-02-ESS",
"ROWLEY": "HD-02-ESS",
"TOPSFIELD": "HD-02-ESS",
"TOPSFIELD PRECINCTS": "HD-02-ESS: 1",

# Third Essex
"HAVERHILL": "HD-03-ESS",
"HAVERHILL WARDS": "HD-03-ESS: Ward 1, Ward 2 Precinct 3, Ward 3, Ward 4, Ward 5 Precinct 3A, Ward 6, Ward 7 Precinct 3",

# Fourth Essex
"LAWRENCE": "HD-04-ESS",
"LAWRENCE WARDS": "HD-04-ESS: Ward A Precincts 1, 2, Ward B",
"METHUEN": "HD-04-ESS",
"METHUEN PRECINCTS": "HD-04-ESS: 1, 2, 4, 6A, 13, 14, 15",

# Fifth Essex
"ESSEX": "HD-05-ESS",
"GLOUCESTER": "HD-05-ESS",
"MANCHESTER-BY-THE-SEA": "HD-05-ESS",
"ROCKPORT": "HD-05-ESS",

# Sixth Essex
"BEVERLY": "HD-06-ESS",
"WENHAM": "HD-06-ESS",
"WENHAM PRECINCTS": "HD-06-ESS: 1",

# Seventh Essex
"SALEM": "HD-07-ESS",

# Eighth Essex
"LYNN": "HD-08-ESS",
"LYNN WARD 3": "HD-08-ESS: Ward 3 Precinct 4",
"LYNN WARD 4": "HD-08-ESS: Ward 4 Precincts 3A, 4",
"MARBLEHEAD": "HD-08-ESS",
"SWAMPSCOTT": "HD-08-ESS",

# Ninth Essex
"LYNN WARD 1": "HD-09-ESS: Ward 1 Precincts 1, 2",
"SAUGUS": "HD-09-ESS",
"SAUGUS PRECINCTS": "HD-09-ESS: 1, 2, 4, 5, 6, 7, 8, 9",
"WAKEFIELD": "HD-09-ESS",
"WAKEFIELD PRECINCTS": "HD-09-ESS: 1, 2, 3, 7",

# Tenth Essex
"LYNN WARD 1 EXTRA": "HD-10-ESS: Ward 1 Precincts 2A, 3, 4",
"LYNN WARD 2": "HD-10-ESS: Ward 2",
"LYNN WARD 3 EXTRA": "HD-10-ESS: Ward 3 Precincts 1, 2, 3",
"LYNN WARD 4 EXTRA": "HD-10-ESS: Ward 4 Precincts 1, 2",
"LYNN WARD 5": "HD-10-ESS: Ward 5 Precinct 3",

# Eleventh Essex
"LYNN WARD 4 ADD": "HD-11-ESS: Ward 4 Precinct 3",
"LYNN WARD 5 ADD": "HD-11-ESS: Ward 5 Precincts 1, 2, 4",
"LYNN WARD 6": "HD-11-ESS: Ward 6",
"LYNN WARD 7": "HD-11-ESS: Ward 7",
"NAHANT": "HD-11-ESS",

# Twelfth Essex
"PEABODY": "HD-12-ESS",
"PEABODY WARDS": "HD-12-ESS: Ward 1, Ward 2, Ward 3, Ward 4, Ward 5",

# Thirteenth Essex
"DANVERS": "HD-13-ESS",
"MIDDLETON": "HD-13-ESS",
"MIDDLETON PRECINCTS": "HD-13-ESS: 2",
"PEABODY WARD 6": "HD-13-ESS",
"TOPSFIELD ALT": "HD-13-ESS",
"TOPSFIELD PRECINCTS ALT": "HD-13-ESS: 2",
"WENHAM ALT": "HD-13-ESS",
"WENHAM PRECINCTS ALT": "HD-13-ESS: 1A",

# Fourteenth Essex
"AMESBURY ALT": "HD-14-ESS",
"AMESBURY PRECINCTS ALT": "HD-14-ESS: 1, 6",
"BOXFORD": "HD-14-ESS",
"BOXFORD PRECINCTS": "HD-14-ESS: 2, 3",
"GROVELAND": "HD-14-ESS",
"NORTH ANDOVER": "HD-14-ESS",
"NORTH ANDOVER PRECINCTS": "HD-14-ESS: 1, 2, 3, 4, 5, 6",
"WEST NEWBURY": "HD-14-ESS",

# Fifteenth Essex
"HAVERHILL ALT": "HD-15-ESS",
"HAVERHILL WARD 2": "HD-15-ESS: Ward 2 Precincts 1, 2",
"HAVERHILL WARD 5": "HD-15-ESS: Ward 5 Precincts 1, 1A, 2, 3",
"HAVERHILL WARD 7": "HD-15-ESS: Ward 7 Precincts 1, 2, 2A, 3A",
"METHUEN ALT": "HD-15-ESS",
"METHUEN PRECINCTS ALT": "HD-15-ESS: 5, 6, 8, 9, 10, 11, 12",

# Sixteenth Essex
"LAWRENCE ALT": "HD-16-ESS",
"LAWRENCE WARD A": "HD-16-ESS: Ward A Precincts 2A, 3, 4",
"LAWRENCE WARD E": "HD-16-ESS: Ward E Precincts 1A, 2, 3, 4",
"LAWRENCE WARD F": "HD-16-ESS: Ward F",
"METHUEN 2": "HD-16-ESS",
"METHUEN PRECINCTS 2": "HD-16-ESS: 3, 7, 13A",

# Seventeenth Essex
"ANDOVER": "HD-17-ESS",
"ANDOVER PRECINCTS": "HD-17-ESS: 2, 3, 4",
"LAWRENCE CITY": "HD-17-ESS: Ward C, Ward D, Ward E Precinct 1",

# Eighteenth Essex
"ANDOVER EXTRA": "HD-18-ESS",
"ANDOVER PRECINCTS EXTRA": "HD-18-ESS: 1, 4A, 5, 6, 7, 8, 9, 10",
"BOXFORD ALT": "HD-18-ESS",
"BOXFORD PRECINCTS ALT": "HD-18-ESS: 1",
"NORTH ANDOVER ALT": "HD-18-ESS",
"NORTH ANDOVER PRECINCTS ALT": "HD-18-ESS: 7, 8",
"TEWKSBURY": "HD-18-ESS",
"TEWKSBURY PRECINCTS": "HD-18-ESS: 3, 5A, 7",
    #First Franklin
    "ASHFIELD": "HD-01-FRA",
    "BERNARDSTON": "HD-01-FRA",
    "BUCKLAND": "HD-01-FRA",
    "CHARLEMONT": "HD-01-FRA",
    "COLRAIN": "HD-01-FRA",
    "CONWAY": "HD-01-FRA",
    "DEERFIELD": "HD-01-FRA",
    "GREENFIELD": "HD-01-FRA",
    "GREENFIELD PRECINCTS": "HD-01-FRA: 5, 6, 7, 8",
    "HAWLEY": "HD-01-FRA",
    "HEATH": "HD-01-FRA",
    "LEVERETT": "HD-01-FRA",
    "LEYDEN": "HD-01-FRA",
    "MONROE": "HD-01-FRA",
    "MONTAGUE": "HD-01-FRA",
    "ROWE": "HD-01-FRA",
    "SHELBURNE": "HD-01-FRA",
    "SUNDERLAND": "HD-01-FRA",
    "WHATELY": "HD-01-FRA",
    #Second Franklin
    "ATHOL": "HD-02-FRA",
    "ERVING": "HD-02-FRA",
    "GILL": "HD-02-FRA",
    "GREENFIELD": "HD-02-FRA",
    "GREENFIELD PRECINCTS": "HD-02-FRA: 1, 2, 3, 4, 9",
    "NORTHFIELD": "HD-02-FRA",
    "ORANGE": "HD-02-FRA",
    "PHILLIPSTON": "HD-02-FRA",
    "ROYALSTON": "HD-02-FRA",
    "WARWICK": "HD-02-FRA",
    "WINCHENDON": "HD-02-FRA",
    "WINCHENDON PRECINCTS": "HD-02-FRA: 1",
    #First Hampden
    "BRIMFIELD": "HD-01-HAM",
    "HOLLAND": "HD-01-HAM",
    "PALMER": "HD-01-HAM",
    "STURBRIDGE": "HD-01-HAM",
    "WALES": "HD-01-HAM",
    "WARE": "HD-01-HAM",
    "WARE PRECINCTS": "HD-01-HAM",
    "WARREN": "HD-01-HAM",
    #Second Hampden
    "EAST LONGMEADOW": "HD-02-HAM",
    "EAST LONGMEADOW PRECINCTS": "HD-02-HAM",
    "HAMPDEN": "HD-02-HAM",
    "LONGMEADOW": "HD-02-HAM",
    "MONSON": "HD-02-HAM",
    "MONSON PRECINCTS": "HD-02-HAM",
    "SPRINGFIELD": "HD-02-HAM",
    "SPRINGFIELD PRECINCTS": "HD-02-HAM",
    #Third Hampden
    "AGAWAM": "HD-03-HAM",
    "AGAWAM PRECINCTS": "HD-03-HAM",
    "BLANDFORD": "HD-03-HAM",
    "CHESTER": "HD-03-HAM",
    "GRANVILLE": "HD-03-HAM",
    "HUNTINGTON": "HD-03-HAM",
    "MIDDLEFIELD": "HD-03-HAM",
    "MONTGOMERY": "HD-03-HAM",
    "RUSSELL": "HD-03-HAM",
    "SOUTHWICK": "HD-03-HAM",
    "TOLLAND": "HD-03-HAM",
    #Fourth Hampden
    "SOUTHAMPTON": "HD-04-HAM",
    "WESTFIELD": "HD-04-HAM",
    "WESTFIELD WARD 1": "HD-04-HAM",
    "WESTFIELD WARD 2 PRECINCTS": "HD-04-HAM",
    "WESTFIELD WARD 3": "HD-04-HAM",
    "WESTFIELD WARD 4": "HD-04-HAM",
    "WESTFIELD WARD 5": "HD-04-HAM",
    "WESTFIELD WARD 6 PRECINCTS": "HD-04-HAM",
    #Fifth Hampden
    "CHICOPEE": "HD-05-HAM",
    "CHICOPEE WARD 3 PRECINCTS": "HD-05-HAM",
    "HOLYOKE": "HD-05-HAM",
    #Sixth Hampden
    "AGAWAM PRECINCT 1": "HD-06-HAM",
    "CHICOPEE WARD 2 PRECINCT": "HD-06-HAM",
    "CHICOPEE WARD 3 PRECINCT": "HD-06-HAM",
    "CHICOPEE WARD 4 PRECINCT": "HD-06-HAM",
    "WEST SPRINGFIELD": "HD-06-HAM",
    "WESTFIELD WARD 2 PRECINCT": "HD-06-HAM",
    "WESTFIELD WARD 6 PRECINCT": "HD-06-HAM",
    #Seventh Hampden
    "BELCHERTOWN": "HD-07-HAM",
    "LUDLOW": "HD-07-HAM",
    "NEW SALEM": "HD-07-HAM",
    "PELHAM": "HD-07-HAM",
    "PETERSHAM": "HD-07-HAM",
    "SHUTESBURY": "HD-07-HAM",
    "WENDELL": "HD-07-HAM",
    #Eigth Hampden
    "CHICOPEE WARD 1": "HD-08-HAM",
    "CHICOPEE WARD 2 PRECINCT": "HD-08-HAM",
    "CHICOPEE WARD 4 PRECINCT": "HD-08-HAM",
    "CHICOPEE WARD 5": "HD-08-HAM",
    "CHICOPEE WARD 6": "HD-08-HAM",
    "CHICOPEE WARD 7": "HD-08-HAM",
    "CHICOPEE WARD 8": "HD-08-HAM",
    "CHICOPEE WARD 9": "HD-08-HAM",
    #Ninth Hampden
    "SPRINGFIELD WARD 1 PRECINCTS": "HD-09-HAM",
    "SPRINGFIELD WARD 2": "HD-09-HAM",
    "SPRINGFIELD WARD 5 PRECINCT": "HD-09-HAM",
    "SPRINGFIELD WARD 8 PRECINCTS": "HD-09-HAM",
    #Tenth Hampden
    "SPRINGFIELD WARD 1 PRECINCTS": "HD-10-HAM",
    "SPRINGFIELD WARD 3 PRECINCTS": "HD-10-HAM",
    "SPRINGFIELD WARD 6 PRECINCTS": "HD-10-HAM",
    "SPRINGFIELD WARD 7 PRECINCT": "HD-10-HAM",
    #Eleventh Hampden
    "SPRINGFIELD WARD 3 PRECINCT": "HD-11-HAM",
    "SPRINGFIELD WARD 4": "HD-11-HAM",
    "SPRINGFIELD WARD 5 PRECINCTS": "HD-11-HAM",
    "SPRINGFIELD WARD 6 PRECINCT": "HD-11-HAM",
    "SPRINGFIELD WARD 7 PRECINCT": "HD-11-HAM",
    #Twelfth Hampden
    "EAST LONGMEADOW": "HD-12-HAM",
    "EAST LONGMEADOW PRECINCTS": "HD-12-HAM",
    "MONSON PRECINCT": "HD-12-HAM",
    "SPRINGFIELD WARD 5 PRECINCTS": "HD-12-HAM",
    "SPRINGFIELD WARD 7 PRECINCTS": "HD-12-HAM",
    "SPRINGFIELD WARD 8 PRECINCTS": "HD-12-HAM",
    "WILBRAHAM": "HD-12-HAM",
    #First Hampshire
    "CHESTERFIELD": "HD-01-HAM",
    "CUMMINGTON": "HD-01-HAM",
    "GOSHEN": "HD-01-HAM",
    "HATFIELD": "HD-01-HAM",
    "NORTHAMPTON": "HD-01-HAM",
    "PLAINFIELD": "HD-01-HAM",
    "WESTHAMPTON": "HD-01-HAM",
    "WILLIAMSBURG": "HD-01-HAM",
    "WORTHINGTON": "HD-01-HAM",
    #Second Hampshire
    "EASTHAMPTON": "HD-02-HAM",
    "GRANBY": "HD-02-HAM",
    "GRANBY PRECINCT 2": "HD-02-HAM",
    "HADLEY": "HD-02-HAM",
    "SOUTH HADLEY": "HD-02-HAM",
    #Third Hampshire
    "AMHERST": "HD-03-HAM",
    "GRANBY PRECINCTS": "HD-03-HAM: 1, 2A",
    #First Middlesex
    "ASHBY": "HD-01-MID",
    "DUNSTABLE": "HD-01-MID",
    "GROTON PRECINCT 2": "HD-01-MID",
    "GROTON PRECINCT 3": "HD-01-MID",
    "LUNENBURG PRECINCT A": "HD-01-MID",
    "LUNENBURG PRECINCT B1": "HD-01-MID",
    "LUNENBURG PRECINCT C": "HD-01-MID",
    "LUNENBURG PRECINCT D": "HD-01-MID",
"PEPPERELL": "HD-01-MID",
"TOWNSEND": "HD-01-MID",

#Second Middlesex
"CHELMSFORD PRECINCT 3B": "HD-02-MID",
"CHELMSFORD PRECINCT 4": "HD-02-MID",
"CHELMSFORD PRECINCT 5A": "HD-02-MID",
"LITTLETON": "HD-02-MID",
"WESTFORD": "HD-02-MID",

#Third Middlesex
"BOLTON": "HD-03-MID",
"HUDSON": "HD-03-MID",
"MAYNARD": "HD-03-MID",
"STOW": "HD-03-MID",

#Fourth Middlesex
"FRAMINGHAM PRECINCT 21B": "HD-04-MID",
"FRAMINGHAM PRECINCT 22": "HD-04-MID",
"FRAMINGHAM PRECINCT 23": "HD-04-MID",
"MARLBOROUGH WARD 1 PRECINCT 1A": "HD-04-MID",
"MARLBOROUGH WARD 2 PRECINCT 1": "HD-04-MID",
"MARLBOROUGH WARD 2 PRECINCT 2": "HD-04-MID",
"MARLBOROUGH WARD 3": "HD-04-MID",
"MARLBOROUGH WARD 4": "HD-04-MID",
"MARLBOROUGH WARD 5": "HD-04-MID",
"MARLBOROUGH WARD 6": "HD-04-MID",
"MARLBOROUGH WARD 7 PRECINCT 1": "HD-04-MID",
"MARLBOROUGH WARD 7 PRECINCT 2": "HD-04-MID",

#Fifth Middlesex
"NATICK": "HD-05-MID",
"WAYLAND PRECINCT 2": "HD-05-MID",
"WAYLAND PRECINCT 3": "HD-05-MID",

#Sixth Middlesex
"FRAMINGHAM PRECINCT 1": "HD-06-MID",
"FRAMINGHAM PRECINCT 2": "HD-06-MID",
"FRAMINGHAM PRECINCT 3": "HD-06-MID",
"FRAMINGHAM PRECINCT 4": "HD-06-MID",
"FRAMINGHAM PRECINCT 5": "HD-06-MID",
"FRAMINGHAM PRECINCT 6": "HD-06-MID",
"FRAMINGHAM PRECINCT 7": "HD-06-MID",
"FRAMINGHAM PRECINCT 8": "HD-06-MID",
"FRAMINGHAM PRECINCT 9B": "HD-06-MID",
"FRAMINGHAM PRECINCT 10": "HD-06-MID",
"FRAMINGHAM PRECINCT 11": "HD-06-MID",
"FRAMINGHAM PRECINCT 12": "HD-06-MID",
"FRAMINGHAM PRECINCT 13": "HD-06-MID",
"FRAMINGHAM PRECINCT 14": "HD-06-MID",
"FRAMINGHAM PRECINCT 15": "HD-06-MID",
"FRAMINGHAM PRECINCT 16": "HD-06-MID",

#Seventh Middlesex
"ASHLAND": "HD-07-MID",
"FRAMINGHAM PRECINCT 9A": "HD-07-MID",
"FRAMINGHAM PRECINCT 17": "HD-07-MID",
"FRAMINGHAM PRECINCT 18": "HD-07-MID",
"FRAMINGHAM PRECINCT 19": "HD-07-MID",
"FRAMINGHAM PRECINCT 20": "HD-07-MID",
"FRAMINGHAM PRECINCT 21C": "HD-07-MID",
"FRAMINGHAM PRECINCT 24": "HD-07-MID",
"FRAMINGHAM PRECINCT 25": "HD-07-MID",
"FRAMINGHAM PRECINCT 26": "HD-07-MID",
"FRAMINGHAM PRECINCT 27": "HD-07-MID",

#Eighth Middlesex
"HOLLISTON": "HD-08-MID",
"HOPKINTON": "HD-08-MID",
"MILLIS PRECINCT 2": "HD-08-MID",
"MILLIS PRECINCT 3": "HD-08-MID",
"SHERBORN": "HD-08-MID",

#Ninth Middlesex
"WALTHAM WARD 1 PRECINCT 1": "HD-09-MID",
"WALTHAM WARD 1 PRECINCT 2": "HD-09-MID",
"WALTHAM WARD 2": "HD-09-MID",
"WALTHAM WARD 3 PRECINCT 1": "HD-09-MID",
"WALTHAM WARD 3 PRECINCT 2": "HD-09-MID",
"WALTHAM WARD 4 PRECINCT 1": "HD-09-MID",
"WALTHAM WARD 5 PRECINCT 2": "HD-09-MID",
"WALTHAM WARD 6 PRECINCT 1": "HD-09-MID",
"WALTHAM WARD 6 PRECINCT 2A": "HD-09-MID",
"WALTHAM WARD 7": "HD-09-MID",
"WALTHAM WARD 8 PRECINCT 1": "HD-09-MID",
"WALTHAM WARD 8 PRECINCT 2A": "HD-09-MID",

#Tenth Middlesex
"NEWTON WARD 1 PRECINCT 1": "HD-10-MID",
"NEWTON WARD 1 PRECINCT 2A": "HD-10-MID",
"NEWTON WARD 1 PRECINCT 4": "HD-10-MID",
"NEWTON WARD 3 PRECINCT 4": "HD-10-MID",
"WALTHAM WARD 1 PRECINCT 2A": "HD-10-MID",
"WALTHAM WARD 3 PRECINCT 2A": "HD-10-MID",
"WALTHAM WARD 4 PRECINCT 1A": "HD-10-MID",
"WALTHAM WARD 4 PRECINCT 2": "HD-10-MID",
"WALTHAM WARD 5 PRECINCT 1": "HD-10-MID",
"WALTHAM WARD 5 PRECINCT 2A": "HD-10-MID",
"WALTHAM WARD 6 PRECINCT 2": "HD-10-MID",
"WALTHAM WARD 8 PRECINCT 2": "HD-10-MID",
"WALTHAM WARD 9": "HD-10-MID",
"WATERTOWN PRECINCT 9": "HD-10-MID",
"WATERTOWN PRECINCT 10": "HD-10-MID",
"WATERTOWN PRECINCT 11": "HD-10-MID",
"WATERTOWN PRECINCT 12": "HD-10-MID",

#Eleventh Middlesex
"NEWTON WARD 1 PRECINCT 2": "HD-11-MID",
"NEWTON WARD 1 PRECINCT 3": "HD-11-MID",
"NEWTON WARD 2": "HD-11-MID",
"NEWTON WARD 3 PRECINCT 1": "HD-11-MID",
"NEWTON WARD 3 PRECINCT 2": "HD-11-MID",
"NEWTON WARD 3 PRECINCT 3": "HD-11-MID",
"NEWTON WARD 4": "HD-11-MID",
"NEWTON WARD 7 PRECINCT 2": "HD-11-MID",
"NEWTON WARD 7 PRECINCT 3": "HD-11-MID",
"NEWTON WARD 7 PRECINCT 4": "HD-11-MID",

#Twelfth Middlesex
"BROOKLINE PRECINCT 5": "HD-12-MID",
"BROOKLINE PRECINCT 13A": "HD-12-MID",
"BROOKLINE PRECINCT 14": "HD-12-MID",
"BROOKLINE PRECINCT 15": "HD-12-MID",
"NEWTON WARD 5": "HD-12-MID",
"NEWTON WARD 6": "HD-12-MID",
"NEWTON WARD 7 PRECINCT 1": "HD-12-MID",
"NEWTON WARD 8": "HD-12-MID",
#Thirteenth Middlesex
"CONCORD PRECINCT 3": "HD-13-MID",
"CONCORD PRECINCT 4": "HD-13-MID",
"LINCOLN PRECINCT 1": "HD-13-MID",
"MARLBOROUGH WARD 1 PRECINCT 1": "HD-13-MID",
"MARLBOROUGH WARD 1 PRECINCT 2": "HD-13-MID",
"MARLBOROUGH WARD 2 PRECINCT 2A": "HD-13-MID",
"MARLBOROUGH WARD 7 PRECINCT 2A": "HD-13-MID",
"SUDBURY": "HD-13-MID",
"WAYLAND PRECINCT 1": "HD-13-MID",
"WAYLAND PRECINCT 4": "HD-13-MID",

#Fourteenth Middlesex
"ACTON PRECINCT 1": "HD-14-MID",
"ACTON PRECINCT 2": "HD-14-MID",
"ACTON PRECINCT 6": "HD-14-MID",
"ACTON PRECINCT 7": "HD-14-MID",
"CARLISLE": "HD-14-MID",
"CHELMSFORD PRECINCT 7": "HD-14-MID",
"CHELMSFORD PRECINCT 8": "HD-14-MID",
"CHELMSFORD PRECINCT 9": "HD-14-MID",
"CHELMSFORD PRECINCT 10": "HD-14-MID",
"CHELMSFORD PRECINCT 11": "HD-14-MID",
"CONCORD PRECINCT 1": "HD-14-MID",
"CONCORD PRECINCT 2": "HD-14-MID",
"CONCORD PRECINCT 5": "HD-14-MID",

#Fifteenth Middlesex
"LEXINGTON PRECINCT 1": "HD-15-MID",
"LEXINGTON PRECINCT 2": "HD-15-MID",
"LEXINGTON PRECINCT 3": "HD-15-MID",
"LEXINGTON PRECINCT 4": "HD-15-MID",
"LEXINGTON PRECINCT 5": "HD-15-MID",
"LEXINGTON PRECINCT 7": "HD-15-MID",
"LEXINGTON PRECINCT 8": "HD-15-MID",
"LEXINGTON PRECINCT 9": "HD-15-MID",
"WINCHESTER PRECINCT 6": "HD-15-MID",
"WOBURN WARD 1 PRECINCT 1": "HD-15-MID",
"WOBURN WARD 1 PRECINCT 2": "HD-15-MID",
"WOBURN WARD 7 PRECINCT 1": "HD-15-MID",
"WOBURN WARD 7 PRECINCT 2": "HD-15-MID",

#Sixteenth Middlesex
"CHELMSFORD PRECINCT 1": "HD-16-MID",
"CHELMSFORD PRECINCT 2": "HD-16-MID",
"CHELMSFORD PRECINCT 3A": "HD-16-MID",
"CHELMSFORD PRECINCT 5B": "HD-16-MID",
"CHELMSFORD PRECINCT 6": "HD-16-MID",
"LOWELL WARD 1 PRECINCT 1": "HD-16-MID",
"LOWELL WARD 1 PRECINCT 2": "HD-16-MID",
"LOWELL WARD 1 PRECINCT 3": "HD-16-MID",
"LOWELL WARD 1 PRECINCT 4": "HD-16-MID",
"LOWELL WARD 2": "HD-16-MID",
"LOWELL WARD 4 PRECINCT 4": "HD-16-MID",

#Seventeenth Middlesex
"LOWELL WARD 3": "HD-17-MID",
"LOWELL WARD 4 PRECINCT 1": "HD-17-MID",
"LOWELL WARD 4 PRECINCT 2": "HD-17-MID",
"LOWELL WARD 4 PRECINCT 3A": "HD-17-MID",
"LOWELL WARD 5 PRECINCT 1": "HD-17-MID",
"LOWELL WARD 5 PRECINCT 2": "HD-17-MID",
"LOWELL WARD 5 PRECINCT 3": "HD-17-MID",
"LOWELL WARD 5 PRECINCT 4": "HD-17-MID",
"LOWELL WARD 6 PRECINCT 3": "HD-17-MID",
"LOWELL WARD 6 PRECINCT 4A": "HD-17-MID",
"LOWELL WARD 8 PRECINCT 4A": "HD-17-MID",
"TEWKSBURY PRECINCT 1": "HD-17-MID",

#Eighteenth Middlesex
"LOWELL WARD 4 PRECINCTS 3": "HD-18-MID",
"LOWELL WARD 4 PRECINCT 4A": "HD-18-MID",
"LOWELL WARD 5 PRECINCT 1A": "HD-18-MID",
"LOWELL WARD 6 PRECINCT 1": "HD-18-MID",
"LOWELL WARD 6 PRECINCT 2": "HD-18-MID",
"LOWELL WARD 6 PRECINCT 3A": "HD-18-MID",
"LOWELL WARD 6 PRECINCT 4": "HD-18-MID",
"LOWELL WARD 7": "HD-18-MID",
"LOWELL WARD 8 PRECINCT 1": "HD-18-MID",
"LOWELL WARD 8 PRECINCT 2": "HD-18-MID",
"LOWELL WARD 8 PRECINCT 3": "HD-18-MID",
"LOWELL WARD 8 PRECINCT 4": "HD-18-MID",

#Nineteenth Middlesex
"TEWKSBURY PRECINCT 2": "HD-19-MID",
"TEWKSBURY PRECINCT 4": "HD-19-MID",
"TEWKSBURY PRECINCT 5": "HD-19-MID",
"TEWKSBURY PRECINCT 6": "HD-19-MID",
"TEWKSBURY PRECINCT 8": "HD-19-MID",
"WILMINGTON": "HD-19-MID",

#Twentieth Middlesex
"LYNNFIELD": "HD-20-MID",
"MIDDLETON PRECINCT 1": "HD-20-MID",
"MIDDLETON PRECINCT 3": "HD-20-MID",
"NORTH READING": "HD-20-MID",
"READING PRECINCT 1": "HD-20-MID",
"READING PRECINCT 7": "HD-20-MID",
"READING PRECINCT 8": "HD-20-MID",

#Twenty-First Middlesex
"BEDFORD": "HD-21-MID",
"BURINGTON": "HD-21-MID",
"LEXINGTON PRECINCT 6": "HD-21-MID",

#Twenty-Second Middlesex
"BILLERICA": "HD-22-MID",

#Twenty-Third Middlesex
"ARLINGTON PRECINCT 1": "HD-23-MID",
"ARLINGTON PRECINCT 3": "HD-23-MID",
"ARLINGTON PRECINCT 5": "HD-23-MID",
"ARLINGTON PRECINCT 7": "HD-23-MID",
"ARLINGTON PRECINCT 9": "HD-23-MID",
"ARLINGTON PRECINCT 11": "HD-23-MID",
"ARLINGTON PRECINCT 13": "HD-23-MID",
"ARLINGTON PRECINCT 14": "HD-23-MID",
"ARLINGTON PRECINCT 15": "HD-23-MID",
"ARLINGTON PRECINCT 16": "HD-23-MID",
"ARLINGTON PRECINCT 17": "HD-23-MID",
"ARLINGTON PRECINCT 18": "HD-23-MID",
"ARLINGTON PRECINCT 19": "HD-23-MID",
"ARLINGTON PRECINCT 20": "HD-23-MID",
"ARLINGTON PRECINCT 21": "HD-23-MID",
"MEDFORD WARD 3 PRECINCT 2": "HD-23-MID",
"MEDFORD WARD 6 PRECINCT 1": "HD-23-MID",
"MEDFORD WARD 6 PRECINCT 2": "HD-23-MID",

#Twenty-Fourth Middlesex
"ARLINGTON PRECINCT 2": "HD-24-MID",
"ARLINGTON PRECINCT 4": "HD-24-MID",
"ARLINGTON PRECINCT 6": "HD-24-MID",
"ARLINGTON PRECINCT 8": "HD-24-MID",
"ARLINGTON PRECINCT 10": "HD-24-MID",
"ARLINGTON PRECINCT 12": "HD-24-MID",
"BELMONT": "HD-24-MID",
"CAMBRIDGE WARD 11 PRECINCT 1": "HD-24-MID",
"CAMBRIDGE WARD 11 PRECINCT 3": "HD-24-MID",
#Twenty-Fifth Middlesex
"CAMBRIDGE WARD 3 PRECINCT 3A": "HD-25-MID",
"CAMBRIDGE WARD 4 PRECINCT 2": "HD-25-MID",
"CAMBRIDGE WARD 4 PRECINCT 2A": "HD-25-MID",
"CAMBRIDGE WARD 4 PRECINCT 3": "HD-25-MID",
"CAMBRIDGE WARD 6 PRECINCT 2": "HD-25-MID",
"CAMBRIDGE WARD 6 PRECINCT 3": "HD-25-MID",
"CAMBRIDGE WARD 7": "HD-25-MID",
"CAMBRIDGE WARD 8": "HD-25-MID",
"CAMBRIDGE WARD 10 PRECINCT 1A": "HD-25-MID",
"CAMBRIDGE WARD 10 PRECINCT 2": "HD-25-MID",

#Twenty-Sixth Middlesex
"CAMBRIDGE WARD 1 PRECINCT 3": "HD-26-MID",
"CAMBRIDGE WARD 2 PRECINCT 1": "HD-26-MID",
"CAMBRIDGE WARD 2 PRECINCT 2": "HD-26-MID",
"CAMBRIDGE WARD 2 PRECINCT 3A": "HD-26-MID",
"CAMBRIDGE WARD 3 PRECINCT 1": "HD-26-MID",
"CAMBRIDGE WARD 3 PRECINCT 2": "HD-26-MID",
"CAMBRIDGE WARD 3 PRECINCT 3": "HD-26-MID",
"CAMBRIDGE WARD 4 PRECINCT 1": "HD-26-MID",
"CAMBRIDGE WARD 5 PRECINCT 1": "HD-26-MID",
"CAMBRIDGE WARD 5 PRECINCT 3": "HD-26-MID",
"CAMBRIDGE WARD 6 PRECINCT 1": "HD-26-MID",
"CAMBRIDGE WARD 6 PRECINCT 1A": "HD-26-MID",
"SOMERVILLE WARD 1 PRECINCT 1": "HD-26-MID",
"SOMERVILLE WARD 1 PRECINCT 2": "HD-26-MID",
"SOMERVILLE WARD 1 PRECINCT 3": "HD-26-MID",
"SOMERVILLE WARD 1 PRECINCT 4": "HD-26-MID",
"SOMERVILLE WARD 2 PRECINCT 1A": "HD-26-MID",

#Twenty-Seventh Middlesex
"SOMERVILLE WARD 1 PRECINCT 4A": "HD-27-MID",
"SOMERVILLE WARD 2 PRECINCT 1": "HD-27-MID",
"SOMERVILLE WARD 2 PRECINCT 2": "HD-27-MID",
"SOMERVILLE WARD 2 PRECINCT 3": "HD-27-MID",
"SOMERVILLE WARD 2 PRECINCT 4": "HD-27-MID",
"SOMERVILLE WARD 3": "HD-27-MID",
"SOMERVILLE WARD 4 PRECINCT 2A": "HD-27-MID",
"SOMERVILLE WARD 5": "HD-27-MID",
"SOMERVILLE WARD 6 PRECINCT 1": "HD-27-MID",
"SOMERVILLE WARD 6 PRECINCT 2": "HD-27-MID",
"SOMERVILLE WARD 6 PRECINCT 3": "HD-27-MID",
"SOMERVILLE WARD 6 PRECINCT 4": "HD-27-MID",

#Twenty-Eighth Middlesex
"EVERETT WARD 1 PRECINCT 1": "HD-28-MID",
"EVERETT WARD 1 PRECINCT 2": "HD-28-MID",
"EVERETT WARD 1 PRECINCT 3A": "HD-28-MID",
"EVERETT WARD 2 PRECINCT 2": "HD-28-MID",
"EVERETT WARD 2 PRECINCT 3": "HD-28-MID",
"EVERETT WARD 3": "HD-28-MID",
"EVERETT WARD 4": "HD-28-MID",
"EVERETT WARD 5": "HD-28-MID",
"EVERETT WARD 6": "HD-28-MID",

#Twenty-Ninth Middlesex
"CAMBRIDGE WARD 9": "HD-29-MID",
"CAMBRIDGE WARD 10 PRECINCT 1": "HD-29-MID",
"CAMBRIDGE WARD 10 PRECINCT 3": "HD-29-MID",
"CAMBRIDGE WARD 11 PRECINCT 1A": "HD-29-MID",
"CAMBRIDGE WARD 11 PRECINCT 2": "HD-29-MID",
"CAMBRIDGE WARD 11 PRECINCT 3A": "HD-29-MID",
"WATERTOWN PRECINCT 1": "HD-29-MID",
"WATERTOWN PRECINCT 2": "HD-29-MID",
"WATERTOWN PRECINCT 3": "HD-29-MID",
"WATERTOWN PRECINCT 4": "HD-29-MID",
"WATERTOWN PRECINCT 5": "HD-29-MID",
"WATERTOWN PRECINCT 6": "HD-29-MID",
"WATERTOWN PRECINCT 7": "HD-29-MID",
"WATERTOWN PRECINCT 8": "HD-29-MID",

#Thirtieth Middlesex
"READING PRECINCT 2": "HD-30-MID",
"READING PRECINCT 3": "HD-30-MID",
"READING PRECINCT 4": "HD-30-MID",
"READING PRECINCT 5": "HD-30-MID",
"READING PRECINCT 6": "HD-30-MID",
"WOBURN WARD 1 PRECINCT 2A": "HD-30-MID",
"WOBURN WARD 2": "HD-30-MID",
"WOBURN WARD 3": "HD-30-MID",
"WOBURN WARD 4": "HD-30-MID",
"WOBURN WARD 5": "HD-30-MID",
"WOBURN WARD 6": "HD-30-MID",

#Thirty-First Middlesex
"STONEHAM": "HD-31-MID",
"WINCHESTER PRECINCT 1": "HD-31-MID",
"WINCHESTER PRECINCT 2": "HD-31-MID",
"WINCHESTER PRECINCT 3": "HD-31-MID",
"WINCHESTER PRECINCT 4": "HD-31-MID",
"WINCHESTER PRECINCT 5": "HD-31-MID",
"WINCHESTER PRECINCT 7": "HD-31-MID",
"WINCHESTER PRECINCT 8": "HD-31-MID",

#Thirty-Second Middlesex
"MALDEN WARD 5 PRECINCT 2": "HD-32-MID",
"MALDEN WARD 5 PRECINCT 3A": "HD-32-MID",
"MELROSE": "HD-32-MID",
"WAKEFIELD PRECINCT 4": "HD-32-MID",
"WAKEFIELD PRECINCT 5": "HD-32-MID",
"WAKEFIELD PRECINCT 6": "HD-32-MID",

#Thirty-Third Middlesex
"MALDEN WARD 2": "HD-33-MID",
"MALDEN WARD 3 PRECINCT 1": "HD-33-MID",
"MALDEN WARD 3 PRECINCT 2": "HD-33-MID",
"MALDEN WARD 3 PRECINCT 3": "HD-33-MID",
"MALDEN WARD 4": "HD-33-MID",
"MALDEN WARD 5 PRECINCT 1": "HD-33-MID",
"MALDEN WARD 5 PRECINCT 3": "HD-33-MID",
"MALDEN WARD 6": "HD-33-MID",
"MALDEN WARD 7 PRECINCT 2": "HD-33-MID",
"MALDEN WARD 7 PRECINCT 3": "HD-33-MID",
"MALDEN WARD 8": "HD-33-MID",

#Thirty-Fourth Middlesex
"MEDFORD WARD 4": "HD-34-MID",
"MEDFORD WARD 5": "HD-34-MID",
"MEDFORD WARD 7 PRECINCT 1": "HD-34-MID",
"MEDFORD WARD 7 PRECINCT 2A": "HD-34-MID",
"MEDFORD WARD 8 PRECINCT 2": "HD-34-MID",
"SOMERVILLE WARD 4 PRECINCT 1": "HD-34-MID",
"SOMERVILLE WARD 4 PRECINCT 2": "HD-34-MID",
"SOMERVILLE WARD 4 PRECINCT 3": "HD-34-MID",
"SOMERVILLE WARD 4 PRECINCT 4": "HD-34-MID",
"SOMERVILLE WARD 6 PRECINCT 3A": "HD-34-MID",
"SOMERVILLE WARD 7": "HD-34-MID",

#Thirty-Fifth Middlesex
"MALDEN WARD 1": "HD-35-MID",
"MALDEN WARD 3 PRECINCT 1A": "HD-35-MID",
"MALDEN WARD 3 PRECINCT 3": "HD-35-MID",
"MALDEN WARD 7 PRECINCT 1": "HD-35-MID",
"MALDEN WARD 7 PRECINCT 3A": "HD-35-MID",
"MEDFORD WARD 1": "HD-35-MID",
"MEDFORD WARD 2": "HD-35-MID",
"MEDFORD WARD 3 PRECINCT 1": "HD-35-MID",
"MEDFORD WARD 6 PRECINCT 2A": "HD-35-MID",
"MEDFORD WARD 7 PRECINCT 2": "HD-35-MID",
"MEDFORD WARD 8 PRECINCT 1": "HD-35-MID",

#Thirty-Sixth Middlesex
"DRACUT": "HD-36-MID",
"TYNGSBOROUGH": "HD-36-MID",

#Thirty-Seventh Middlesex
"ACTON PRECINCT 3": "HD-37-MID",
"ACTON PRECINCT 4": "HD-37-MID",
"ACTON PRECINCT 5": "HD-37-MID",
"ACTON PRECINCT 6A": "HD-37-MID",
"AYER": "HD-37-MID",
"BOXBOROUGH": "HD-37-MID",
"GROTON PRECINCT 1": "HD-37-MID",
"HARVARD": "HD-37-MID",
"SHIRLEY": "HD-37-MID",
# First Norfolk
"QUINCY WARD 3 PRECINCT 3": "HD-01-NOR",
"QUINCY WARD 3 PRECINCT 4": "HD-01-NOR",
"QUINCY WARD 3 PRECINCT 5": "HD-01-NOR",
"QUINCY WARD 4 PRECINCT 1": "HD-01-NOR",
"QUINCY WARD 4 PRECINCT 3": "HD-01-NOR",
"QUINCY WARD 6": "HD-01-NOR",
"RANDOLPH PRECINCT 7": "HD-01-NOR",
"RANDOLPH PRECINCT 8": "HD-01-NOR",
"RANDOLPH PRECINCT 11": "HD-01-NOR",
"RANDOLPH PRECINCT 12": "HD-01-NOR",

# Second Norfolk
"QUINCY WARD 1": "HD-02-NOR",
"QUINCY WARD 3 PRECINCT 1": "HD-02-NOR",
"QUINCY WARD 3 PRECINCT 2": "HD-02-NOR",
"QUINCY WARD 4 PRECINCT 2": "HD-02-NOR",
"QUINCY WARD 4 PRECINCT 4": "HD-02-NOR",
"QUINCY WARD 5 PRECINCT 1": "HD-02-NOR",
"QUINCY WARD 5 PRECINCT 2": "HD-02-NOR",
"QUINCY WARD 5 PRECINCT 3": "HD-02-NOR",
"QUINCY WARD 5 PRECINCT 4": "HD-02-NOR",
"QUINCY WARD 5 PRECINCT 5": "HD-02-NOR",

# Third Norfolk
"HOLBROOK PRECINCT 3": "HD-03-NOR",
"HOLBROOK PRECINCT 4": "HD-03-NOR",
"QUINCY WARD 2": "HD-03-NOR",
"QUINCY WARD 4 PRECINCT 5": "HD-03-NOR",
"QUINCY WARD 5 PRECINCT 1A": "HD-03-NOR",
"WEYMOUTH PRECINCT 5": "HD-03-NOR",
"WEYMOUTH PRECINCT 6": "HD-03-NOR",
"WEYMOUTH PRECINCT 9": "HD-03-NOR",
"WEYMOUTH PRECINCT 12": "HD-03-NOR",
"WEYMOUTH PRECINCT 16": "HD-03-NOR",

# Fourth Norfolk
"WEYMOUTH PRECINCT 1": "HD-04-NOR",
"WEYMOUTH PRECINCT 2": "HD-04-NOR",
"WEYMOUTH PRECINCT 3": "HD-04-NOR",
"WEYMOUTH PRECINCT 4": "HD-04-NOR",
"WEYMOUTH PRECINCT 7": "HD-04-NOR",
"WEYMOUTH PRECINCT 8": "HD-04-NOR",
"WEYMOUTH PRECINCT 9A": "HD-04-NOR",
"WEYMOUTH PRECINCT 10": "HD-04-NOR",
"WEYMOUTH PRECINCT 11": "HD-04-NOR",
"WEYMOUTH PRECINCT 13": "HD-04-NOR",
"WEYMOUTH PRECINCT 14": "HD-04-NOR",
"WEYMOUTH PRECINCT 15": "HD-04-NOR",
"WEYMOUTH PRECINCT 17": "HD-04-NOR",
"WEYMOUTH PRECINCT 18": "HD-04-NOR",

# Fifth Norfolk
"BRAINTREE": "HD-05-NOR",
"HOLBROOK PRECINCT 1": "HD-05-NOR",
"HOLBROOK PRECINCT 2": "HD-05-NOR",

# Sixth Norfolk
"AVON": "HD-06-NOR",
"CANTON": "HD-06-NOR",
"STOUGHTON PRECINCT 1": "HD-06-NOR",
"STOUGHTON PRECINCT 2A": "HD-06-NOR",
"STOUGHTON PRECINCT 4A": "HD-06-NOR",
"STOUGHTON PRECINCT 5": "HD-06-NOR",
"STOUGHTON PRECINCT 7": "HD-06-NOR",
"STOUGHTON PRECINCT 8": "HD-06-NOR",

# Seventh Norfolk
"MILTON PRECINCT 3": "HD-07-NOR",
"MILTON PRECINCT 4": "HD-07-NOR",
"MILTON PRECINCT 5": "HD-07-NOR",
"MILTON PRECINCT 6": "HD-07-NOR",
"MILTON PRECINCT 7": "HD-07-NOR",
"MILTON PRECINCT 8": "HD-07-NOR",
"MILTON PRECINCT 9": "HD-07-NOR",
"MILTON PRECINCT 10": "HD-07-NOR",
"RANDOLPH PRECINCT 1": "HD-07-NOR",
"RANDOLPH PRECINCT 2": "HD-07-NOR",
"RANDOLPH PRECINCT 3": "HD-07-NOR",
"RANDOLPH PRECINCT 4": "HD-07-NOR",
"RANDOLPH PRECINCT 5": "HD-07-NOR",
"RANDOLPH PRECINCT 6": "HD-07-NOR",
"RANDOLPH PRECINCT 9": "HD-07-NOR",
"RANDOLPH PRECINCT 10": "HD-07-NOR",

# Eighth Norfolk
"MANSFIELD PRECINCT 4": "HD-08-NOR",
"MANSFIELD PRECINCT 6A": "HD-08-NOR",
"SHARON": "HD-08-NOR",
"STOUGHTON PRECINCT 2": "HD-08-NOR",
"STOUGHTON PRECINCT 3": "HD-08-NOR",
"STOUGHTON PRECINCT 4": "HD-08-NOR",
"STOUGHTON PRECINCT 5A": "HD-08-NOR",
"STOUGHTON PRECINCT 6": "HD-08-NOR",
"STOUGHTON PRECINCT 7A": "HD-08-NOR",
"STOUGHTON PRECINCT 8A": "HD-08-NOR",
"WALPOLE PRECINCT 2A": "HD-08-NOR",
"WALPOLE PRECINCT 3": "EHD-08-NOR",
"WALPOLE PRECINCT 4": "HD-08-NOR",
"WALPOLE PRECINCT 5A": "HD-08-NOR",

# Ninth Norfolk
"MEDFIELD PRECINCT 3": "HD-09-NOR",
"MEDFIELD PRECINCT 4": "HD-09-NOR",
"MILLIS PRECINCT 1": "HD-09-NOR",
"NORFOLK": "HD-09-NOR",
"PLAINVILLE": "HD-09-NOR",
"WALPOLE PRECINCT 5": "HD-09-NOR",
"WRENTHAM": "HD-09-NOR",

# Tenth Norfolk
"FRANKLIN": "HD-10-NOR",
"MEDWAY PRECINCT 2": "HD-10-NOR",
"MEDWAY PRECINCT 3": "HD-10-NOR",
"MEDWAY PRECINCT 4": "HD-10-NOR",

# Eleventh Norfolk
"DEDHAM": "HD-11-NOR",
"WALPOLE PRECINCT 8": "HD-11-NOR",
"WESTWOOD": "HD-11-NOR",

# Twelfth Norfolk
"NORWOOD": "HD-12-NOR",
"WALPOLE PRECINCT 1": "HD-12-NOR",
"WALPOLE PRECINCT 2": "HD-12-NOR",
"WALPOLE PRECINCT 6": "HD-12-NOR",
"WALPOLE PRECINCT 7": "HD-12-NOR",

# Thirteenth Norfolk
"DOVER": "HD-13-NOR",
"MEDFIELD PRECINCT 1": "HD-13-NOR",
"MEDFIELD PRECINCT 2": "HD-13-NOR",
"NEEDHAM": "HD-13-NOR",

# Fourteenth Norfolk
"LINCOLN PRECINCT 2": "HD-14-NOR",
"WELLESLEY": "HD-14-NOR",
"WESTON": "HD-14-NOR",

# Fifteenth Norfolk
"BROOKLINE PRECINCT 1": "HD-15-NOR",
"BROOKLINE PRECINCT 2": "HD-15-NOR",
"BROOKLINE PRECINCT 3": "HD-15-NOR",
"BROOKLINE PRECINCT 4": "HD-15-NOR",
"BROOKLINE PRECINCT 5A": "HD-15-NOR",
"BROOKLINE PRECINCT 6": "HD-15-NOR",
"BROOKLINE PRECINCT 7": "HD-15-NOR",
"BROOKLINE PRECINCT 8": "HD-15-NOR",
"BROOKLINE PRECINCT 9": "HD-15-NOR",
"BROOKLINE PRECINCT 10": "HD-15-NOR",
"BROOKLINE PRECINCT 11": "HD-15-NOR",
"BROOKLINE PRECINCT 12": "HD-15-NOR",
"BROOKLINE PRECINCT 17": "HD-15-NOR",
# First Plymouth
"PLYMOUTH PRECINCT 4": "HD-01-PLY",
"PLYMOUTH PRECINCT 6": "HD-01-PLY",
"PLYMOUTH PRECINCT 7": "HD-01-PLY",
"PLYMOUTH PRECINCT 8": "HD-01-PLY",
"PLYMOUTH PRECINCT 9": "HD-01-PLY",
"PLYMOUTH PRECINCT 10": "HD-01-PLY",
"PLYMOUTH PRECINCT 11": "HD-01-PLY",
"PLYMOUTH PRECINCT 12": "HD-01-PLY",
"PLYMOUTH PRECINCT 14": "HD-01-PLY",
"PLYMOUTH PRECINCT 15": "HD-01-PLY",
"PLYMOUTH PRECINCT 16": "HD-01-PLY",
"PLYMOUTH PRECINCT 17": "HD-01-PLY",
"PLYMOUTH PRECINCT 18": "HD-01-PLY",

# Second Plymouth
"CARVER": "HD-02-PLY",
"MIDDLEBOROUGH PRECINCT 3": "HD-02-PLY",
"MIDDLEBOROUGH PRECINCT 6": "HD-02-PLY",
"MIDDLEBOROUGH PRECINCT 7A": "HD-02-PLY",
"WAREHAM": "HD-02-PLY",

# Third Plymouth
"COHASSET": "HD-03-PLY",
"HINGHAM": "HD-03-PLY",
"HULL": "HD-03-PLY",

# Fourth Plymouth
"MARSHFIELD PRECINCT 1": "HD-04-PLY",
"MARSHFIELD PRECINCT 2": "HD-04-PLY",
"MARSHFIELD PRECINCT 3": "HD-04-PLY",
"MARSHFIELD PRECINCT 5": "HD-04-PLY",
"MARSHFIELD PRECINCT 6": "HD-04-PLY",
"MARSHFIELD PRECINCT 7": "HD-04-PLY",
"NORWELL PRECINCT 3": "HD-04-PLY",
"SCITUATE": "HD-04-PLY",

# Fifth Plymouth
"HANOVER": "HD-05-PLY",
"HANSON PRECINCT 1": "HD-05-PLY",
"NORWELL PRECINCT 1": "HD-05-PLY",
"NORWELL PRECINCT 2": "HD-05-PLY",
"ROCKLAND": "HD-05-PLY",

# Sixth Plymouth
"DUXBURY": "HD-06-PLY",
"HALIFAX PRECINCT 2": "HD-06-PLY",
"HANSON PRECINCT 2": "HD-06-PLY",
"HANSON PRECINCT 3": "HD-06-PLY",
"MARSHFIELD PRECINCT 2A": "HD-06-PLY",
"MARSHFIELD PRECINCT 4": "HD-06-PLY",
"PEMBROKE PRECINCT 1": "HD-06-PLY",
"PEMBROKE PRECINCT 2": "HD-06-PLY",
"PEMBROKE PRECINCT 3A": "HD-06-PLY",
"PEMBROKE PRECINCT 4": "HD-06-PLY",
"PEMBROKE PRECINCT 5": "HD-06-PLY",

# Seventh Plymouth
"ABINGTON": "HD-07-PLY",
"EAST BRIDGEWATER PRECINCT 1": "HD-07-PLY",
"EAST BRIDGEWATER PRECINCT 2": "HD-07-PLY",
"EAST BRIDGEWATER PRECINCT 3": "HD-07-PLY",
"WHITMAN": "HD-07-PLY",

# Eighth Plymouth
"BRIDGEWATER": "HD-08-PLY",
"RAYNHAM": "HD-08-PLY",

# Ninth Plymouth
"BROCKTON WARD 1 PRECINCT B": "HD-09-PLY",
"BROCKTON WARD 1 PRECINCT C": "HD-09-PLY",
"BROCKTON WARD 1 PRECINCT D": "HD-09-PLY",
"BROCKTON WARD 3 PRECINCT C": "HD-09-PLY",
"BROCKTON WARD 3 PRECINCT D": "HD-09-PLY",
"EAST BRIDGEWATER PRECINCT 4": "HD-09-PLY",
"EASTON PRECINCT 1": "HD-09-PLY",
"EASTON PRECINCT 2": "HD-09-PLY",
"EASTON PRECINCT 3": "HD-09-PLY",
"EASTON PRECINCT 4B": "HD-09-PLY",
"EASTON PRECINCT 7": "HD-09-PLY",
"WEST BRIDGEWATER": "HD-09-PLY",

# Tenth Plymouth
"BROCKTON WARD 4": "HD-10-PLY",
"BROCKTON WARD 5": "HD-10-PLY",
"BROCKTON WARD 6": "HD-10-PLY",

# Eleventh Plymouth
"BROCKTON WARD 1 PRECINCT A": "HD-11-PLY",
"BROCKTON WARD 2": "HD-11-PLY",
"BROCKTON WARD 3 PRECINCT A": "HD-11-PLY",
"BROCKTON WARD 3 PRECINCT B": "HD-11-PLY",
"BROCKTON WARD 7": "HD-11-PLY",

# Twelfth Plymouth
"HALIFAX PRECINCT 1": "HD-12-PLY",
"HALIFAX PRECINCT 2A": "HD-12-PLY",
"KINGSTON": "HD-12-PLY",
"MIDDLEBOROUGH PRECINCT 1": "HD-12-PLY",
"MIDDLEBOROUGH PRECINCT 5A": "HD-12-PLY",
"PEMBROKE PRECINCT 3": "HD-12-PLY",
"PLYMOUTH PRECINCT 1": "HD-12-PLY",
"PLYMOUTH PRECINCT 2": "HD-12-PLY",
"PLYMOUTH PRECINCT 3": "HD-12-PLY",
"PLYMOUTH PRECINCT 5": "HD-12-PLY",
"PLYMOUTH PRECINCT 13": "HD-12-PLY",
"PLYMPTON": "HD-12-PLY",

# First Suffolk
"BOSTON WARD 1 PRECINCT 1": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 2": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 3": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 4": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 5": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 6": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 7": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 8": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 9": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 10": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 11": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 12": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 13": "HD-01-SUF",
"BOSTON WARD 1 PRECINCT 14": "HD-01-SUF",

# Second Suffolk
"BOSTON WARD 2": "HD-02-SUF",
"BOSTON WARD 5 PRECINCT 10": "HD-02-SUF",
"BOSTON WARD 5 PRECINCT 12": "HD-02-SUF",
"BOSTON WARD 21 PRECINCT 1": "HD-02-SUF",
"CAMBRIDGE WARD 1 PRECINCT 1": "HD-02-SUF",
"CAMBRIDGE WARD 1 PRECINCT 2": "HD-02-SUF",
"CAMBRIDGE WARD 2 PRECINCT 3": "HD-02-SUF",
"EVERETT WARD 1 PRECINCT 3": "HD-02-SUF",

# Third Suffolk
"BOSTON WARD 3 PRECINCT 1": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 2": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 3": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 4": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 6": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 8": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 10": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 11": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 12": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 13": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 14": "HD-03-SUF",
"BOSTON WARD 3 PRECINCT 15": "HD-03-SUF",
"BOSTON WARD 4 PRECINCT 1": "HD-03-SUF",
"BOSTON WARD 5 PRECINCT 1": "HD-03-SUF",
"BOSTON WARD 5 PRECINCT 13": "HD-03-SUF",
"BOSTON WARD 5 PRECINCT 14": "HD-03-SUF",

# Fourth Suffolk
"BOSTON WARD 1 PRECINCT 15": "HD-04-SUF",
"BOSTON WARD 6": "HD-04-SUF",
"BOSTON WARD 7 PRECINCT 1": "HD-04-SUF",
"BOSTON WARD 7 PRECINCT 2": "HD-04-SUF",
"BOSTON WARD 7 PRECINCT 3": "HD-04-SUF",
"BOSTON WARD 7 PRECINCT 4": "HD-04-SUF",
"BOSTON WARD 7 PRECINCT 5": "HD-04-SUF",
"BOSTON WARD 7 PRECINCT 6": "HD-04-SUF",
"BOSTON WARD 7 PRECINCT 7": "HD-04-SUF",

# Fifth Suffolk
"BOSTON WARD 7 PRECINCT 10": "HD-05-SUF",
"BOSTON WARD 8 PRECINCT 5": "HD-05-SUF",
"BOSTON WARD 12 PRECINCT 6": "HD-05-SUF",
"BOSTON WARD 12 PRECINCT 7": "HD-05-SUF",
"BOSTON WARD 12 PRECINCT 9": "HD-05-SUF",
"BOSTON WARD 13 PRECINCT 1": "HD-05-SUF",
"BOSTON WARD 13 PRECINCT 2": "HD-05-SUF",
"BOSTON WARD 13 PRECINCT 4": "HD-05-SUF",
"BOSTON WARD 13 PRECINCT 5": "HD-05-SUF",
"BOSTON WARD 14 PRECINCT 1": "HD-05-SUF",
"BOSTON WARD 14 PRECINCT 3": "HD-05-SUF",
"BOSTON WARD 14 PRECINCT 4": "HD-05-SUF",
"BOSTON WARD 15 PRECINCT 1": "HD-05-SUF",
"BOSTON WARD 15 PRECINCT 2": "HD-05-SUF",
"BOSTON WARD 15 PRECINCT 3": "HD-05-SUF",
"BOSTON WARD 15 PRECINCT 4": "HD-05-SUF",
"BOSTON WARD 15 PRECINCT 5": "HD-05-SUF",
"BOSTON WARD 15 PRECINCT 7": "HD-05-SUF",
"BOSTON WARD 15 PRECINCT 9": "HD-05-SUF",

# Sixth Suffolk
"BOSTON WARD 14 PRECINCT 2": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 5": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 6": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 7": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 8": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 9": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 10": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 11": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 12": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 13": "HD-06-SUF",
"BOSTON WARD 14 PRECINCT 14": "HD-06-SUF",
"BOSTON WARD 17 PRECINCT 1": "HD-06-SUF",
"BOSTON WARD 17 PRECINCT 2": "HD-06-SUF",
"BOSTON WARD 17 PRECINCT 3": "HD-06-SUF",
"BOSTON WARD 17 PRECINCT 5": "HD-06-SUF",
"BOSTON WARD 17 PRECINCT 6": "HD-06-SUF",
"BOSTON WARD 17 PRECINCT 7": "HD-06-SUF",
"BOSTON WARD 18 PRECINCT 7": "HD-06-SUF",
"BOSTON WARD 18 PRECINCT 8": "HD-06-SUF",
"BOSTON WARD 19 PRECINCT 12": "HD-06-SUF",

# Seventh Suffolk
"BOSTON WARD 4 PRECINCT 9": "HD-07-SUF",
"BOSTON WARD 4 PRECINCT 10": "HD-07-SUF",
"BOSTON WARD 9 PRECINCT 4": "HD-07-SUF",
"BOSTON WARD 9 PRECINCT 5": "HD-07-SUF",
"BOSTON WARD 9 PRECINCT 7": "HD-07-SUF",
"BOSTON WARD 10 PRECINCT 1": "HD-07-SUF",
"BOSTON WARD 10 PRECINCT 2": "HD-07-SUF",
"BOSTON WARD 10 PRECINCT 3": "HD-07-SUF",
"BOSTON WARD 11 PRECINCT 1": "HD-07-SUF",
"BOSTON WARD 11 PRECINCT 2": "HD-07-SUF",
"BOSTON WARD 11 PRECINCT 3": "HD-07-SUF",
"BOSTON WARD 12 PRECINCT 1": "HD-07-SUF",
"BOSTON WARD 12 PRECINCT 2": "HD-07-SUF",
"BOSTON WARD 12 PRECINCT 3": "HD-07-SUF",
"BOSTON WARD 12 PRECINCT 4": "HD-07-SUF",
"BOSTON WARD 12 PRECINCT 5": "HD-07-SUF",
"BOSTON WARD 12 PRECINCT 8": "HD-07-SUF",

# Eighth Suffolk
"BOSTON WARD 3 PRECINCT 5": "HD-08-SUF",
"BOSTON WARD 3 PRECINCT 9": "HD-08-SUF",
"BOSTON WARD 3 PRECINCT 17": "HD-08-SUF",
"BOSTON WARD 4 PRECINCT 6": "HD-08-SUF",
"BOSTON WARD 4 PRECINCT 7": "HD-08-SUF",
"BOSTON WARD 4 PRECINCT 8": "HD-08-SUF",
"BOSTON WARD 4 PRECINCT 11": "HD-08-SUF",
"BOSTON WARD 4 PRECINCT 12": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 2": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 3": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 4": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 5": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 6": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 7": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 8": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 9": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 11": "HD-08-SUF",
"BOSTON WARD 5 PRECINCT 15": "HD-08-SUF",

# Ninth Suffolk
"BOSTON WARD 3 PRECINCT 7": "HD-09-SUF",
    "BOSTON WARD 3 PRECINCT 16": "HD-09-SUF",
    "BOSTON WARD 4 PRECINCT 2": "HD-09-SUF",
    "BOSTON WARD 4 PRECINCT 3": "HD-09-SUF",
    "BOSTON WARD 4 PRECINCT 4": "HD-09-SUF",
    "BOSTON WARD 7 PRECINCT 8": "HD-09-SUF",
    "BOSTON WARD 7 PRECINCT 9": "HD-09-SUF",
    "BOSTON WARD 8 PRECINCT 1": "HD-09-SUF",
    "BOSTON WARD 8 PRECINCT 2": "HD-09-SUF",
    "BOSTON WARD 8 PRECINCT 3": "HD-09-SUF",
    "BOSTON WARD 8 PRECINCT 4": "HD-09-SUF",
    "BOSTON WARD 8 PRECINCT 6": "HD-09-SUF",
    "BOSTON WARD 9 PRECINCT 1": "HD-09-SUF",
    "BOSTON WARD 9 PRECINCT 2": "HD-09-SUF",
    "BOSTON WARD 9 PRECINCT 3": "HD-09-SUF",
    "BOSTON WARD 9 PRECINCT 6": "HD-09-SUF",
# Tenth Suffolk
"BOSTON WARD 19 PRECINCT 2": "HD-10-SUF",
    "BOSTON WARD 19 PRECINCT 3": "HD-10-SUF",
    "BOSTON WARD 19 PRECINCT 8": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 1": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 2": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 4": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 5": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 6": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 7": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 8": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 9": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 10": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 11": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 12": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 13": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 14": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 15": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 16": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 17": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 18": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 19": "HD-10-SUF",
    "BOSTON WARD 20 PRECINCT 20": "HD-10-SUF",
    "BROOKLINE PRECINCT 16": "HD-10-SUF",

# Eleventh Suffolk
"CHELSEA": "HD-11-SUF",
    "EVERETT WARD 2 PRECINCT 1": "HD-11-SUF",
    "EVERETT WARD 2 PRECINCT 2A": "HD-11-SUF",

# Twelfth Suffolk
"BOSTON WARD 16 PRECINCT 11": "HD-12-SUF",
    "BOSTON WARD 17 PRECINCT 4": "HD-12-SUF",
    "BOSTON WARD 17 PRECINCT 8": "HD-12-SUF",
    "BOSTON WARD 17 PRECINCT 9": "HD-12-SUF",
    "BOSTON WARD 17 PRECINCT 10": "HD-12-SUF",
    "BOSTON WARD 17 PRECINCT 11": "HD-12-SUF",
    "BOSTON WARD 17 PRECINCT 12": "HD-12-SUF",
    "BOSTON WARD 17 PRECINCT 13": "HD-12-SUF",
    "BOSTON WARD 17 PRECINCT 14": "HD-12-SUF",
    "BOSTON WARD 18 PRECINCT 1": "HD-12-SUF",
    "BOSTON WARD 18 PRECINCT 2": "HD-12-SUF",
    "BOSTON WARD 18 PRECINCT 3": "HD-12-SUF",
    "BOSTON WARD 18 PRECINCT 4": "HD-12-SUF",
    "BOSTON WARD 18 PRECINCT 5": "HD-12-SUF",
    "BOSTON WARD 18 PRECINCT 6": "HD-12-SUF",
    "BOSTON WARD 18 PRECINCT 21": "HD-12-SUF",
    "MILTON PRECINCT 1": "HD-12-SUF",
    "MILTON PRECINCT 2": "HD-12-SUF",
    "MILTON PRECINCT 4A": "HD-12-SUF",

# Thirteenth Suffolk
"BOSTON WARD 13 PRECINCT 3": "HD-13-SUF",
    "BOSTON WARD 13 PRECINCT 6": "HD-13-SUF",
    "BOSTON WARD 13 PRECINCT 7": "HD-13-SUF",
    "BOSTON WARD 13 PRECINCT 8": "HD-13-SUF",
    "BOSTON WARD 13 PRECINCT 9": "HD-13-SUF",
    "BOSTON WARD 13 PRECINCT 10": "HD-13-SUF",
    "BOSTON WARD 15 PRECINCT 6": "HD-13-SUF",
    "BOSTON WARD 15 PRECINCT 8": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 1": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 2": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 3": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 4": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 5": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 6": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 7": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 8": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 9": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 10": "HD-13-SUF",
    "BOSTON WARD 16 PRECINCT 12": "HD-13-SUF",

# Fourteenth Suffolk
"BOSTON WARD 18 PRECINCT 9": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 10": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 11": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 12": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 13": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 14": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 15": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 16": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 17": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 18": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 19": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 20": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 22": "Fourteenth Suffolk",
  "BOSTON WARD 18 PRECINCT 23": "Fourteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 10": "Fourteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 11": "Fourteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 13": "Fourteenth Suffolk",
  "BOSTON WARD 20 PRECINCT 3": "Fourteenth Suffolk",
  "BOSTON WARD 20 PRECINCT 21": "Fourteenth Suffolk",

# Fifteenth Suffolk
"BOSTON WARD 10 PRECINCT 4": "Fifteenth Suffolk",
  "BOSTON WARD 10 PRECINCT 5": "Fifteenth Suffolk",
  "BOSTON WARD 10 PRECINCT 6": "Fifteenth Suffolk",
  "BOSTON WARD 10 PRECINCT 7": "Fifteenth Suffolk",
  "BOSTON WARD 10 PRECINCT 8": "Fifteenth Suffolk",
  "BOSTON WARD 10 PRECINCT 9": "Fifteenth Suffolk",
  "BOSTON WARD 11 PRECINCT 4": "Fifteenth Suffolk",
  "BOSTON WARD 11 PRECINCT 5": "Fifteenth Suffolk",
  "BOSTON WARD 11 PRECINCT 6": "Fifteenth Suffolk",
  "BOSTON WARD 11 PRECINCT 7": "Fifteenth Suffolk",
  "BOSTON WARD 11 PRECINCT 8": "Fifteenth Suffolk",
  "BOSTON WARD 11 PRECINCT 9": "Fifteenth Suffolk",
  "BOSTON WARD 11 PRECINCT 10": "Fifteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 1": "Fifteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 4": "Fifteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 5": "Fifteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 6": "Fifteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 7": "Fifteenth Suffolk",
  "BOSTON WARD 19 PRECINCT 9": "Fifteenth Suffolk",

# Sixteenth Suffolk
"REVERE WARD 1 PRECINCT 3": "Sixteenth Suffolk",
  "REVERE WARD 2 PRECINCT 3": "Sixteenth Suffolk",
  "REVERE WARD 3": "Sixteenth Suffolk",
  "REVERE WARD 4": "Sixteenth Suffolk",
  "REVERE WARD 6": "Sixteenth Suffolk",
  "SAUGUS PRECINCT 3": "Sixteenth Suffolk",
  "SAUGUS PRECINCT 10": "Sixteenth Suffolk",

# Seventeenth Suffolk
"BOSTON WARD 21 PRECINCT 3": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 5": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 6": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 7": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 8": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 9": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 10": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 11": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 12": "Seventeenth Suffolk",
  "BOSTON WARD 21 PRECINCT 15": "Seventeenth Suffolk",
  "BOSTON WARD 22 PRECINCT 2": "Seventeenth Suffolk",
  "BOSTON WARD 22 PRECINCT 3": "Seventeenth Suffolk",
  "BOSTON WARD 22 PRECINCT 6": "Seventeenth Suffolk",
  "BOSTON WARD 22 PRECINCT 9": "Seventeenth Suffolk",
  "BOSTON WARD 22 PRECINCT 10": "Seventeenth Suffolk",
  "BROOKLINE PRECINCT 13": "Seventeenth Suffolk",
  "BROOKLINE PRECINCT 14A": "Seventeenth Suffolk",

# Eighteenth Suffolk
"BOSTON WARD 21 PRECINCT 2": "Eighteenth Suffolk",
  "BOSTON WARD 21 PRECINCT 4": "Eighteenth Suffolk",
  "BOSTON WARD 21 PRECINCT 13": "Eighteenth Suffolk",
  "BOSTON WARD 21 PRECINCT 14": "Eighteenth Suffolk",
  "BOSTON WARD 21 PRECINCT 16": "Eighteenth Suffolk",
  "BOSTON WARD 22 PRECINCT 1": "Eighteenth Suffolk",
  "BOSTON WARD 22 PRECINCT 4": "Eighteenth Suffolk",
  "BOSTON WARD 22 PRECINCT 5": "Eighteenth Suffolk",
  "BOSTON WARD 22 PRECINCT 7": "Eighteenth Suffolk",
  "BOSTON WARD 22 PRECINCT 8": "Eighteenth Suffolk",
  "BOSTON WARD 22 PRECINCT 11": "Eighteenth Suffolk",
  "BOSTON WARD 22 PRECINCT 12": "Eighteenth Suffolk",
  "BOSTON WARD 22 PRECINCT 13": "Eighteenth Suffolk",
  "CAMBRIDGE WARD 1 PRECINCT 2A": "Eighteenth Suffolk",
  "CAMBRIDGE WARD 5 PRECINCT 2": "Eighteenth Suffolk",

# Nineteenth Suffolk
"REVERE WARD 1 PRECINCT 1": "Nineteenth Suffolk",
  "REVERE WARD 1 PRECINCT 2": "Nineteenth Suffolk",
  "REVERE WARD 2 PRECINCT 1": "Nineteenth Suffolk",
  "REVERE WARD 2 PRECINCT 2": "Nineteenth Suffolk",
  "REVERE WARD 2 PRECINCT 3A": "Nineteenth Suffolk",
  "REVERE WARD 5": "Nineteenth Suffolk",
  "WINTHROP": "Nineteenth Suffolk",
# First Worcester
"HOLDEN": "HD-01-WOR",
"PAXTON": "HD-01-WOR",
"PRINCETON": "HD-01-WOR",
"RUTLAND": "HD-01-WOR",
"WESTMINSTER": "HD-01-WOR",

# Second Worcester
"ASHBURNHAM": "HD-02-WOR",
"GARDNER": "HD-02-WOR",
"TEMPLETON": "HD-02-WOR",
"WINCHENDON PRECINCT 2": "HD-02-WOR",
"WINCHENDON PRECINCT 3": "HD-02-WOR",

# Third Worcester
"FITCHBURG": "HD-03-WOR",
"LUNENBURG PRECINCT B": "HD-03-WOR",
"LUNENBURG PRECINCT C1": "HD-03-WOR",

# Fourth Worcester
"LEOMINSTER": "HD-04-WOR",

# Fifth Worcester
"BARRE": "HD-05-WOR",
"BROOKFIELD": "HD-05-WOR",
"EAST BROOKFIELD": "HD-05-WOR",
"HARDWICK": "HD-05-WOR",
"HUBBARDSTON": "HD-05-WOR",
"LEICESTER PRECINCT 1": "HD-05-WOR",
"NEW BRAINTREE": "HD-05-WOR",
"NORTH BROOKFIELD": "HD-05-WOR",
"OAKHAM": "HD-05-WOR",
"SPENCER PRECINCT 2": "HD-05-WOR",
"SPENCER PRECINCT 3": "HD-05-WOR",
"SPENCER PRECINCT 4": "HD-05-WOR",
"WARE PRECINCT A": "HD-05-WOR",
"WEST BROOKFIELD": "HD-05-WOR",

# Sixth Worcester
"CHARLTON PRECINCT 1": "HD-06-WOR",
"CHARLTON PRECINCT 2": "HD-06-WOR",
"CHARLTON PRECINCT 3": "HD-06-WOR",
"CHARLTON PRECINCT 4A": "HD-06-WOR",
"DUDLEY": "HD-06-WOR",
"SOUTHBRIDGE": "HD-06-WOR",
"SPENCER PRECINCT 1": "HD-06-WOR",

# Seventh Worcester
"AUBURN": "HD-07-WOR",
"CHARLTON PRECINCT 4": "HD-07-WOR",
"LEICESTER PRECINCT 3": "HD-07-WOR",
"MILLBURY": "HD-07-WOR",
"OXFORD PRECINCT 2": "HD-07-WOR",
"OXFORD PRECINCT 3": "HD-07-WOR",
"OXFORD PRECINCT 4A": "HD-07-WOR",

# Eighth Worcester
"BELLINGHAM": "HD-08-WOR",
"BLACKSTONE": "HD-08-WOR",
"MEDWAY PRECINCT 1": "HD-08-WOR",
"MILLVILLE": "HD-08-WOR",
"UXBRIDGE PRECINCT 1A": "HD-08-WOR",
"UXBRIDGE PRECINCT 2": "HD-08-WOR",
"UXBRIDGE PRECINCT 3": "HD-08-WOR",
"UXBRIDGE PRECINCT 4": "HD-08-WOR",

# Ninth Worcester
"GRAFTON": "HD-09-WOR",
"NORTHBRIDGE": "HD-09-WOR",
"UPTON": "HD-09-WOR",

# Tenth Worcester
"HOPEDALE": "HD-10-WOR",
"MENDON": "HD-10-WOR",
"MILFORD": "HD-10-WOR",

# Eleventh Worcester
"SHREWSBURY": "HD-11-WOR",
"WESTBOROUGH PRECINCT 4": "HD-11-WOR",

# Twelfth Worcester
"BERLIN": "HD-12-WOR",
"BOYLSTON": "HD-12-WOR",
"CLINTON": "HD-12-WOR",
"LANCASTER": "HD-12-WOR",
"NORTHBOROUGH PRECINCT 4": "HD-12-WOR",
"STERLING": "HD-12-WOR",

# Thirteenth Worcester
"WORCESTER WARD 1 PRECINCT 1": "HD-13-WOR",
"WORCESTER WARD 1 PRECINCT 2": "HD-13-WOR",
"WORCESTER WARD 1 PRECINCT 3": "HD-13-WOR",
"WORCESTER WARD 1 PRECINCT 4": "HD-13-WOR",
"WORCESTER WARD 1 PRECINCT 6": "HD-13-WOR",
"WORCESTER WARD 3 PRECINCT 2": "HD-13-WOR",
"WORCESTER WARD 9": "HD-13-WOR",
"WORCESTER WARD 10 PRECINCT 1": "HD-13-WOR",

# Fourteenth Worcester
"WEST BOYLSTON": "HD-14-WOR",
"WORCESTER WARD 1 PRECINCT 5": "HD-14-WOR",
"WORCESTER WARD 2": "HD-14-WOR",
"WORCESTER WARD 3 PRECINCT 3": "HD-14-WOR",
"WORCESTER WARD 3 PRECINCT 3A": "HD-14-WOR",
"WORCESTER WARD 3 PRECINCT 5": "HD-14-WOR",
"WORCESTER WARD 3 PRECINCT 5A": "HD-14-WOR",
"WORCESTER WARD 3 PRECINCT 6": "HD-14-WOR",

# Fifteenth Worcester
"WORCESTER WARD 3 PRECINCT 1": "HD-15-WOR",
"WORCESTER WARD 3 PRECINCT 4": "HD-15-WOR",
"WORCESTER WARD 4": "HD-15-WOR",
"WORCESTER WARD 6 PRECINCT 1": "HD-15-WOR",
"WORCESTER WARD 10 PRECINCT 2": "HD-15-WOR",
"WORCESTER WARD 10 PRECINCT 3": "HD-15-WOR",
"WORCESTER WARD 10 PRECINCT 4": "HD-15-WOR",
"WORCESTER WARD 10 PRECINCT 4A": "HD-15-WOR",
"WORCESTER WARD 10 PRECINCT 5": "HD-15-WOR",

# Sixteenth Worcester
"WORCESTER WARD 5": "HD-16-WOR",
"WORCESTER WARD 6 PRECINCT 2": "HD-16-WOR",
"WORCESTER WARD 6 PRECINCT 3": "HD-16-WOR",
"WORCESTER WARD 6 PRECINCT 4": "HD-16-WOR",
"WORCESTER WARD 6 PRECINCT 5": "HD-16-WOR",
"WORCESTER WARD 6 PRECINCT 6": "HD-16-WOR",
"WORCESTER WARD 8 PRECINCT 1": "HD-16-WOR",
"WORCESTER WARD 8 PRECINCT 5": "HD-16-WOR",

# Seventeenth Worcester
"LEICESTER PRECINCT 2": "HD-17-WOR",
"LEICESTER PRECINCT 4": "HD-17-WOR",
"WORCESTER WARD 7": "HD-17-WOR",
"WORCESTER WARD 8 PRECINCT 2": "HD-17-WOR",
"WORCESTER WARD 8 PRECINCT 3": "HD-17-WOR",
"WORCESTER WARD 8 PRECINCT 4": "HD-17-WOR",
"WORCESTER WARD 8 PRECINCT 6": "HD-17-WOR",
"WORCESTER WARD 10 PRECINCT 6": "HD-17-WOR",

# Eighteenth Worcester
"DOUGLAS": "HD-18-WOR",
"OXFORD PRECINCT 1": "HD-18-WOR",
"OXFORD PRECINCT 4": "HD-18-WOR",
"SUTTON": "HD-18-WOR",
"UXBRIDGE PRECINCT 1": "HD-18-WOR",
"WEBSTER": "HD-18-WOR",

# Nineteenth Worcester
"FRAMINGHAM PRECINCT 21A": "HD-19-WOR",
"NORTHBOROUGH PRECINCT 1": "HD-19-WOR",
"NORTHBOROUGH PRECINCT 2": "HD-19-WOR",
"NORTHBOROUGH PRECINCT 3": "HD-19-WOR",
"SOUTHBOROUGH": "HD-19-WOR",
"WESTBOROUGH PRECINCT 1": "HD-19-WOR",
"WESTBOROUGH PRECINCT 2": "HD-19-WOR",
"WESTBOROUGH PRECINCT 3": "HD-19-WOR",
"WESTBOROUGH PRECINCT 5": "HD-19-WOR",
"WESTBOROUGH PRECINCT 6": "HD-19-WOR"


}

#Assign the district based on city and state
def assign_district(row):
    if row['state'] == 'Unassigned':
        return 'Unknown'

    if row['state'] == 'MA' and row['city'] in district_mapping:
        return district_mapping.get(row['city'], 'Unknown')

    return 'Other state'


def assign_senate_district(row):
    if row['state'] == 'Unassigned':
        return 'Unknown'
    if row['state'] == 'MA' and row['city'] in senate_mapping:
        return senate_mapping.get(row['city'], 'Unknown')
    return 'Other state'


def assign_house_district(row):
    if row['state'] == 'Unassigned':
        return 'Unknown'
    if row['state'] == 'MA' and row['city'] in house_mapping:
        return house_mapping.get(row['city'], 'Unknown')
    return 'Other state'

#print the progression so we our laptop doesnt crash due to data overloads
try:
    project_root = find_project()
    print(f"Found project root: {project_root}")

    input_path = project_root / "data" / "combined_spending.csv"
    output_path = project_root / "data" / "updated_spending_with_districts.csv"

    print(f"Reading data from: {input_path}")
    df = pd.read_csv(input_path, low_memory=False)
    total_rows = len(df)
    print(f"Processing {total_rows} rows of data...")

    print("Assigning Congressional Districts...")
    df['Congressional_District'] = [assign_district(row) for row in tqdm(df.to_dict('records'), total=total_rows)]

    print("Assigning Senate Districts...")
    df['Senate_District'] = [assign_senate_district(row) for row in tqdm(df.to_dict('records'), total=total_rows)]

    print("Assigning House Districts...")
    df['House_District'] = [assign_house_district(row) for row in tqdm(df.to_dict('records'), total=total_rows)]

    print(f"Saving updated file to {output_path}...")
    df.to_csv(output_path, index=False)
    print("Process complete!")

    print("\nFirst 5 rows:")
    print(df.head())
    print("\nLast 5 rows:")
    print(df.tail())

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Current directory is:", Path.cwd())
    print("Please check the project structure or provide the full path to the CSV file.")