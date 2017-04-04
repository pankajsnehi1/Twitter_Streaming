import os
import csv
import glob
from textblob import TextBlob
from nltk.tokenize import WhitespaceTokenizer
import re

# path_for_folder = r'/Users/Pankaj/PycharmProjects/untitled/tweets_from_31-Mar'

'''with open('/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores_textblob/01-Apr_Final_Score.csv',
          'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    if os.path.exists(path_for_folder):
        for filename in glob.glob(os.path.join(path_for_folder, '*.txt')):'''

filename = '/Users/Pankaj/PycharmProjects/untitled/spare_tweets/Tesco_tweets.txt'

#  to store final sentiment score for a company
final_score = 0

# if file size is 0 then add name and score
'''if (not os.path.getsize(filename)):

    # writing the score with name of the company
    #writer.writerow([filename[58:-11],final_score])
else:'''
file = open(filename, 'r')

# initialising the tokensier

positive_score=0
negative_score=0
neutral_score=0

for line in (file.readlines()):

    # removing links from the text
    line = re.sub(r"http\S+", "", line)
    text = TextBlob(line)

    # lemmatisation
    for word in (text.words):
        word.lemmatize()

    scores = 0


    scores = text.sentiment.polarity
    print(scores)

    if (scores > 0):
        positive_score += scores

    elif (scores < 0):
        negative_score += scores

    else:
        neutral_score += scores

    final_score += scores


print("Positive sentiment: ", positive_score)

print("Negative sentiment: ", negative_score)

print("Neutral sentiment: ", neutral_score)



senti_score_one = positive_score/final_score

senti_score_two = positive_score/(positive_score+negative_score)

senti_score_three = positive_score-negative_score/final_score

print(senti_score_one, senti_score_two, senti_score_three)

print("Final score for :", filename, final_score)
                # writer.writerow([filename[58:-11], final_score])