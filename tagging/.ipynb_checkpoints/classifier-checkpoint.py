import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
from time import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


classifiers = {
    'lr': LogisticRegression,
    'svm': LinearSVC,
    'nb': MultinomialNB
}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def feature_dict(sent, i):
    """Feature dictionary for a given sentence and position.

    sent -- the tokenized(creo) sentence.
    i -- the position.
    """
    # Dada una oracion devuelve los features que tiene: 
    # la palabra actual en minúsculas.
    # si la palabra actual empieza en mayúsculas.
    # si la palabra actual está en mayúsculas.
    # si la palabra actual es un número.
    # mismos features para la palabra anterior y para la siguiente.
    features = {
        'lower': sent[i][0].lower(),
        'firstUpper': sent[i][0][0].isupper(),
        'isUpper': sent[i][0].isupper(),
        'isNumber': is_number(sent[i][0])
        }
    
    if i == 0:
        features_prev = {
        'prevLower': '<p>', # primer token
        'prevFirstUpper': False,
        'prevIsUpper': False,
        'prevIsNumber': False
        }
    else:
        features_prev = {
        'prevLower': sent[i-1][0].lower(),
        'prevFirstUpper': sent[i-1][0][0].isupper(),
        'prevIsUpper': sent[i-1][0].isupper(),
        'prevIsNumber': is_number(sent[i-1][0])
        }
    
    #features = dict(features, features_prev)
    features.update(features_prev)
    if i == len(sent)-1:
        features_next = {
        'nextLower': '<u>',  # ultimo token
        'nextFirstUpper': False,
        'nextIsUpper': False,
        'nextIsNumber': False
        }
    else:
        features_next = {
        'nextLower': sent[i+1][0].lower(),
        'nextFirstUpper': sent[i+1][0][0].isupper(),
        'nextIsUpper': sent[i+1][0].isupper(),
        'nextIsNumber': is_number(sent[i+1][0])
        }
    
    #features = dict(features, features_next)
    features.update(features_next)
    return features


class ClassifierTagger:
    """Simple and fast classifier based tagger.
    """

    def __init__(self, tagged_sents, clf='lr'):
        """
        tagged_sents -- X, y_true (feature_matrix and vector)
        clf -- classifying model, one of 'svm', 'lr' (default: 'lr').
        """
        self.sentences = list(tagged_sents)
        self._words = []
        self.time = 0
        self.pipeline = Pipeline([
                ('vectorizer', DictVectorizer()),
                ('classifier', classifiers[clf]())],
                verbose = True)
        self.fit(self.sentences)
        
    def _dataSeparation(self, sents):

        X = []
        y_true = []
        for sent in sents:
            for i, (word, tag) in enumerate(sent):
                self._words.append(word)
                x = feature_dict(sent, i)
                X.append(x)
                y_true.append(tag)

        return X, y_true
    
    def fit(self, tagged_sents):
        """
        Train.

        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        tagged_sents = list(tagged_sents)
        X, y = self._dataSeparation(tagged_sents)
        start = time()
        #self.classifier.fit(X, y)
        self.pipeline.fit(X, y)
        self.time = time() - start
        print("Tiempo de vectorizacion  + entrenamiento: {}".format(self.time))
        
    def tag_sents(self, sents):
        """Tag sentences.

        sent -- the sentences.
        """
        return [self.tag(sent) for sent in sents]

    def tag(self, sent):
        """Tag a sentence (list of pairs).

        sent -- the sentence.
        """
        #y = []
        #for i, (w,t) in enumerate(sent):
            #x = feature_dict(sent,i)
            ##y.append((w, self.classifier.predict(x)))
            #y.append(self.pipeline.predict(x))
        
        #return y
        return self.pipeline.predict([feature_dict(sent, i) for i in range(len(sent))])
    
    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        if w in self._words:
            return False
        else:
            return True
