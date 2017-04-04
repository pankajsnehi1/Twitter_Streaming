'''import csv
import glob
import os
import csv
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd

companies_code = csv.reader(open('companies_with_stock_code.csv', 'r'))

path_for_folder = '/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores'


#for row in (companies_code):
try:
    print("For Barclays")
    price_matrix = web.DataReader('LON:BARC', 'google', '2017/3/14', '2017/4/01')

    for row in price_matrix.itertuples(index=True, name='Pandas'):
        daily_average = 0
        daily_average = (getattr(row, 'Open') + getattr(row, 'Close') + getattr(row, 'Low') +
                         getattr(row, 'High')) / 4.0
        price_matrix.set_value(row.Index, 'Day Average', float(daily_average))
except:
    pass

senti_score=[]
for filename in glob.glob(os.path.join(path_for_folder, '*.csv')):
    file = csv.reader(open(filename, 'r'))
    for line in file:
        name, score = line[0], line[1]
        if name == 'Barclays':
            senti_score.append(int(score))

print(price_matrix['Day Average'])
print('Senti score for Barc is', senti_score)
#plt.plot(price_matrix['Day Average'],senti_score)

new_df = pd.DataFrame({'BARC':price_matrix['Day Average'], 'Twitter Sentiment': senti_score})

plt.figure()
new_df.plot()
plt.show()'''

import matplotlib
import matplotlib.transforms
from pylab import figure, show

# New enough versions have offset_copy by Eric Firing:
if 'offset_copy' in dir(matplotlib.transforms):
 from matplotlib.transforms import offset_copy
 def offset(ax, x, y):
     return offset_copy(ax.transData, x=x, y=y, units='dots')
else: # Without offset_copy we have to do some black transform magic
 from matplotlib.transforms import blend_xy_sep_transform, identity_transform
 def offset(ax, x, y):
     # This trick makes a shallow copy of ax.transData (but fails for polar plots):
     trans = blend_xy_sep_transform(ax.transData, ax.transData)
     # Now we set the offset in pixels
     trans.set_offset((x,y), identity_transform())
     return trans

fig=figure()
ax=fig.add_subplot(111)

# plot some data
x = (3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3)
y = (2,7,1,8,2,8,1,8,2,8,4,5,9,0,4,5)
ax.plot(x,y,'.')

 # add labels
trans=offset(ax, 10, 5)
for a,b in zip(x,y):
    ax.text(a, b, '(%d,%d)'%(a,b), transform=trans)

show()