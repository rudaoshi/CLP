__author__ = 'sun'

from clp.core.document import Document

from clp.segmenter.white_space_segmenter import WhiteSpaceSegmenter

from clp.corpora.vector_space_model import WordIdMap

def make_biake_corpora(baike_input_file_path, output_file_path):

    word_id_map = WordIdMap()
    with open(baike_input_file_path,'r') as input:
        for line in input:
            document = Document(line.strip())
            document.split_sentences(WhiteSpaceSegmenter())
            document.segement_words(WhiteSpaceSegmenter())

            word_id_map.add_document(document)

    word_id_map.save_as_text(output_file_path)


import sys
if __name__ == "__main__":

    try:
        _, input, output = sys.argv
    except:

        print "_, input, output"
        exit(1)

    make_biake_corpora(input,output)