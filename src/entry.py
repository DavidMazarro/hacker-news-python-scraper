from typing import Optional

# Note that entries in Hacker News are not required
# to have comments or points, so the fields can be empty,
# hence the Optional type for comments_num and points
class Entry:
    def __init__(
        self,
        title: str,
        rank: int,
        comments_num: Optional[int] = None,
        points: Optional[int] = None,
    ) -> None:
        self.title = title
        self.rank = rank
        self.comments_num = comments_num
        self.points = points

    def __str__(self) -> str:
        entry_str: str = f"{self.rank}. {self.title}"
        if self.comments_num:
            entry_str += f", {self.comments_num} comments"
        if self.points:
            entry_str += f", {self.points} points"
        return entry_str
