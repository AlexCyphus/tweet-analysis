"""[Sentiment Analysis; 20 points] Using TextBlob, calculate the polarity and
subjectivity scores for each tweet in the 7.2K+7.2K tweet corpus.
Summarize the calculated scores with histograms using Matplotlib,
where X-axis is the score and Y-axis is the tweet count in the score bin.
Also, provide the average of the polarity and subjectivity scores for each keyword."""

import os
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

#changes directory to where data is stored
os.chdir("../data")

#returns list of all files in directory
all_files = os.listdir()

# collects data for keyword
def sentiment_data(keyword):

    #lists to be populated
    subjectivity = []
    polarity = []

    #iterate through the files and match keyword
    for file in all_files:
        if file.split('-')[4].split('.')[0] == keyword:
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
        plt.title("{}\'s {}".format(keyword.capitalize(), string_type.capitalize()))
        plt.show()

    #return two histograms and averages
    make_histogram(subjectivity, "subjectivity")
    make_histogram(polarity, "polarity")
    print("\n{}\'s average for subjectivity is {} and the average for polarity is {}\n".format(keyword.capitalize(), subjectivity_average,polarity_average))

sentiment_data('amazon')
sentiment_data('walmart')
