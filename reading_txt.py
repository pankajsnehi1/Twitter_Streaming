import csv

reader = open('barclays_twitter_data.txt')

next = reader.readline()

while next != "":
    print (type(next))
    next = reader.readline()