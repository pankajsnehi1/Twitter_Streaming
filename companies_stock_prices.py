import csv
import pandas_datareader.data as web

companies_code = csv.reader(open('companies_with_stock_code.csv', 'r'))

for row in (companies_code):
    try:
        print("For %s :" % row[0])
        price_matrix = web.DataReader('LON:%s' % row[1], 'google', '2017/3/14', '2017/4/01')

        for row in price_matrix.itertuples(index=True, name='Pandas'):
            daily_average = 0
            daily_average = (getattr(row, 'Open') + getattr(row, 'Close') + getattr(row, 'Low') +
                             getattr(row, 'High')) / 4.0
            price_matrix.set_value(row.Index, 'Day Average', float(daily_average))
        print (price_matrix['Day Average'])

    except:
        pass