import pickle
from nlp_train import remove_noise
from nltk.tokenize import word_tokenize

def analyze_comments(comments):
    result = []

    classifier_f = open("classifier.pickle", "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()

    for comment in comments:
        tokens = remove_noise(word_tokenize(comment))
        classification = classifier.classify(dict([token, True] for token in tokens))
        result.append(tuple((comment, classification)))

    return result
