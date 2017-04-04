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
    for line in (affinn_file):
        term, score = (line.split("\t"))
        scores[term] = int(score)
    return scores

affin_score = get_affinn_scores()

path_for_folder = r'/Users/Pankaj/PycharmProjects/untitled/tweets_from_01-Apr'

with open('/Users/Pankaj/PycharmProjects/untitled/tweets_sentiment_scores/01-Apr_Final_Score.csv',
          'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    if os.path.exists(path_for_folder):
        for filename in glob.glob(os.path.join(path_for_folder, '*.txt')):

            #  to store final sentiment score for a company
            final_score = 0

            # if filesize 0 then add name and score
            if (not os.path.getsize(filename)):

                # writing the score with name of the company
                writer.writerow([filename[58:-11],final_score])
            else:
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
                    for word in (text.words):
                        word.lemmatize()

                    # tokenising the tweets
                    words = ws_tok.tokenize(line)

                    #to store a word's individual sentiment(AFFINN score)
                    scores = 0

                    # calculating the sentiment scores
                    for w in words:
                        if w.lower() in affin_score:
                            scores += affin_score[w.lower()]
                    print(scores)
                    final_score += scores

                print("Final score for %s:", filename, final_score)
                writer.writerow([filename[58:-11], final_score])