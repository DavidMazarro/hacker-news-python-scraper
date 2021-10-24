from typing import Optional

# Note that entries in Hacker News are not required
# to have comments or points, so the fields can be empty
class Entry:
    def __init__(
        self,
        title: str,
        order: int,
        comments_num: Optional[int] = None,
        points: Optional[int] = None,
    ) -> None:
        self.title = title
        self.order = order
        self.comments_num = comments_num
        self.points = points

    def __str__(self) -> str:
        entry_str: str = f"{self.order}. {self.title}"
        if self.comments_num:
            entry_str += f", {self.comments_num} comments"
        if self.points:
            entry_str += f", {self.points} points"
        return entry_str
