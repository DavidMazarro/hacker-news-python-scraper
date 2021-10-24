import src.entry as entry
import src.scraper as scraper

URL = "https://news.ycombinator.com/"
entries = scraper.scrape(URL)

def test_number_scraped_entries_is_30():
    assert len(entries) == 30

def test_entries_sorted_by_title_idempotency():
    sorted_by_title = scraper.sort_entries_by_field(entries, 'title')
    assert scraper.sort_entries_by_field(sorted_by_title, 'title') == sorted_by_title

def test_entries_sorted_by_comments_num_idempotency():
    sorted_by_comments_num = scraper.sort_entries_by_field(entries, 'comments_num')
    assert scraper.sort_entries_by_field(sorted_by_comments_num, 'comments_num') == sorted_by_comments_num

def test_entries_sorted_by_points_idempotency():
    sorted_by_points = scraper.sort_entries_by_field(entries, 'points')
    assert scraper.sort_entries_by_field(sorted_by_points, 'points') == sorted_by_points
    
def test_entries_sorted_by_order_identity():
    assert scraper.sort_entries_by_field(entries, 'title', True) == entries

def test_entries_sorted_by_order_involution():
    assert scraper.sort_entries_by_field(
        scraper.sort_entries_by_field(entries, 'title'),
        'title'
    ) == entries
