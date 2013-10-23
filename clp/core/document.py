

class Document(object):

    def __init__(self, content):
        self.content = content
        self.sentences = []
        self.words = []

    def segment(self, segmenter):

        return segmenter.segment(self.content)

    def split_sentences(self, sentence_segmenter):
        self.sentences = sentence_segmenter.segment(self.content)

    def segement_words(self, word_segmenter):

        self.words = []

        for sentence in self.sentences:
            self.words.append(word_segmenter.segment(sentence))