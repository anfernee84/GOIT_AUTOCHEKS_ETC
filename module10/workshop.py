import os
import pandas as pd
from typing import Dict
import sklearn.feature_extraction.text


student_filenames = [fname for fname in os.listdir('.') if fname.endswith (".txt")]
student_notes = [open(fname).read() for fname in student_filenames]

corpus = {k: v for k,v in zip (student_filenames, student_notes)}

class PlagiarismChecker:
    def __init__(self):
        self._vectorizer = TfidfVectorizer()

    def vectorize(self,text: List):
        retutn self._vectorizer.fit_transform(texts).toarray()


    @staticmethod
    def similarity (text1, text2):
        return cosine_similarity(text1,text2)

    def check(self, corpus: Dict):
        vectorized_text = self.vectorize(corpus.values())
        filenames = list(corpus.keys())
        results


