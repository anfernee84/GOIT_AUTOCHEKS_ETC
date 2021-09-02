import os
from typing import Dict

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes = [open(_file, encoding='utf-8').read()
                 for _file in student_files]
corpus_ = {k: v for k, v in zip(student_files, student_notes)}


class PlagiarismChecker:
    def __init__(self):
        self._vectorizer = TfidfVectorizer()

    def vectorize(self, texts):
        return self._vectorizer.fit_transform(texts).toarray()

    @staticmethod
    def similarity(text1, text2):
        return cosine_similarity(text1, text2)

    def check_plagiarism(self, corpus: Dict):
        vectorized_texts = self.vectorize(corpus.values())
        filenames = list(corpus.keys())
        results = pd.DataFrame(index=filenames, columns=filenames)
        similarity_results = cosine_similarity(vectorized_texts, vectorized_texts)
        for filename, row in zip(filenames, similarity_results):
            results[filename] = row
        return results

# print(PlagiarismChecker().check_plagiarism(corpus_))
