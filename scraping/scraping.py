from bs4 import BeautifulSoup
from urllib.request import urlopen

PARSER = "html.parser"


def process_text(url):
    page = urlopen(url)
    text = page.read().decode("utf-8")
    bs = BeautifulSoup(text, PARSER)
    return bs.get_text()
