from CategorizerEmails import CategorizerEmails
from PickleUtils import PickleUtils
import os

# Crear nuestro vocabulario
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_HAM_PATH = ROOT_DIR + '/data/test/ham'
TEST_SPAM_PATH = ROOT_DIR + '/data/test/spam'

vocabulary = []

os.chdir(TEST_HAM_PATH)
for filename in os.listdir():
    file = open(filename, 'r')
    vocabulary += CategorizerEmails.process_text(file.read())
    file.close()

os.chdir(TEST_SPAM_PATH)
for filename in os.listdir():
    file = open(filename, 'r')
    vocabulary += CategorizerEmails.process_text(file.read())
    file.close()

loaded = PickleUtils.load(ROOT_DIR, 'categorized_emails_processed')
for (words, tag) in loaded:
    vocabulary += words

print("Custom vocabulary len: ", len(vocabulary))
PickleUtils.save(ROOT_DIR+'/save', 'custom_vocabulary', vocabulary)