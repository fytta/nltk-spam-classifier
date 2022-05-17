from PickleUtils import PickleUtils 
from CategorizerEmails import *
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HAM_PATH = ROOT_DIR + '/data/ham'
SPAM_PATH = ROOT_DIR + '/data/spam'

ham_files = CategorizerEmails.process_categorize('HAM', HAM_PATH)
spam_files = CategorizerEmails.process_categorize('SPAM', SPAM_PATH)

print ('HAM files categorized: ', len(ham_files))
print ('SPAM files categorized: ', len(spam_files))

categorized_emails = [*ham_files, *spam_files]

# Guarda el resultado de los emails limpios y categorizados en la carpeta raiz del proyecto
# con el nombre categorized_emails_processed.pickle
PickleUtils.save(ROOT_DIR+'/save', 'categorized_emails_processed', categorized_emails)

# Abre el fichero y compruebo que se haya guardado bien
categorized_emails = PickleUtils.load(ROOT_DIR+'/save', 'categorized_emails_processed')
print(len(categorized_emails), ' categorized emails loaded')