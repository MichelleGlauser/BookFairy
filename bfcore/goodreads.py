import requests
from pyquery import PyQuery as pq
from thefuzz import fuzz
from . import debug_log

# GOODREADS SEARCHING
# to retrieve the Goodreads site url for any book
def get_gr_search_url(title, author):
    base_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q="
    return f"{base_url}{title} {author}&search_type=books"

user_agent = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}


def find_gr_rating(title, author):
    """Return the best Goodreads rating (float) for a title/author, or None if not found."""
    try:
        gr_url = get_gr_search_url(title, author)
        response = requests.get(gr_url, headers=user_agent, timeout=6.1)
        pq_data = pq(response.content)
        books = pq_data("tr[itemtype='http://schema.org/Book']")
        all_info = books.children("td").eq(1)

        biblio_info = []
        for row in all_info.items():
            title_el = row.find("a.bookTitle")
            author_el = row.find("a.authorName")
            rating_el = row.find("span.minirating")
            if len(title_el) == 0 or len(author_el) == 0 or len(rating_el) == 0:
                continue
            title_txt = title_el.text().strip()
            author_txt = author_el.text().strip()
            try:
                rating_val = float(rating_el.text().strip().partition(" ")[0])
            except Exception:
                continue
            if title_txt and author_txt:
                biblio_info.append((title_txt, author_txt, rating_val))
        if not biblio_info:
            return None

        def score(info):
            # Favor near-exact title matches; avoid subset 100s
            title_score = fuzz.token_sort_ratio(info[0], title)
            author_score = fuzz.token_sort_ratio(info[1], author)
            weighted = title_score * 1.2 + author_score
            length_penalty = abs(len(info[0]) - len(title)) * 0.2
            return weighted - length_penalty

        return max(biblio_info, key=score)[2]
    except Exception as e:
        debug_log(f"Error fetching Goodreads rating: {e}")
        return None
