import requests
import urllib
import xml.etree.ElementTree as ET
from fuzzywuzzy import fuzz
# LIBRARY SEARCHING
# to retrieve the SFPL site url for any book using the new BiblioCommons API
def create_library_url(book_title, author, lib_location="3"):
    """
    Create a BiblioCommons RSS search URL for SFPL
    lib_location mapping to branch names needs to be updated
    """
    
    # Map location codes to exact branch names as used by the new API
    location_map = {
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
    
    branch_name = location_map.get(lib_location, "MAIN")
    
    # Create the search query in the new format
    # Format: title:(Book Title) AND contributor:(Author Name) AND format:(bk) AND avlocation:"BRANCH NAME"
    query = f'title:({book_title}) AND contributor:({author}) AND format:(bk) AND avlocation:"{branch_name}"'
    
    # URL encode the query
    encoded_query = urllib.parse.quote(query)
    
    # Create the full URL
    base_url = "https://gateway.bibliocommons.com/v2/libraries/sfpl/rss/search"
    full_url = f"{base_url}?query={encoded_query}&searchType=bl"
    
    print(f"Library URL: {full_url}")
    return full_url

def extract_details(book_title, author, content):
    """
    Main function to extract details from library response
    Now uses RSS XML parsing instead of HTML parsing
    """
    # The content is now XML from RSS feed, not HTML
    """
    Extract book details from BiblioCommons RSS XML response
    """
    from xml.etree.ElementTree import ParseError
    
    try:
        # Parse the XML
        root = ET.fromstring(content)
        
        # Find all items in the RSS feed
        items = root.findall('.//item')
        
        if not items:
            print("No items found in RSS feed")
            return None
        
        # Extract book information from items
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
        
        # Use fuzzy matching to find the best match
        scored_info = []
        for info in biblio_info:
            title_score = fuzz.token_set_ratio(info[0], book_title)
            author_score = fuzz.token_set_ratio(info[1], author)
            total_score = title_score + author_score
            scored_info.append((total_score, info))
        
        if scored_info:
            scored_info.sort(reverse=True)  # Sort descending by score
            best_match = scored_info[0][1]  # Get the best match
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
    url = create_library_url(book, author, library)  # Now passes both book and author
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
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
