![GitHub Actions badge](https://github.com/DavidMazarro/hacker-news-python-scraper/actions/workflows/python-testing.yml/badge.svg)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
# Hacker News scraper (in Python)
This is just a basic scraper that takes the first 30 entries from the [Hacker News frontpage](https://news.ycombinator.com/), makes an object model of the entries content
and performs a couple of operations (sorting entries by title, rank, num. of comments or points and filtering by num. of words in the title)
over them. The program is intended for a take-home assignment as part of an interview process, but can be extended in a relatively easy way.

## Installation

You need to have [Python **3.9**](https://www.python.org/) installed for this program to work (previous versions won't work without some tweaks; see [Observations](#observations)). 
You also need to clone this repository:
```console
git clone https://github.com/DavidMazarro/hacker-news-python-scraper.git
```

After that run the following command:
```console
pip install --upgrade pip
```
to upgrade pip, and then run this from within the project root folder:
```console
pip install -r requirements.txt
```
to install the dependencies for the program.

The program is tested using [pytest](https://pytest.org/) and type-checked using type annotations
and [mypy](http://mypy-lang.org/) with every new commit that is
pushed to the repository. In case you want to perform the type-checking yourself, run:
```console
pip install pytest mypy types-requests
```
to install mypy and pytest, and then within the project folder you can run:
```console
mypy .
```
to type-check the project and:
```console
pytest
```
to run the [unit tests](./src/tests/).


## Running
The project includes the [hn-scraper.py](./hn-scraper.py) script, intended to show the scraper working.
From within the project root folder, run the following command:
```console
python ./hn-scraper.py
```
and you will get an output similar to this:
```console
-- Entries with more than 5 words in title, sorted by num. of comments--

19. NYT journalist hacked with Pegasus after reporting on previous hacking attempts, 278 comments, 934 points
27. To learn a new language, read its standard library, 193 comments, 343 points
17. Jetson One – Personal Electric Aerial Vehicle, 180 comments, 208 points
4. WhatsApp scaled to 1B users with only 50 engineers, 145 comments, 164 points
[...]

-- Entries with less than 5 words or equal in title, sorted by points--

20. Across Kazakhstan by rail, 60 comments, 162 points
30. Signed integers are asymmetrical, 113 comments, 121 points
21. Fun with Nano Server, 12 comments, 57 points
22. Art Vote, 30 comments, 56 points
```

## Observations
### Why does this only work for Python >3.9?
Python 3.9 introduces with [PEP 585](https://www.python.org/dev/peps/pep-0585/) built-in support for
type hinting generics in standard collections. Because of this, the code is not supported by previous versions
of Python; however, I believe you can do some minor changes to make this work for versions 3.5 up to 3.8 by adding
this line:
```python
from typing import List
```
at the top of the source code files which use type annotations for `list`, and replacing
appearances of `list` with `List` (e.g. `list[Entry]` with `List[Entry]`) in such annotations.
