"""
Kevin Chau
November 16th 2021
This program computes all the scores and number of tweets for each region
"""
def compute_tweets(tweets, keywords):

    #First try and except is for hard coding and storing all the possible values in the "Keywords File"
    try:
        keywordFile = open(keywords, "r", encoding='utf-8') #Opens the keywords file
        keyValue1 = []  #Creates a list and stores all possible values of a keyword
        keyValue2 = []
        keyValue3 = []
        keyValue4 = []
        keyValue5 = []
        keyValue6 = []
        keyValue7 = []
        keyValue8 = []
        keyValue9 = []
        keyValue10 = []
        eastScore = 0  #Stores the score for each region
        centralScore = 0
        mountainScore = 0
        pacificScore = 0
        eastTweets = 0 #Stores the tweets for each region
        centralTweets = 0
        mountainTweets = 0
        pacificTweets = 0
        eastTotalTweets = 0 #Stores the total number of tweets for each region
        pacificTotalTweets = 0
        centralTotalTweets = 0
        mountainTotalTweets = 0

        for keywordList in keywordFile: #Loop through the file
            keywordList = keywordList.rstrip('\n')
            listSplit = keywordList.split(',')  #Splits into list

            #Statements to check each values 1 through 10 and append them onto the new list
            if listSplit[1] == "1":
                keyValue1.append(listSplit[0])
            if listSplit[1] == "2":
                keyValue2.append(listSplit[0])
            if listSplit[1] == "3":
                keyValue3.append(listSplit[0])
            if listSplit[1] == "4":
                keyValue4.append(listSplit[0])
            if listSplit[1] == "5":
                keyValue5.append(listSplit[0])
            if listSplit[1] == "6":
                keyValue6.append(listSplit[0])
            if listSplit[1] == "7":
                keyValue7.append(listSplit[0])
            if listSplit[1] == "8":
                keyValue8.append(listSplit[0])
            if listSplit[1] == "9":
                keyValue9.append(listSplit[0])
            if listSplit[1] == "10":
                keyValue10.append(listSplit[0])

        keywordFile.close()  #Close the file

    except IOError: #Try and catch for files not found
        print("ERROR FILE COULD NOT BE FOUND")

    try:
        tweetsFile = open(tweets, "r", encoding='utf-8')
        for tweetList in tweetsFile:
            tweetList = tweetList.strip('''!()-[]{};:'"\,<>./?@#$%^&*_~''') #Remove any punctuation from the line
            tweetList = tweetList.lower() #Converts everything to lower case
            tweetList = tweetList.split()  #Splits the words

            lat = tweetList[0].rstrip(',') #
            lat = lat.lstrip('[') #Removes [
            latitude = float(lat) #Takes the latitude value and stores it

            long = tweetList[1].rstrip(']')
            longitude = float(long)  #Takes the longitude value and stores it

            tweet = tweetList[5:]  #Takes the tweets and stores it

            #COMPUTATIONS FOR THE EASTERN TIME ZONE
            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -67.4446574 and longitude >= -87.518395): #Checks the longitude and latitude
                eastTotalTweets += 1 #Counter for every total tweet
                for sentiment in tweet:
                    if sentiment in keyValue1:
                        eastScore += 1 #Happiness Score +1
                        eastTweets += 1 #Adds one for keyword tweets
                    elif sentiment in keyValue2:
                        eastScore += 2
                        eastTweets += 1
                    elif sentiment in keyValue3:
                        eastScore+= 3
                        eastTweets += 1
                    elif sentiment in keyValue4:
                        eastScore += 4
                        eastTweets += 1
                    elif sentiment in keyValue5:
                        eastScore += 5
                        eastTweets += 1
                    elif sentiment in keyValue6:
                        eastScore += 6
                        eastTweets += 1
                    elif sentiment in keyValue7:
                        eastScore += 7
                        eastTweets += 1
                    elif sentiment in keyValue8:
                        eastScore += 8
                        eastTweets += 1
                    elif sentiment in keyValue9:
                        eastScore += 9
                        eastTweets += 1
                    elif sentiment in keyValue10:
                        eastScore += 10
                        eastTweets += 1

            #COMPUTATIONS FOR THE CENTRAL TIME ZONE
            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -87.518395 and longitude >= -101.998892):
                centralTotalTweets += 1
                for sentiment in tweet:
                    if sentiment in keyValue1:
                        centralScore += 1
                        centralTweets += 1
                    elif sentiment in keyValue2:
                        centralScore += 2
                        centralTweets += 1
                    elif sentiment in keyValue3:
                        centralScore += 3
                        centralTweets += 1
                    elif sentiment in keyValue4:
                        centralScore += 4
                        centralTweets += 1
                    elif sentiment in keyValue5:
                        centralScore += 5
                        centralTweets += 1
                    elif sentiment in keyValue6:
                        centralScore += 6
                        centralTweets += 1
                    elif sentiment in keyValue7:
                        centralScore += 7
                        centralTweets += 1
                    elif sentiment in keyValue8:
                        centralScore += 8
                        centralTweets += 1
                    elif sentiment in keyValue9:
                        centralScore += 9
                        centralTweets += 1
                    elif sentiment in keyValue10:
                        centralScore += 10
                        centralTweets += 1

            #COMPUTATIONS FOR THE MOUNTAIN TIME ZONE
            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -101.998892 and longitude >= -115.236428):
                mountainTotalTweets += 1
                for sentiment in tweet:
                    if sentiment in keyValue1:
                        mountainScore += 1
                        mountainTweets += 1
                    elif sentiment in keyValue2:
                        mountainScore += 2
                        mountainTweets += 1
                    elif sentiment in keyValue3:
                        mountainScore += 3
                        mountainTweets += 1
                    elif sentiment in keyValue4:
                        mountainScore += 4
                        mountainTweets += 1
                    elif sentiment in keyValue5:
                        mountainScore += 5
                        mountainTweets += 1
                    elif sentiment in keyValue6:
                        mountainScore += 6
                        mountainTweets += 1
                    elif sentiment in keyValue7:
                        mountainScore += 7
                        mountainTweets += 1
                    elif sentiment in keyValue8:
                        mountainScore += 8
                        mountainTweets += 1
                    elif sentiment in keyValue9:
                        mountainScore += 9
                        mountainTweets += 1
                    elif sentiment in keyValue10:
                        mountainScore += 10
                        mountainTweets += 1

            #COMPUTATIONS FOR THE PACIFIC TIME ZONE
            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -115.236428 and longitude >= -125.242264):
                pacificTotalTweets += 1
                for sentiment in tweet:
                    if sentiment in keyValue1:
                        pacificScore += 1
                        pacificTweets += 1
                    elif sentiment in keyValue2:
                        pacificScore += 2
                        pacificTweets += 1
                    elif sentiment in keyValue3:
                        pacificScore += 3
                        pacificTweets += 1
                    elif sentiment in keyValue4:
                        pacificScore += 4
                        pacificTweets += 1
                    elif sentiment in keyValue5:
                        pacificScore += 5
                        pacificTweets += 1
                    elif sentiment in keyValue6:
                        pacificScore += 6
                        pacificTweets += 1
                    elif sentiment in keyValue7:
                        pacificScore += 7
                        pacificTweets += 1
                    elif sentiment in keyValue8:
                        pacificScore += 8
                        pacificTweets += 1
                    elif sentiment in keyValue9:
                        pacificScore += 9
                        pacificTweets += 1
                    elif sentiment in keyValue10:
                        pacificScore += 10
                        pacificTweets += 1


        if eastTweets == 0:  #Statement to check if there is 0
            easternTime = 0
        else:
            easternTime = eastScore / eastTweets
        if centralTweets == 0:
            centralTime = 0
        else:
            centralTime = centralScore / centralTweets
        if mountainTweets == 0:
            mountainTime = 0
        else:
            mountainTime = mountainScore / mountainTweets
        if pacificTweets == 0:
            pacificTime = 0
        else:
           pacificTime = pacificScore / pacificTweets

        #Display Information
        print("Eastern Region: Happiness Score: " + str(easternTime) + ", " + str(eastTweets) + " Keyword tweets, " + str(eastTotalTweets) + " tweets in total for the region")
        print("Central Region: Happiness Score: " + str(centralTime) + ", " + str(centralTweets) + " Keyword tweets, " + str(centralTotalTweets) + " tweets in total for the region")
        print("Mountain Region: Happiness Score: " + str(mountainTime) + ", " + str(mountainTweets) + " Keyword tweets, " + str(mountainTweets) + " tweets in total for the region")
        print("Pacific Region: Happiness Score: " + str(pacificTime) + ", " + str(pacificTweets) + " Keyword tweets, " + str(pacificTotalTweets) + " tweets in total for the region")
        tweetsFile.close()  # closes the file

    except IOError:
        print("ERROR FILE DOES NOT EXIST")
