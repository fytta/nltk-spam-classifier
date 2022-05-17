import nltk
from nltk.probability import FreqDist

class SpamClassifier:

    word_features = []

    def build_vocabulary(self, categorized_emails):
        vocabulary = []
        for (email, category) in categorized_emails:
            vocabulary.extend(email)
        return vocabulary


    def get_words_features(self, wordlist):
        wordlist = FreqDist(wordlist)
        self.word_features = wordlist.keys()
        return self.word_features


    def extract_features(self, document):
        document_words = set(document)
        features = {}
        for word in self.word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features


    def get_features_dataset(self, categorized_emails, ntrain):
        ntrain = round(len(categorized_emails) * ntrain)
        training_data = nltk.classify.apply_features(self.extract_features, categorized_emails[:ntrain])
        testing_data = nltk.classify.apply_features(self.extract_features, categorized_emails[ntrain:])
        return training_data, testing_data


    def train(self, training_data):
        return nltk.NaiveBayesClassifier.train(training_data)


    def test(self, classifier, testing_data):
        return nltk.classify.accuracy(classifier, testing_data)