__author__ = 'sun'


__author__ = 'sun'

from clp.core.document import Document

from clp.segmenter.sentence_segmenter import SentenceSegmenter

import codecs

def make_sentence_corpora(baike_input_file_path, output_file_path):

    output = codecs.open(output_file_path,'r','utf-8')

    with codecs.open(baike_input_file_path,'r','utf-8') as input:
        for line in input:
            document = Document(line.strip())
            document.split_sentences(SentenceSegmenter())


            for sentence in document.sentences:
                output.write(str(document.id) + "\t" + str(sentence.id) + "\t" + sentence.content + "\n")



import sys
if __name__ == "__main__":

    try:
        _, input, output = sys.argv
    except:

        print "_, input, output"
        exit(1)

    make_sentence_corpora(input,output)