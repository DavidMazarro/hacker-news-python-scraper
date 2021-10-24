![GitHub Actions badge](https://github.com/DavidMazarro/hacker-news-python-scraper/actions/workflows/python-testing.yml/badge.svg)
# Hacker News scraper (in Python)
This is just a basic scraper that takes the first 30 entries from the Hacker News frontpage,

## Installation

You need to have [Python](https://www.python.org/) installed for this program to work. 
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
