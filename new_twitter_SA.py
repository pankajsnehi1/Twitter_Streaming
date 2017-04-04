import tweepy
import sys
import jsonpickle
import json
import os

consumer_key = "l3m0ZysbUSq68ijZ8YiyaQlcs"
consumer_secret = "jpozK0XzVNyZWGMLQelxwzbuhK5y9ovQ4tbxgFYA6p0uS1cHWW"

#API Keys for authentication
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print("Can't Authenticate")
    sys.exit(-1)


path_for_folder = r'/Users/Pankaj/PycharmProjects/untitled/tweets_from_6366-Mar'

fName = 'dumtesco.txt' #We'll store the tweets in a text file.
searchQuery = '@tesco'  #this is what we're searching for
maxTweets = 100000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits

retweet_filter='-filter:retweets' #to remove RTs

# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = 0

until_date='2017-03-20'

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
if not os.path.exists(path_for_folder):
    os.makedirs(path_for_folder)
    with open(os.path.join(path_for_folder, fName), 'w') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery + retweet_filter, count=tweetsPerQry,
                                                until=until_date)
                    else:
                        new_tweets = api.search(q=searchQuery + retweet_filter, count=tweetsPerQry,
                                                since_id=sinceId, until=until_date)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery + retweet_filter, count=tweetsPerQry,
                                                max_id=str(max_id - 1), until=until_date)
                    else:
                        new_tweets = api.search(q=searchQuery + retweet_filter, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId, until=until_date)

                if not new_tweets:
                    print("No more tweets found")
                    break

                for tweet in new_tweets:
                    #print(type(tweet))
                    print(tweet.created_at)

                    #print (jsonpickle.encode(tweet._json, unpicklable=False)).text
                    f.write(json.loads(jsonpickle.encode(tweet._json, unpicklable=False))["text"] + '\n')
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                #max_id = new_tweets[-1].id

            except tweepy.TweepError as e:
                #Just exit if any error
                print("some error : " + str(e))
                break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))