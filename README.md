# chatbot_igor

Experimento en Python que combina análisis de texto y un cliente de Twitter. `main.py` consulta publicaciones, analiza sus resultados y llama a una operación de retweet cada 30 segundos.

## Estructura

- [TextAnalyzer.py](TextAnalyzer.py)
- [TwitterClient.py](TwitterClient.py)
- [main.py](main.py)
- [processJson.py](processJson.py)
- [training_model.py](training_model.py)

## Preparación y uso

El proyecto usa APIs antiguas de TensorFlow/tflearn y Twitter, y no incluye un manifiesto de dependencias con versiones. Revisa `TwitterClient.py`, `TextAnalyzer.py`, `training_model.py` y `settings.py` antes de preparar un entorno compatible. Las importaciones incluyen tweepy, NLTK, TextBlob, NumPy, TensorFlow, tflearn y BeautifulSoup. No hay una instalación reproducible validada; `python main.py` realiza acciones en la cuenta configurada.

## Validación y estado

Esta guía se contrastó con el árbol de archivos y los manifiestos del repositorio. No se ha validado una ejecución completa contra servicios externos, bases de datos o hardware. Las versiones y los scripts mostrados describen el código actual; no implican que sus dependencias antiguas sigan siendo compatibles.
