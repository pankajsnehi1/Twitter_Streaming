import tweepy
import sys
import jsonpickle
import json
import csv
import os, datetime


consumer_key = "l3m0ZysbUSq68ijZ8YiyaQlcs"
consumer_secret = "jpozK0XzVNyZWGMLQelxwzbuhK5y9ovQ4tbxgFYA6p0uS1cHWW"

#API Keys for authentication
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

#after 15 minutes of API pause windows, the program restarts
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print("Can't Authenticate")
    sys.exit(-1)

#creating a folder to store tweets for a specific day
path_for_folder = r'/Users/Pankaj/PycharmProjects/untitled/tweets_from_BT_test_test'

#to remove retweets ensuring our data has unique tweets
retweet_filter='-filter:retweets'

fName = 'BT_tweets.txt' # We'll store the tweets in a text file.
searchQuery = '@BTGroup'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = 0

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
if not os.path.exists(path_for_folder):
    os.makedirs(path_for_folder)
    with open(fName, 'w') as f:
        while tweetCount < maxTweets:
            try:

                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery+retweet_filter, count=tweetsPerQry)
                    else:
                        new_tweets = api.search(q=searchQuery+retweet_filter, count=tweetsPerQry,
                                                since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery+retweet_filter, count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=searchQuery+retweet_filter, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    #print(tweet.created_at)
                    if (tweet.created_at > datetime.datetime(2017, 3, 22, 00, 00, 00) and
                                tweet.created_at < datetime.datetime(2017, 3, 22, 23, 59, 00)):
                        print(tweet.created_at)
                    #print(json.loads(jsonpickle.encode(tweet._json, unpicklable=False))["text"])
                    #f.write(json.loads(jsonpickle.encode(tweet._json, unpicklable=False))["text"] + \n')
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break

    print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))