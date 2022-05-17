from PickleUtils import PickleUtils
import os
from SpamClassifier import SpamClassifier

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
spamClassifier = PickleUtils.load(ROOT_DIR+'/save', 'classifier')
classifier = SpamClassifier()

vocabulary = PickleUtils.load(ROOT_DIR+'/save', 'custom-vocabulary')
categorized_emails = PickleUtils.load(ROOT_DIR+'/save', 'categorized_emails_processed')
word_features = classifier.get_words_features(vocabulary)

count = 0
total_files = 0
path = ROOT_DIR+'\\data\\test\\spam\\'

os.chdir(path)
total_files += len(os.listdir())
for file_name in os.listdir():
    file = open(file_name, 'r')
    predict = spamClassifier.classify(classifier.extract_features(file.read().split()))
    file.close()
    if predict != 'SPAM':
        count += 1

path = ROOT_DIR+'\\data\\test\\ham\\'
os.chdir(path)
total_files += len(os.listdir())
for file_name in os.listdir():
    file = open(file_name, 'r')
    predict = spamClassifier.classify(classifier.extract_features(file.read().split()))
    file.close()
    if predict != 'HAM':
        count += 1

print (count, ' fallos de ', total_files, ' : ', count/total_files, ' fail ratio')