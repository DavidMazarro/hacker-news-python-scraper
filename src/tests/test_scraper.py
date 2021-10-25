import src.entry as entry
import src.scraper as scraper
import src.entry_funcs as entry_funcs

URL = "https://news.ycombinator.com/"
entries = scraper.scrape(URL)

def test_number_scraped_entries_is_30():
    assert len(entries) == 30

def test_entries_sorted_by_title_idempotency():
    sorted_by_title = entry_funcs.sort_entries_by_field(entries, 'title')
    assert entry_funcs.sort_entries_by_field(sorted_by_title, 'title') == sorted_by_title

def test_entries_sorted_by_comments_num_idempotency():
    sorted_by_comments_num = entry_funcs.sort_entries_by_field(entries, 'comments_num')
    assert entry_funcs.sort_entries_by_field(sorted_by_comments_num, 'comments_num') == sorted_by_comments_num

def test_entries_sorted_by_points_idempotency():
    sorted_by_points = entry_funcs.sort_entries_by_field(entries, 'points')
    assert entry_funcs.sort_entries_by_field(sorted_by_points, 'points') == sorted_by_points
    
def test_entries_sorted_by_rank_identity():
    assert entry_funcs.sort_entries_by_field(entries, 'rank', True) == entries

def test_entries_sorted_by_rank_involution():
    assert entry_funcs.sort_entries_by_field(
        entry_funcs.sort_entries_by_field(entries, 'rank'),
        'rank',
        reverse=True
    ) == entries

def test_entries_filtered_added_length_is_30():
    entries1 = entry_funcs.entries_gr5_comment_num(entries)
    entries2 = entry_funcs.entries_leq5_points(entries)
    assert len(entries1 + entries2) == 30
