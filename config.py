#Variables that contains the user credentials to access Twitter API
import datetime

access_token = "765129173140725760-281bSWa7dSOCxp9w5hWYUrHFRFplQkL"
access_token_secret = "roa9zDpx4LwNXLFyMkHPQggBvzsBgkSM3igXGDNBcWyTn"
consumer_key = "RtEMttVUDINmULh9FlYhpUfsB"
consumer_secret = "CHk9H4jWF6hZXQtz2K6POdsZsI8p2UkbbwAnSK0k1VzSXmaSto"

# username and API key to access Plotly in order to show the graphics
username='graphics_VAA'
api_key='hsa2b84ky3'

pre_candidate_keywords = ['daloes10', 'CynthiaViteri6', 'LassoGuillermo', 'IvanEspinelM', 'Lenin', 'PacoMoncayo',
                               'PZuquilanda', 'pesanteztwof']
pre_candidate_names = ['Abdalá Bucaram', 'Cynthia Viteri', 'Guillermo Lasso', 'Iván Espinel', 'Lenin Moreno',
                       'Paco Moncayo', 'Patricio Zuquilanda', 'Washington Pesántez']

vicepre_candidate_keywords = ['ramiroaguilart', 'MauricioPozoEC', 'andrespaezec', 'JorgeGlas', 'MonseBustamant', 'a_alcivar']
vicepre_candidate_names = ['Ramiro Aguilar', 'Mauricio Pozo', 'Andrés Páez', 'Jorge Glas', 'Monserratt Mustamante', 'Alex Alcivar']

colors = [('rgb(102, 204, 0)'), ('rgb(35, 145, 254)'), ('rgb(255, 153, 51)'), ('rgb(255, 255, 102)'), ('rgb(255, 102, 255)'),
                       ('rgb(96, 96, 96)'), ('rgb(0, 255, 255)'), ('rgb(0, 0, 255)')]

start_date='2016-11-20'

yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime("%Y-%m-%d")

dailyGraphicsTitle='Actividad en Twitter. Fecha: %s' % yesterday
dailyViceGraphicsTitle='Actividad en Twitter. Fecha: %s' % yesterday
dailyGraphicsXaxis=''
dailyGraphicsYaxis='Número de Tweets'

monthlyGraphicsTitle='Actividad en Twitter de Candidatos Presidenciales'
monthlyViceGraphicsTitle='Actividad en Twitter de Candidatos a Vicepresidente'
monthlyGraphicsXaxis=''
monthlyGraphicsYaxis='Número de Tweets'
