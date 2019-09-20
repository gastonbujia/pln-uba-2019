from collections import defaultdict
import operator

class BadBaselineTagger:

    def __init__(self, tagged_sents, default_tag='nc0s000'):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for all words.
        """
        self._default_tag = default_tag

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        return self._default_tag

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return True


class BaselineTagger:

    def __init__(self, tagged_sents, default_tag = "nc0s000"):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for unknown words - ACCORDING TO ASKED = "nc0s000".
        """
        self._word_tags = defaultdict(lambda: defaultdict(int))
        #self._words = set()
        for sent in tagged_sents:
            for word, tag in sent:
                self._word_tags[word][tag] += 1
                #self._words.add(word)
        self._word_tags = dict(self._word_tags)
        self._default_tag = default_tag

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.
        - ACCORDING TO ASKED each word is tagged with the most frequent tag seen in corpus train
        w -- the word.
        """
        if self.unknown(w):
            return self._default_tag
        else:
            sorted_tags = sorted(self._word_tags[w].items(), key=lambda x: x[1])
            return sorted_tags[-1][0]
        
    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        if w in self._word_tags.keys():
            return False
        return True
