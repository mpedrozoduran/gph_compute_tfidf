from compute.tf_idf import TfIdf
from utils.utils import get_articles_file


def test_should_call_compute_tfidf():
    text_sample = (
        "the mayor is facing growing calls to address chaotic and violent conditions"
    )
    limit = 3
    article = get_articles_file()
    subject = TfIdf(article)
    res = subject.compute_tfidf(text_sample, limit)
    assert res is not None
