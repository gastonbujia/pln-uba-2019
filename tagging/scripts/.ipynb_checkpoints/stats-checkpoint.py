"""Print corpus statistics.

Usage:
  stats.py -c <path>
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
from collections import defaultdict

from tagging.ancora import SimpleAncoraCorpusReader

# TODO: preguntar si conviene o no definir el atributo como None y despues asignarlo en el metodo o no

class POSStats:
    """Several statistics for a POS tagged corpus.
    """

    def __init__(self, tagged_sents):
        """
        tagged_sents -- corpus (list/iterable/generator of tagged sentences) - LazyMap
        """
        # WORK HERE!!
        # COLLECT REQUIRED STATISTICS INTO DICTIONARIES.
        self.tagged_sents = tagged_sents
        self.word_tags = defaultdict(lambda: defaultdict(int))
        self.tag_words = defaultdict(lambda: defaultdict(int))
        self.tag_freq = defaultdict(int)
        self.word_freq = defaultdict(int)
        nsents = 0
        token = 0
        for sent in self.tagged_sents:
            nsents += 1
            for word, tag in sent:
                self.word_tags[word][tag] += 1 
                self.tag_words[tag][word] += 1
                self.word_freq[word] += 1
                self.tag_freq[tag] += 1
                token += 1
        self._scount = nsents
        self._tkcount = token
        self._wcount = len(self.word_tags)
        self._tcount = len(self.tag_words)
        self.word_tags = dict(self.word_tags)
        self.tag_words = dict(self.tag_words)
        self.tag_freq = dict(self.tag_freq)
        self.word_freq = dict(self.word_freq)
        
    def sent_count(self):
        """Total number of sentences."""
        return self._scount

    def token_count(self):
        """Total number of tokens."""
        return self._tkcount
        
    def words(self):
        """Vocabulary (set of word types)."""
        return set(self.word_tags.keys())

    def word_count(self):
        """Vocabulary size."""
        return self._wcount

    def word_freq(self, w):
        """Frequency of word w."""
        return dict(self.word_freq)
    
    def unambiguous_words(self):
        """List of words with only one observed POS tag."""
        
        return [word for word in self.word_tags.keys() if len(dict(self.word_tags[word])) == 1]

    def ambiguous_words(self, n):
        """List of words with n different observed POS tags.

        n -- number of tags.
        """
        
        return [word for word in self.word_tags.keys() if len(dict(self.word_tags[word])) == n]

    def tags(self):
        """POS Tagset."""
        return list(self.tag_freq.keys())

    def tag_count(self):
        """POS tagset size."""
        return self._tcount

    def tag_freq(self, t):
        """Frequency of tag t."""
        return self.tag_freq

    def tag_word_dict(self, t):
        """Dictionary of words and their counts for tag t."""
        return dict(self.tag_words[t])

if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    corpus = SimpleAncoraCorpusReader(opts['<path>'])
    sents = corpus.tagged_sents()

    # compute the statistics
    stats = POSStats(sents)

    print('Basic Statistics')
    print('================')
    print('sents: {}'.format(stats.sent_count()))
    token_count = stats.token_count()
    print('tokens: {}'.format(token_count))
    word_count = stats.word_count()
    print('words: {}'.format(word_count))
    print('tags: {}'.format(stats.tag_count()))
    print('')

    print('Most Frequent POS Tags')
    print('======================')
    tags = [(t, stats.tag_freq[t]) for t in stats.tags()]
    sorted_tags = sorted(tags, key=lambda t_f: -t_f[1])
    print('tag\tfreq\t%\ttop')
    for t, f in sorted_tags[:10]:
        words = stats.tag_word_dict(t).items()
        sorted_words = sorted(words, key=lambda w_f: -w_f[1])
        top = [w for w, _ in sorted_words[:5]]
        print('{0}\t{1}\t{2:2.2f}\t({3})'.format(t, f, f * 100 / token_count, ', '.join(top)))
    print('')

    print('Word Ambiguity Levels')
    print('=====================')
    print('n\twords\t%\ttop')
    for n in range(1, 10):
        words = list(stats.ambiguous_words(n))
        m = len(words)

        # most frequent words:
        sorted_words = sorted(words, key=lambda w: -stats.word_freq[w])
        top = sorted_words[:5]
        print('{0}\t{1}\t{2:2.2f}\t({3})'.format(n, m, m * 100 / word_count, ', '.join(top)))
