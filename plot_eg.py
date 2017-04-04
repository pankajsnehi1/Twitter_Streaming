'''import numpy as np
import matplotlib.pyplot as plt

t1 = [0,1,2,3,4]
t2 = [0,2,4,9,16]
t3 = [0,4,8,]

plt.figure(1)
plt.plot(t1, t2, 'bo', t1, t2, "r--")

plt.show()'''

'''import csv
import glob
import os

companies_code = csv.reader(open('companies_with_stock_code.csv', 'r'))

path_for_folder = '/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores'

for row in (companies_code):
    senti_score=[]
    for filename in glob.glob(os.path.join(path_for_folder, '*.csv')):
        file = csv.reader(open(filename, 'r'))
        for line in file:
            name, score = line[0], line[1]
            if name == row[0]:
                senti_score.append(int(score))
    print('Senti score for', row[0], 'is', senti_score)'''