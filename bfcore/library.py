import requests
import urllib
import xml.etree.ElementTree as ET
from fuzzywuzzy import fuzz

# Exposed location map for clients (standalone + Django app)
LOCATION_MAP = {
    "3": "MAIN",
    "4": "ANZA BRANCH",
    "5": "BAYVIEW BRANCH", 
    "6": "BERNAL HEIGHTS BRANCH",
    "8": "CHINATOWN BRANCH",
    "9": "EUREKA VALLEY BRANCH",
    "10": "EXCELSIOR BRANCH",
    "11": "GLEN PARK BRANCH",
    "12": "GOLDEN GATE VALLEY BRANCH",
    "13": "INGLESIDE BRANCH",
    "14": "CHILDREN'S BOOKMOBILE",
    "15": "MARINA BRANCH",
    "16": "MERCED BRANCH",
    "17": "MISSION BRANCH",
    "18": "MISSION BAY BRANCH",
    "19": "NOE VALLEY BRANCH",
    "20": "NORTH BEACH BRANCH",
    "21": "OCEAN VIEW BRANCH",
    "22": "ORTEGA BRANCH",
    "23": "PARK BRANCH",
    "24": "PARKSIDE BRANCH",
    "25": "PORTOLA BRANCH",
    "26": "POTRERO BRANCH",
    "27": "PRESIDIO BRANCH",
    "28": "RICHMOND BRANCH",
    "29": "SUNSET BRANCH",
    "30": "VISITACION VALLEY BRANCH",
    "31": "WEST PORTAL BRANCH",
    "34": "WESTERN ADDITION BRANCH",
}


def create_library_url(book_title, author, lib_location="3"):
    branch_name = LOCATION_MAP.get(lib_location, "MAIN")
    query = f'title:({book_title}) AND contributor:({author}) AND format:(bk) AND avlocation:"{branch_name}"'
    encoded_query = urllib.parse.quote(query)
    base_url = "https://gateway.bibliocommons.com/v2/libraries/sfpl/rss/search"
    full_url = f"{base_url}?query={encoded_query}&searchType=bl"
    print(f"Library URL: {full_url}")
    return full_url


def extract_details(book_title, author, content):
    # The content is now XML from RSS feed, not HTML
    from xml.etree.ElementTree import ParseError
    try:
        root = ET.fromstring(content)
        items = root.findall('.//item')
        if not items:
            print("No items found in RSS feed")
            return None
        biblio_info = []
        for item in items:
            title_elem = item.find('title')
            creator_elem = item.find('.//{http://purl.org/dc/elements/1.1/}creator')
            if title_elem is not None and creator_elem is not None:
                title = title_elem.text.strip() if title_elem.text else ""
                creator = creator_elem.text.strip() if creator_elem.text else ""
                if title and creator:
                    biblio_info.append((title, creator))
        if not biblio_info:
            print("No valid book info found in RSS items")
            return None
        scored_info = []
        for info in biblio_info:
            title_score = fuzz.token_set_ratio(info[0], book_title)
            author_score = fuzz.token_set_ratio(info[1], author)
            total_score = title_score + author_score
            scored_info.append((total_score, info))
        if scored_info:
            scored_info.sort(reverse=True)
            best_match = scored_info[0][1]
            print(f"Best match: {best_match} (score: {scored_info[0][0]})")
            return best_match
        return None
    except ParseError as e:
        print(f"XML parsing error: {e}")
        return None
    except Exception as e:
        print(f"Error extracting details from RSS: {e}")
        return None


def get_library_details(book, author, library):
    url = create_library_url(book, author, library)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if not response.content:
            print(f"Empty response from library URL: {url}")
            return None
        details = extract_details(book, author, response.content)
        return details
    except requests.RequestException as e:
        print(f"Error fetching library details for '{book}' by '{author}': {e}")
        return None
    except Exception as e:
        print(f"Error parsing library response for '{book}' by '{author}': {e}")
        return None
