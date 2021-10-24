from typing import Optional

class Entry():
    title: str
    order: int
    comments_num: Optional[int]
    points: Optional[int]
    
    def __init__(
            self,
            title: str,
            order: int,
            comments_num: Optional[int] = None,
            points: Optional[int] = None,
    ) -> None: ...
