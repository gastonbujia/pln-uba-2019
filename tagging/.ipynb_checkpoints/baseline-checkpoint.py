from collections import defaultdict


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
        for sent in tagged_sents:
            nsents += 1
            for word, tag in sent:
                self._word_tags[word][tag] += 1 
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
        self
        return self._default_tag

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return self._default_tag
