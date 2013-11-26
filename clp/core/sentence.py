__author__ = 'sun'


class Sentence(object):

    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.words = []


    def segement_words(self, word_segmenter):

        self.words = []

        for sentence in self.sentences:
            self.words.append(word_segmenter.segment(sentence))