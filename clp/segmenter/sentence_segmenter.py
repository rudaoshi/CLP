#encoding=utf-8


__author__ = 'sun'

import re

from clp.core.sentence import Sentence

class SentenceSegmenter(object):

    def segment(doc):

        splitter = [u'。',u'！',u'？',u'\n']


        for idx, sent in enumerate(re.split('|'.join(splitter), doc.content)):
            sentence = Sentence(idx,sent)

            yield sentence



