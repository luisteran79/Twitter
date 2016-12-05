import csv
import datetime
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import config
import os

tls.set_credentials_file(username=config.username, api_key=config.api_key)

def create_row(row_name, curDate, totalTweets, totalRetweets, totalFavorites, totalActivities):
    rowData = []
    rowData.append(curDate)
    rowData.append(row_name)
    rowData.append(totalTweets)
    rowData.append(totalRetweets)
    rowData.append(totalFavorites)
    rowData.append(totalActivities)
    return rowData
def create_empty_row(dataOutput, nbOfDays, screen_name, curDate):
    while (nbOfDays > 0):
        dataByData = []
        _date = (
            curDate - datetime.timedelta(
                nbOfDays)).strftime(
            "%Y-%m-%d")
        dataByData = create_row(screen_name, _date, 0, 0, 0, 0)
        dataOutput.append(dataByData)
        nbOfDays -= 1
def read_csv(filename, screen_name):
    data = []
    with open(filename, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
        totalRows = len(rows)
        totalFavorites = 0;
        totalRetweets = 0;
        totalActivities = 0;
        totalTweets = 0
        startDate = datetime.datetime.strptime(config.start_date, "%Y-%m-%d")
        curDate = datetime.datetime.now();
        interval = datetime.timedelta(0)

        for i, row in enumerate(rows):
            if i == 0:
                curDate = datetime.datetime.strptime(row['created_at'], "%Y-%m-%d %H:%M:%S")
                interval = curDate - startDate

            if curDate.strftime("%Y-%m-%d") not in str(row['created_at']) or i == totalRows - 1:
                    dataByData = []

                    # Get the day of yesterday
                    yesterday = (datetime.datetime.now() - datetime.timedelta(1))
                    rowDate = datetime.datetime.strptime(row['created_at'], "%Y-%m-%d %H:%M:%S")
                    if len(data)==0 or (len(data)==0 and i == totalRows - 1):
                        interval = curDate - startDate
                        if interval.days > 0:
                            nbOfDays = interval.days
                            create_empty_row(data,nbOfDays,screen_name,curDate)
                        if curDate.strftime("%Y-%m-%d") in row['created_at']:
                            totalTweets += 1
                            totalFavorites += int(row['favorite_count'])
                            totalRetweets += int(row['retweet_count'])
                        totalActivities = totalTweets + totalRetweets + totalFavorites;
                        dataByData = create_row(screen_name, curDate.strftime("%Y-%m-%d"), totalTweets, totalRetweets,
                                                totalFavorites, totalActivities)
                        data.append(dataByData)
                        startDate = curDate
                        if i == totalRows - 1:
                            interval = rowDate - curDate
                            totalTweets = 0
                            totalFavorites = 0
                            totalRetweets = 0
                            totalActivities = totalTweets + totalRetweets + totalFavorites;
                        totalTweets = 1
                        totalFavorites = int(row['favorite_count'])
                        totalRetweets = int(row['retweet_count'])

                    else:
                        interval = datetime.datetime.strptime(row['created_at'], "%Y-%m-%d %H:%M:%S") - curDate
                        lastDate = datetime.datetime.strptime(data[len(data)-1][0], "%Y-%m-%d")
                        if (curDate > lastDate and data[len(data)-1][0] != curDate.strftime("%Y-%m-%d")):
                            interval1 = curDate - datetime.datetime.strptime(data[len(data)-1][0], "%Y-%m-%d")
                            if interval1.days > 1:
                                nbOfDays = interval1.days-1
                                create_empty_row(data, nbOfDays, screen_name, curDate)
                        if curDate.strftime("%Y-%m-%d") in row['created_at']:
                            totalTweets += 1
                            totalFavorites += int(row['favorite_count'])
                            totalRetweets += int(row['retweet_count'])
                        totalActivities = totalTweets + totalRetweets + totalFavorites;
                        dataByData = create_row(screen_name, curDate.strftime("%Y-%m-%d"), totalTweets, totalRetweets,
                                                totalFavorites, totalActivities)
                        data.append(dataByData)
                        if interval.days > 0:
                            nbOfDays = interval.days - 1
                            create_empty_row(data, nbOfDays, screen_name, rowDate)
                        totalTweets = 1
                        totalFavorites = int(row['favorite_count'])
                        totalRetweets = int(row['retweet_count'])

                    if (i == totalRows - 1 and yesterday.strftime("%Y-%m-%d") == rowDate.strftime("%Y-%m-%d")):
                        if (data[len(data)-1][0] != rowDate.strftime("%Y-%m-%d")):
                            totalActivities = totalTweets + totalRetweets + totalFavorites;
                            dataByData = create_row(screen_name, rowDate.strftime("%Y-%m-%d"), totalTweets, totalRetweets,
                                                totalFavorites, totalActivities)
                            data.append(dataByData)

                    if (i == totalRows - 1 and yesterday > rowDate):
                        if (data[len(data)-1][0] != rowDate.strftime("%Y-%m-%d")):
                            interval = rowDate - curDate
                            if interval.days > 1:
                                nbOfDays = interval.days
                                create_empty_row(data, nbOfDays, screen_name, rowDate)
                            totalActivities = totalTweets + totalRetweets + totalFavorites;
                            dataByData = create_row(screen_name, rowDate.strftime("%Y-%m-%d"), totalTweets, totalRetweets,
                                                totalFavorites, totalActivities)
                            data.append(dataByData)
                        today = datetime.datetime.now()
                        interval = today - datetime.datetime.strptime(rowDate.strftime("%Y-%m-%d"), "%Y-%m-%d")
                        if interval.days > 0:
                            nbOfDays = interval.days - 1
                            create_empty_row(data, nbOfDays, screen_name, today)
                    curDate = rowDate
            else:
                totalTweets += 1
                totalFavorites += int(row['favorite_count'])
                totalRetweets += int(row['retweet_count'])
                curDate = datetime.datetime.strptime(row['created_at'], "%Y-%m-%d %H:%M:%S")
    #print(data)
    return data

def main():
    presidentsData = []

    os.chdir(os.path.dirname(__file__))

    for i, p in enumerate(config.pre_candidate_keywords):
        filename = '%s\%s' % (os.getcwd(), p)
        presidentsData.append(read_csv('%s_tweets.csv' % filename, config.pre_candidate_names[i]))

    #get all dates
    dates = []
    for pData in presidentsData[0]:
        dates.append(pData[0])

    #Candidat activities
    preCandidatesData = []
    count = 0
    while (count < len(presidentsData)):
        data = []
        for row in presidentsData[count]:
            data.append(row[5])
        preCandidatesData.append(data)
        count += 1

    # Create and style traces/data
    data = []
    for i, row in enumerate(config.pre_candidate_names):
        data.append(go.Scatter(
            x=dates,
            y=preCandidatesData[i],
            name=row,
            line=dict(
                color=config.colors[i],
                width=2)
            )
        )

    # Edit the layout
    layout = dict(title=config.monthlyGraphicsTitle,
                    xaxis=dict(title=config.monthlyGraphicsXaxis,
                        rangeselector=dict(
                            buttons=list([
                                dict(count=7,
                                     label='1 week',
                                     step='day',
                                     stepmode='backward'),
                                dict(count=1,
                                     label='1 month',
                                     step='month',
                                     stepmode='backward'),
                                dict(step='all')
                            ])
                        ),
                        rangeslider=dict(),
                        type='date'
                    ),
                    yaxis=dict(title=config.monthlyGraphicsYaxis),
                    )

    # Plot and embed in ipython notebook!
    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='presidential-candidates-monthly-report')