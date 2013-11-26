__author__ = 'sun'


from collections import defaultdict, Counter


class WordIdMap(object):

    def __init__(self):

        self.word_id_map = dict()
        self.id_word_map = dict()

        self.tns = defaultdict(Counter)        #term number in each document
        self.dns = Counter()                   #doc number containing each term

    def occupy_word_id(self, word):
        if word not in self.word_id_map:
            cur_top_idx = len(self.word_id_map)
            self.word_id_map[word] = cur_top_idx
            self.id_word_map[cur_top_idx] = word

        return self.word_id_map[word]


    def add_document(self, document):

        word_id_set = set()

        for word in document.words:

            word_id = self.occupy_word_id(word)

            self.tns[document.id][word_id] += 1

            if word_id not in word_id_set:

                self.dns[word_id] += 1
                word_id_set.add(word_id)

    def filter_words(self, min_occur = None, max_occur_ratio = None):

        doc_num = len(self.tns)

        word_id_remove = set()

        for word in self.word_id_map:
            word_id = self.word_id_map[word]

            if min_occur and self.dns[word_id] < min_occur:
                word_id_remove.add(word_id)

                continue

            if max_occur_ratio and self.dns[word_id] > max_occur_ratio * doc_num:
                word_id_remove.add(word_id)
                continue

        for word_id in word_id_remove:

            del self.word_id_map[self.id_word_map[word_id]]
            del self.id_word_map[word_id]
            del self.dns[word_id]

        for doc_id in self.tns:
            self.tns[doc_id] = dict((k, v ) for k in self.tns[doc_id] if k not in word_id_remove)


    def reorder_word_id(self):

        old_new_map = dict()

        idx = 0

        for word in self.word_id_map:

            old_word_id = self.word_id_map[word]

            old_new_map[old_word_id] = idx

            idx += 1


        self.word_id_map = dict( (k,old_new_map[v]) for (k, v) in self.word_id_map.iteritems())
        self.id_word_map = dict( (old_new_map[k],v) for (k, v) in self.id_word_map.iteritems())
        self.dns = dict( (old_new_map[k],v) for (k, v) in self.tns.iteritems())

        for doc_id in self.tns:
            self.tns[doc_id] = dict((old_new_map[k], (k, v) ) for k in self.tns[doc_id].iteritems())


    def save_word_dictionary(self, file_name):

        with open(file_name, 'w') as output:
            output.write('\n'.join(self.word_id_map.keys()))

    def save_doc_word_freq(self, file_name):

        with open(file_name, 'w') as output:

            for doc_id in self.tns:
                output.write('\n'.join("\t".join([doc_id, word_id, n] for word_id, n in self.tns[doc_id].iteritmes())))