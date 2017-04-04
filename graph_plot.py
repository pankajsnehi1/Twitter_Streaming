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
        #share price matrix in df format
        price_matrix = web.DataReader('LON:%s' %company_code, 'google', start_date, end_date)

        for row in price_matrix.itertuples(index=True, name='Pandas'):
            daily_average = 0
            daily_average = (getattr(row, 'Open') + getattr(row, 'Close') + getattr(row, 'Low') +
                             getattr(row, 'High')) / 4.0
            price_matrix.set_value(row.Index, 'Day Average', float(daily_average))
    except:
        pass
    # returns the average share price for the day, could be changed to return the full data
    return (price_matrix['Day Average'])


# gets the twitter sentiment score for a company
def get_senti_score(company_name):
    path_for_folder = '/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores'
    senti_score=[]
    # reads all the file in a directory to collate the score for the company
    for filename in glob.glob(os.path.join(path_for_folder, '*.csv')):
        file = csv.reader(open(filename, 'r'))
        for line in file:
            name, score = line[0], line[1]
            # checks if the name's score in every file it looks through in the dir
            if name == company_name:
                senti_score.append(int(score))
    return (senti_score)

# company's business name
company_name = 'Aviva'

# company's trading name
company_code = 'AV.'

# df for the plot
new_df = pd.DataFrame({company_name:get_share_price(company_code,'2017/03/14','2017/04/01'),
                       'Twitter Sentiment': get_senti_score(company_name)})

new_df.plot()
plt.show()