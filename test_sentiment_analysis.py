from textblob import TextBlob
from nltk.tokenize import WhitespaceTokenizer
import re

#loading the AFFINN score
def get_affinn_scores(file='AFINN-111.txt'):
    affinn_file = open(file)
    scores = {}
    for line in (affinn_file):
        term, score = (line.split("\t"))
        scores[term] = int(score)
    return scores

affin_score = get_affinn_scores()

file = open ('Tesco_tweets.txt', 'r')
final_score = 0
ws_tok = WhitespaceTokenizer()
for line in (file.readlines()):

     #removing links from the text
     line = re.sub(r"http\S+", "", line)
     text = TextBlob(line)

     #correcting the spellings
     line = str(text.correct())

     #lemmatization
     for word in (text.words):
         word.lemmatize()

     #print (ws_tok.tokenize(line))
     words = ws_tok.tokenize(line)
     scores = 0
     for w in words:
         if w.lower() in affin_score:
             scores += affin_score[w.lower()]
     print(scores)
     final_score += scores

print ("Final score:", final_score)


