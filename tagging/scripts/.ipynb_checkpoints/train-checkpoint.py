"""Train a sequence tagger.

Usage:
  train.py [options] -c <path> -o <file>
  train.py -h | --help

Options:
  -m <model>    Model to use [default: badbase]:
                  badbase: Bad baseline
                  base: Baseline
                  clf: ClassifierTagger
  -f <function> Classifier function:
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
from classifier import ClassifierTagger

models = {
    'badbase': BadBaselineTagger,
    'base': BaselineTagger,
    'clf': ClassifierTagger
}


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader(opts['-c'], files)
    sents = corpus.tagged_sents()

    # train the model
    model_class = models[opts['-m']]
    if opts['-m']=='clf':
        model = model_class(sents, opts['-f'])
    else:
        model = model_class(sents)
        
    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
    
    
