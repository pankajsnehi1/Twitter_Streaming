import glob
import os
import csv
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd

# for if all the company's graphs need returned
# companies_code = csv.reader(open('companies_with_stock_code.csv', 'r'))


# gets the share price given company's code, start date and end date
def get_share_price(company_code, start_date, end_date):
    try:
        # share price matrix in df format
        price_matrix = web.DataReader('LON:%s' %company_code, 'google', start_date, end_date)

        for row in price_matrix.itertuples(index=True, name='Pandas'):
            daily_average = 0
            daily_average = (getattr(row, 'Open') + getattr(row, 'Close') + getattr(row, 'Low') +
                             getattr(row, 'High')) / 4.0
            price_matrix.set_value(row.Index, 'Day Average', float(daily_average))
    except:
        pass
    # returns the average share price for the day, could be changed to return the full data
    return price_matrix['Day Average']


# gets the twitter sentiment score for a company
def get_senti_score(company_name):
    path_for_folder = '/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores_affinn/sentiment_score_one_affinn'
    senti_score=[]
    # reads all the file in a directory to collate the score for the company
    for filename in glob.glob(os.path.join(path_for_folder, '*.csv')):
        file = csv.reader(open(filename, 'r'))
        for line in file:
            name, score = line[0], line[1]
            # checks if the name's score in every file it looks through in the dir
            if name == company_name:
                score = float('%.1f' % round(float(score),1))
                senti_score.append(score)
    return senti_score


# shows a simple graph for company's share price and twitter sentiment movement
def plot_share_vs_sentiment(company_name, company_code, start_date, end_date):

    # df for the plot
    new_df = pd.DataFrame({company_name:get_share_price(company_code,start_date,end_date),
                           'Twitter Sentiment': get_senti_score(company_name)})
    new_df.plot()
    plt.show()


# normalises the graphs should one has higher value than the other
def plot_normalised_graph(company_name, company_code, start_date, end_date):
    sentiment_score = get_senti_score(company_name)
    share_price = get_share_price(company_code, start_date, end_date)
    new_df = pd.DataFrame({company_name: share_price, 'Twitter Sentiment': sentiment_score})

    sum_of_share_prices = 0
    sum_of_sentiment_scores = 0
    counter = 0

    for index, row in new_df.iterrows():
        sum_of_share_prices += row[company_name]
        sum_of_sentiment_scores += row['Twitter Sentiment']
        counter = counter + 1

    if sum_of_share_prices > sum_of_sentiment_scores:
        share_average = sum_of_share_prices / counter
        sentiment_average = sum_of_sentiment_scores / counter
        difference = share_average - sentiment_average
        print (difference)
        for index, row in new_df.iterrows():
            new_df.set_value(index, 'Twitter Sentiment', row['Twitter Sentiment'] + difference)
    else:
        sentiment_average = sum_of_sentiment_scores / counter
        share_average = sum_of_share_prices / counter
        difference = sentiment_average - share_average
        for index, row in new_df.iterrows():
            new_df.set_value(index, company_name, row[company_name] + difference)

    new_df.plot()
    plt.show()


#plot_share_vs_sentiment('Aviva', 'AV.', '2017/03/14', '2017/04/06')

plot_normalised_graph('Aviva', 'AV.', '2017/03/14', '2017/04/06')