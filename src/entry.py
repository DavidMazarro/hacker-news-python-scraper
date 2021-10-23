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
    ):
        self.title = title
        self.order = order
        self.comments_num = comments_num
        self.points = points

    def puntos(self):
        print(self.points)
