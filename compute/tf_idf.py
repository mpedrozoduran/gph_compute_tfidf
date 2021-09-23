import math
import re
import codecs
from operator import itemgetter

ARTICLE_COLS_SIZE = 10
CONTENT_INDEX = 9


class TfIdf:

    def __init__(self):
        self.terms_num_docs = {}
        self.num_docs = 0

    def get_tokens(self, str):
        return re.findall(r"<a.*?/a>|<[^\>]*>|[\w'@#]+", str.lower())

    def add_input_doc_for_idf_calculation(self, doc):
        self.num_docs += 1
        words = set(self.get_tokens(doc))
        for word in words:
            if word in self.terms_num_docs:
                self.terms_num_docs[word] += 1
            else:
                self.terms_num_docs[word] = 1

    def load_article_for_idf_calculation(self, docs):
        for doc in docs:
            file = codecs.open(doc, mode='r', encoding='utf8')
            # header
            header = file.readline()
            for line in file:
                row = line.split(',')
                if row and len(row) == ARTICLE_COLS_SIZE:
                    content = row[CONTENT_INDEX]
                    self.add_input_doc_for_idf_calculation(content)

    def calculate_tfidf(self, text, limit):
        res_tfidf = {}
        tokens = self.get_tokens(text)
        web_doc_set = set(tokens)
        for word in web_doc_set:
            tf = float(tokens.count(word)) / len(web_doc_set)
            if not word in self.terms_num_docs:
                idf = 1.5
            else:
                idf = math.log(float(self.num_docs + 1) / (self.terms_num_docs[word] + 1))
            res_tfidf[word] = tf * idf
        terms = sorted(res_tfidf.items(), key=itemgetter(1), reverse=True)
        calc_limit = 10 if limit <= 0 else limit - 1
        return terms[0:calc_limit]
