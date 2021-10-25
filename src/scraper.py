import requests
from entry import Entry
from typing import Optional
from bs4 import BeautifulSoup # type: ignore
from bs4.element import Tag # type: ignore

# This function recieves the URL to whatever Hacker News'
# current homepage is, and returns a list of the first
# 30 entries with title, rank, number of comments and points
def scrape(URL: str) -> list[Entry]:
    frontpage = requests.get(URL)

    if frontpage.status_code != 200:
        raise Exception(f"The response status code ({frontpage.status_code}) was not 200 OK")
    
    soup = BeautifulSoup(frontpage.content, "html.parser")

    tag_entries = soup.find_all("table", class_="itemlist")[0]
    entries: list[Entry] = []
    
    for n in range(1, len(tag_entries) - 3, 5):
        entries.append(Entry(
            get_title(tag_entries.contents[n]),
            get_rank(tag_entries.contents[n]),
            get_comments_num(tag_entries.contents[n+1]),
            get_points(tag_entries.contents[n+1])
        ))
    return entries

def get_title(tag_entry: Tag) -> str:
    # Gets the title from the tag as a string
    return str(tag_entry.contents[4].contents[0].contents[0])

def get_rank(tag_entry: Tag) -> int:
    # Gets the rank from the tag as a string
    rank_str = str(tag_entry.contents[1].contents[0].contents[0])
    # Since the string contains a dot at the end (e.g. "16."),
    # it gets trimmed by getting the string minus the last character
    # and then converted into a int
    return int(rank_str[0:-1])

def get_comments_num(tag_entry: Tag) -> Optional[int]:
    try:
        # Gets the num. of comments from the tag as a string
        comments_num_str = str(tag_entry.contents[1].contents[11].contents[0])
    except:
        return None
    # If the comments_str doesn't end in 'comments' or ' comment' after
    # accessing its contents, it means the tag for this entry didn't
    # have a value for comments, so None is returned
    if comments_num_str[-8:] != 'comments' and comments_num_str[-8:] != ' comment':
        return None
    # If the last letter of the string is 's', it means
    # the word ends in "comments" and we have to trim the last 7
    # characters before turning our num. of comments string into an int
    if comments_num_str[-1] != 's':
        return int(comments_num_str[0:-9])
    else:
        # This value should be 1 since the last word is
        # "comment", but just in case it isn't, this is not going
        # to return 1 because it would be a made up value and
        # not the scraped contents of the actual headline
        return int(comments_num_str[0:-8])
    pass

def get_points(tag_entry: Tag) -> Optional[int]:
    try:
        # Gets the points from the tag as a string
        points_str = str(tag_entry.contents[1].contents[1].contents[0])
    except:
        return None
    # If the points_str doesn't end in 'points' or ' point' after
    # accessing its contents, it means the tag for this entry didn't
    # have a value for points, so None is returned
    if points_str[-6:] != 'points' and points_str[-6:] != ' point':
        return None
    # If the last letter of the string is 's', it means
    # the word ends in "points" and we have to trim the last 7
    # characters before turning our points string into an int
    if points_str[-1] != 's':
        return int(points_str[0:-7])
    else:
        # This value should be 1 since the last word is
        # "point", but just in case it isn't, this is not going
        # to return 1 because it would be a made up value and
        # not the scraped contents of the actual headline
        return int(points_str[0:-6])

# This function recieves a list of scraped entries
# and a string meant to represent one of the possible fields
# of an Entry object, and returns a list with the same entries but sorted
# by a particular field; the behavior the function for each field is as follows:
# "title": Sorts the entries alphabetically
# "rank": Sorts the entries by descending rank, instead of ascending
#          like returned by the scrape function
# "comments_num": Sorts the entries from biggest to smallest number of comments
# "points": Sorts the entries from biggest to smallest number of points
# The reverse argument is an optional one which returns the opposite sorting
# (smallest to biggest, etc.)
def sort_entries_by_field(entries: list[Entry], field_name: str, reverse: bool = False) -> list[Entry]:
    pass
