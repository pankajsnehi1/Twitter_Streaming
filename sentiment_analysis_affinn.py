import os
import csv
import glob
from textblob import TextBlob
from nltk.tokenize import WhitespaceTokenizer
import re


# loading the AFFINN score
def get_affinn_scores(file='AFINN-111.txt'):
    affinn_file = open(file)
    scores = {}
    for line in affinn_file:
        term, score = (line.split("\t"))
        scores[term] = int(score)
    return scores

affin_score = get_affinn_scores()

path_for_folder = r'/Users/Pankaj/PycharmProjects/untitled/tweets_from_31-Mar'

sentiment_score_dict_one = {}
sentiment_score_dict_two = {}
sentiment_score_dict_three = {}

#  to store final sentiment score for a company
if os.path.exists(path_for_folder):
        for filename in glob.glob(os.path.join(path_for_folder, '*.txt')):

            final_score = 0
            positive_score = 0
            negative_score = 0
            neutral_score = 0

            file = open(filename, 'r')

            # initialising the tokensier
            ws_tok = WhitespaceTokenizer()
            for line in (file.readlines()):

                # removing links from the text
                line = re.sub(r"http\S+", "", line)
                text = TextBlob(line)

                # correcting the spellings, been commented as it takes very long
                # line = str(text.correct())

                # lemmatisation
                for word in text.words:
                    word.lemmatize()

                # tokenising the tweets
                words = ws_tok.tokenize(line)

                # to store a word's individual sentiment(AFFINN score)
                scores = 0

                # calculating the sentiment scores
                for w in words:
                    if w.lower() in affin_score:
                        scores += affin_score[w.lower()]
                if scores > 0:
                    positive_score += scores
                elif scores < 0:
                    negative_score += scores
                else:
                    neutral_score += scores

                final_score += scores

            try:

                senti_score_one = positive_score / final_score
                senti_score_two = positive_score / (positive_score + negative_score)
                senti_score_three = positive_score - negative_score / final_score

                sentiment_score_dict_one[filename[58:-11]] = senti_score_one
                sentiment_score_dict_two[filename[58:-11]] = senti_score_two
                sentiment_score_dict_three[filename[58:-11]] = senti_score_three

            # error occurs when file is empty, assigning that file to 0
            except ZeroDivisionError:

                sentiment_score_dict_one[filename[58:-11]] = 0
                sentiment_score_dict_two[filename[58:-11]] = 0
                sentiment_score_dict_three[filename[58:-11]] = 0

with open('/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores_affinn/'
          'sentiment_score_one_affinn/31-Mar_Final_Score.csv', 'wt') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in sorted(sentiment_score_dict_one.items()):
        writer.writerow([key, value])

with open('/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores_affinn/'
          'sentiment_score_two_affinn/31-Mar_Final_Score.csv', 'wt') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in sorted(sentiment_score_dict_two.items()):
        writer.writerow([key, value])

with open('/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores_affinn/'
          'sentiment_score_three_affinn/31-Mar_Final_Score.csv', 'wt') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in sorted(sentiment_score_dict_three.items()):
        writer.writerow([key, value])