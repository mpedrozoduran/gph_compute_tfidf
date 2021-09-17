from scraping import scraping


def test_should_call_process_text():
    url = "https://www.nytimes.com/2021/09/14/health/sickle-cell-cure.html"
    text = scraping.process_text(url)
    assert text is not None
