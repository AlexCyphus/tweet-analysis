import os
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

def get_files(keyword,day = 0):
    os.chdir("../data")
    all_files = os.listdir()
    return_files = []
    if day == 0:
        for file in all_files:
            if file.split('-')[4].split('.')[0] == keyword:
                return_files.append(file)
            if len(return_files) == 72:
                break
        return return_files
    else:
        for file in all_files:
            if (file.split('-')[4].split('.')[0] == keyword) and (int(file.split("-")[2]) == day):
                return_files.append(file)
        return return_files

#Amazon Data
amazon_day_1 = get_files('amazon', 27)
amazon_day_2 = get_files('amazon', 28)
amazon_day_3 = get_files('amazon', 29)

#Walmart Data
walmart_day_1 = get_files('walmart', 27)
walmart_day_2 = get_files('walmart', 28)
walmart_day_3 = get_files('walmart', 29)

# collects data for keyword
def sentiment_data(keyword, files):

    #lists to be populated
    subjectivity = []
    polarity = []

    #iterate through the files and match keyword
    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
        #iterate through tweets in file and add sentiment to lists
        for x in range(len(data)):
            tweet = TextBlob(data[x]['text'])
            polarity.append(tweet.sentiment.polarity) # gives polarity
            subjectivity.append(tweet.sentiment.subjectivity) #gives subjectivity

    #calculate averages
    subjectivity_average = sum(subjectivity)/len(subjectivity)
    polarity_average = sum(polarity)/len(polarity)

    #make histogram code inspired by https://realpython.com/python-histograms/
    def make_histogram(type, string_type):
        n, bins, patches = plt.hist(x=type, bins='auto', color='#b00b00')
        plt.grid(axis='y', alpha=1,)
        plt.xlabel('Score')
        plt.ylabel('Frequency')
        plt.title("{}\'s {}".format(keyword, string_type.capitalize()))
        plt.show()

    #return two histograms and averages
    make_histogram(subjectivity, "subjectivity")
    make_histogram(polarity, "polarity")
    print("\n{} average for subjectivity is {} and the average for polarity is {}\n".format(keyword.capitalize(), subjectivity_average,polarity_average))

#amazon_data
sentiment_data('Amazon\'s Day 1', walmart_day_1)
sentiment_data('Amazon\'s Day 2', walmart_day_2)
sentiment_data('Amazon\'s Day 3', walmart_day_3)

#walmart data
sentiment_data('Walmart\'s Day 1', walmart_day_1)
sentiment_data('Walmart\'s Day 2', walmart_day_2)
sentiment_data('Walmart\'s Day 3', walmart_day_3)
