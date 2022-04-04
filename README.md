# Twitter Sentiment Analysis

Live: [https://tweetsental.herokuapp.com/](https://tweetsental.herokuapp.com/)

Este es el repositorio dedicado a la Web App de analisis de sentimientos de Twitter,

en la cual podras elegir el tema o hashtag que inluya los tweets para ser analizados si se habla

positivamente, negativamente o de forma neutral acerca del tema dado, tambien podras escoger

el numero de tweets a importar y el idioma ya sea Ingles o Español.

Ademas cuenta con un fomulario para analizar el texto de tu propio tweet.

## Librerias Utilizadas

Para esta Web App se utilizo:

- Flask como framework de backend
- Textblob y NLTK para el analisis de sentimientos
- Chat.js para la creacion de un pie chart
- Tweepy para el accesso a la API de Twitter

## Correr la aplicacion en servidor local

- Realizar un git clone con el siguiente comando en una terminal

```
git clone https://github.com/erikqtrs/twitter-sentiment-analysis.git
```
- Una vez dentro de la carpeta del repositorioinstalar los paquetes que se encuentran en el archivo requirements.txt con el comando:

```
pip install -r requiremnts.txt
```
- Deberan crear una cuenta de desarrollador en Twitter API y obtener sus credenciales,

las cuales deberan ponerlas en un archivo **.env** con los nombres de:
 - CONSUMER_KEY
 - CONSUMER_KEY_SECRET
 - API_KEY
 - API_KEY_SECRET
estas variables estan importadas en el archivo twitter_api.py dentro de la carpeta nlp.


