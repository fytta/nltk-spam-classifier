from PickleUtils import PickleUtils
import os
import random
from SpamClassifier import SpamClassifier

classifier = SpamClassifier()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

vocabulary = PickleUtils.load(ROOT_DIR+'/save', 'custom-vocabulary')
categorized_emails = PickleUtils.load(ROOT_DIR+'/save', 'categorized_emails_processed')
random.shuffle(categorized_emails)

categorized_emails_list = categorized_emails[:100]

word_features = classifier.get_words_features(vocabulary)

training_data, testing_data = classifier.get_features_dataset(categorized_emails_list, 0.8)
print(training_data[0])
# spamClassifier = classifier.train(training_data)
# accuracy_train_data = classifier.test(spamClassifier, training_data)
# accuracy_test_data = classifier.test(spamClassifier, testing_data)

# print('Using vocabulary with ', len(vocabulary), ' length')
# print('Testing accuracy with training data: ', accuracy_train_data)
# print('Testing accuracy with testing data: ', accuracy_test_data)

# spamClassifier.show_most_informative_features()

#PickleUtils.save(ROOT_DIR+'/save', 'classifier', spamClassifier)