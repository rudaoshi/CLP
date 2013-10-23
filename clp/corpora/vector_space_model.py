__author__ = 'sun'

from gensim import corpora, models, similarities

class WordIdMap(object):

    def __init__(self):

        self.dictionary = corpora.Dictionary()

    def add_document(self, document):

        self.dictionary.doc2bow(document.words, allow_update = True)

    def find_stop_words(self):
        pass