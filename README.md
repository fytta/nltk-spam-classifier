## Paqueetes a descargar
nltk.download('words')
nltk.download('punkt')
nltk.download('stopwords')

## Pasos
1. Limpiar y categorizar los emails del dataset. Para esto se ha creado un script que guarda el fichero
    con los datos preparados. El fichero ya esta cargado con 10000 emails del dataset de Enron
    process-emails-script.py

2. Entrenar el modelo con los datos que se han procesado en el punto anterior.
    train-classifier-script.py

3. Evaluar el modelo.
    test-classifier-script.py