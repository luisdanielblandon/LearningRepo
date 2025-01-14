# The program scrapes the headlines of each post on the
# Hacker News website using requests and BeautifulSoup.
# The Hacker News URL is given below:
# https://news.ycombinator.com/

# The program, stores the headlines in a pandas dataframe.

# Then, it uses the textblob library to define the sentiment
# of each post headline (i.e., negative, neutral, or positive)
# and prints out the dataframe which contains the post headlines
# with the sentiment value next to them.

# Required libraries: requests, pandas, BeautifulSoup, textblob

import requests
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob

# URL of the website
url = 'https://news.ycombinator.com/'
print(url)


def get_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the post titles
    post_titles = soup.find_all('span', class_='titleline')
    
    # Create an empty list to store the headlines
    headlines = []
    
    # Loop through each post title and find the 'a' tag
    for title in post_titles:
        a_tag = title.find('a')
        if a_tag:
            headlines.append(a_tag.text)
    
    return headlines

# Get the headlines
headlines = get_headlines(url)
print(headlines)

# Set display options to prevent truncation
pd.set_option('display.max_colwidth', None)

# Create a pandas dataframe
df = pd.DataFrame(headlines, columns=['Headline'])

# Define a function to get the sentiment of each headline
def get_sentiment(headline):
    analysis = TextBlob(headline)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Add a new column to the dataframe with the sentiment value
df['Sentiment'] = df['Headline'].apply(get_sentiment)

# Apply left-justification to the 'Headline' column
df_styled = df.style.set_properties(subset=['Headline'], **{'text-align': 'left'})

# Print the dataframe
print(df_styled)