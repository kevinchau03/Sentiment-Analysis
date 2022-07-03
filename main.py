'''
Author: Kevin Chau
Date: November 15th 2021
Desc: Program that takes all computations and displays for the user when they ask
'''

from sentiment_analysis import compute_tweets

tweetFile = input("Enter the tweet file (with the txt at the end) ") #Takes user input and opens the txt file
keywordFile = input("Enter the keyword file (with the txt at the end) ")
compute_tweets(tweetFile, keywordFile) #starts the compute_tweets function
