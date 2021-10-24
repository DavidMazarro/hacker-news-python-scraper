import requests
from entry import Entry
from typing import Optional
from bs4 import BeautifulSoup # type: ignore

# This function recieves the URL to whatever Hacker News'
# current homepage is, and returns a list of the first
# 30 entries with title, order, number of comments and points
def scrape(URL: str) -> list[Entry]:
    pass

# This function recieves a list of scraped entries
# and a string meant to represent one of the possible fields
# of an Entry object, and returns a list with the same entries but sorted
# by a particular field; the behavior the function for each field is as follows:
# "title": Sorts the entries alphabetically
# "order": Sorts the entries by descending order, instead of ascending
#          like returned by the scrape function
# "comments_num": Sorts the entries from biggest to smallest number of comments
# "points": Sorts the entries from biggest to smallest number of points
# The reverse argument is an optional one which returns the opposite sorting
# (smallest to biggest, etc.)
def sort_entries_by_field(entries: list[Entry], field_name: str, reverse: bool = False) -> list[Entry]:
    pass
