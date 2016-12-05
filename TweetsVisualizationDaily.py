import csv

import datetime
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

import config

tls.set_credentials_file(username=config.username, api_key=config.api_key)

def read_csv(filename, _date):
    data = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        totalFavorites = 0;
        totalRetweets = 0;
        user_name = '';
        numberOfTweets = 0

        for row in reader:
            user_name = row['name']
            if _date in str(row['created_at']):
                numberOfTweets += 1
                totalFavorites += int(row['favorite_count'])
                totalRetweets += int(row['retweet_count'])

    data.append(user_name)
    data.append(numberOfTweets)
    data.append(totalRetweets)
    data.append(totalFavorites)
    return data

presidentsData = []
yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime("%Y-%m-%d")
today = datetime.datetime.now().strftime("%Y-%m-%d")

for p in config.pre_candidate_keywords:
    presidentsData.append(read_csv('%s_tweets.csv' % p, yesterday))

print(presidentsData)
numberOfTweets = []
numberOfRetweets = []
numberOfFavorites = []
for p in presidentsData:
    numberOfTweets.append(p[1])
    numberOfRetweets.append(p[2])
    numberOfFavorites.append(p[3])

tweets = go.Bar(
    x=config.pre_candidate_names,
    y=numberOfTweets,
    name='Tweets'
)
retweets = go.Bar(
    x=config.pre_candidate_names,
    y=numberOfRetweets,
    name='Retweets'
)
favorites = go.Bar(
    x=config.pre_candidate_names,
    y=numberOfFavorites,
    name='Favorites'
)

data = [tweets, retweets, favorites]

layout = dict(title=config.dailyGraphicsTitle,
              xaxis=dict(title=config.dailyGraphicsXaxis),
              yaxis=dict(title=config.dailyGraphicsYaxis),
              barmode='stack',
              )

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='presidential-candidates-daily-report')