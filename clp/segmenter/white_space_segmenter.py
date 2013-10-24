__author__ = 'sun'


from clp.segmenter.segmenter import Segmenter


class WhiteSpaceSegmenter(Segmenter):

    def __init__(self):

        super(self, WhiteSpaceSegmenter).__init__()

    def segment(self, strings):

        return strings.split()