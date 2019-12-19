from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


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
        'nextLower': '<u>',  # ultima token
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

def dataVectorizer(sents):
    
    X = []
    y_true = []
    for sent in sents:
    for i, (word, tag) in enumerate(sent):
        x = feature_dict(sent, i)
        X.append(x)
        y_true.append(tag)
    
    vect = DictVectorizer()
    X2 = vect.fit(X)
    
    return X2, y_true, vect


class ClassifierTagger:
    """Simple and fast classifier based tagger.
    """

    def __init__(self, tagged_sents, clf='lr'):
        """
        tagged_sents -- X, y_true (feature_matrix and vector)
        clf -- classifying model, one of 'svm', 'lr' (default: 'lr').
        """
        self.classifier = classifiers[clf] 
        self.sentences = tagged_sents
        
    def fit(self, tagged_sents):
        """
        Train.

        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        return self.classifier.fit(tagged_sents)
        
    def tag_sents(self, sents):
        """Tag sentences.

        sent -- the sentences.
        """
        return [self.tag(w) for w in sents]

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return np.array([self.classifier.predict(w) for w in sent])

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return True
