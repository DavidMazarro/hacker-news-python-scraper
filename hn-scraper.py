from src.scraper import scrape, sort_entries_by_field, entries_gr5_comment_num, entries_leq5_points
from src.entry import Entry

entries: list[Entry] = scrape("https://news.ycombinator.com/")
entries1 = entries_gr5_comment_num(entries)
entries2 = entries_leq5_points(entries)

for entry in entries1:
    print(entry)
print('\n')
for entry in entries2:
    print(entry)
