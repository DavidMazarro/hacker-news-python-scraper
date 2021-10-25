from src.entry import Entry

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
    # All sortings that are not by title must be reversed
    # when passed to the sorted function, since sorted returns
    # the elements from lowest to greatest, and we want the opposite
    if field_name != 'title':
        reverse = not reverse
    return sorted(
        entries,
        # If the some optional field (points or comments_num) has a value of None,
        # the key function returns -1 to have them at the
        # end of the sorting (e.g. None points being less than 0 points)
        key=lambda entry: -1
        if getattr(entry, field_name) == None
        else getattr(entry, field_name),
        reverse=reverse,
    )

# Entries with more than five words in the title ordered by the number of comments first
def entries_gr5_comment_num(entries: list[Entry]) -> list[Entry]:
    return sort_entries_by_field(
        list(filter(lambda entry: len(entry.title.split()) > 5, entries)),
        'comments_num'
    )

# Entries with less than or equal to five words in the title ordered by points
def entries_leq5_points(entries: list[Entry]) -> list[Entry]:
    return sort_entries_by_field(
        list(filter(lambda entry: len(entry.title.split()) <= 5, entries)),
        'points'
    )
