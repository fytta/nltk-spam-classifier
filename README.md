## nltk-spam-classifier
Trabajo para la asignatura Ingeniería del Lenguaje Natural del Master de Ingenieria y Tecnologías de Sistemas Software

## Paquetes a descargar
nltk.download('words')   
nltk.download('punkt')   
nltk.download('stopwords')   

## Pasos
1. Limpiar y categorizar los emails del dataset. Para esto se ha creado un script que guarda el fichero
    con los datos preparados. El fichero ya esta cargado con emails del dataset de Enron
    ProcessEmailsScript.py

2. Entrenar el modelo con los datos que se han procesado en el punto anterior.
    TrainClassifierScript.py

3. Evaluar el modelo.
    TestClassifierScript.py
