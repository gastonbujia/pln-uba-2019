"""Train a sequence tagger.

Usage:
  train.py [options] -c <path> -o <file>
  train.py -h | --help

Options:
  -m <model>    Model to use [default: badbase]:
                  badbase: Bad baseline
                  base: Baseline
                  lr: LogisticRegression,
                  svm: LinearSVC,
                  nb: MultinomialNB
  -c <path>     Ancora corpus path.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle

from tagging.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger, BadBaselineTagger
from tagging.classifier import ClassifierTagger, vectorize

models = {
    'badbase': BadBaselineTagger,
    'base': BaselineTagger,
    'lr': ClassifierTagger,
    'svm': ClassifierTagger,
    'nb': ClassifierTagger
}


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader(opts['-c'], files)
    sents = corpus.tagged_sents()

    # train the model
    if opts['-m']=='lr' or opts['-m']=='svm' or opts['-m']=='nb':
        model_class = models[opts['-m']]
        model = model_class(sents, opts['-m'])
    else: 
        model_class = models[opts['-m']]
        model = model_class(sents)
        
    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
