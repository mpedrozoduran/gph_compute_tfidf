import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

SPACE = " "
DEFAULT_LIMIT = 10


class TfIdf:
    def __init__(self, articles_file):
        self.article_df = TfIdf.load_article(articles_file)
        self.tfidfvectorizer = TfidfVectorizer(
            stop_words="english",
            lowercase=True,
            use_idf=True,
            norm=u"l2",
            smooth_idf=True,
        )
        self.tfidfvectorizer.fit_transform(self.article_df["content"])

    def compute_tfidf(self, text, limit):

        tfidf_term_vectors = self.tfidfvectorizer.fit_transform([text])
        tfidf_term_vectors.todense()
        tokens = self.tfidfvectorizer.get_feature_names()
        df_tfidfvect = pd.DataFrame(data=tfidf_term_vectors.toarray(), columns=tokens)
        upper_limit = DEFAULT_LIMIT if limit <= 0 else limit - 1
        data = df_tfidfvect.iloc[0:1, 0:upper_limit]
        return data

    @staticmethod
    def load_article(articles_file):
        return pd.read_csv(articles_file)
