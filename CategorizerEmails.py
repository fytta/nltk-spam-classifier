import os
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class CategorizerEmails:
    """
    Clase para procesar el texto de los ficheros de los emails.
    """

    def process_categorize(tag, path):
        """
        Lee todos los ficheros que hayan en la carpeta pasada por parámetro.
        Para cada fichero, elimina los simbolos de puntuacion y las stopwords del texto y
        crea un lista de tuplas (data, tag).
        Arguments:
            tag: tag que se le asignara al texto extraido de los ficheros.
            path: ruta donde deben estar ubicados los ficheros.
        Return:
            Lista de tuplas (data, tag)
        """
        os.chdir(path)
        categorized_files = []
        count = 0
        for file_name in os.listdir():
            file = open(file_name, 'r')
            text = file.read()
            file.close()

            cleaned = CategorizerEmails.process_text(text)
            categorized_files.append((cleaned, tag))
            count += 1
            if count % 50 == 0: 
                print("Process ", count, " emails ...")
        return categorized_files

    def process_text(text):
        """
        Elimina los signos de puntuacion y stopwords de un texto pasado por 
        parametro.
        Arguments:
            text: texto a procesar
        Return:
            texto procesado
        """
        processed_text = []
        for word in word_tokenize(text):
            word = word.lower()
            if word not in stopwords.words('english') and word.isdigit() == False and word not in punctuation:
                processed_text.append(word)

        return processed_text