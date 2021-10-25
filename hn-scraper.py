from src.scraper import scrape
from src.entry import Entry
from src.entry_funcs import sort_entries_by_field, entries_gr5_comment_num, entries_leq5_points

entries: list[Entry] = scrape("https://news.ycombinator.com/")

entries1 = entries_gr5_comment_num(entries)
entries2 = entries_leq5_points(entries)

print("-- Entries with more than 5 words in title, sorted by num. of comments--\n")
for entry in entries1:
    print(entry)
print('\n')
print("-- Entries with less than 5 words or equal in title, sorted by points--\n")
for entry in entries2:
    print(entry)
