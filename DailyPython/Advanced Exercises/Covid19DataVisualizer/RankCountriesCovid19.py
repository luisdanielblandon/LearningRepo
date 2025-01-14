# Import all data from appdata/covid19data.csv. Sum all the
# cases for each country (row). Output the list of top 10
# countries by # of Covid cases.

# Required libraries: pandas, csv

import pandas as pd
import csv
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

def rank_countries_by_covid19_cases():
    # Load the data from the CSV file
    data = pd.read_csv(os.path.join(script_dir, 'appdata/covid19data.csv'))
    print("Original Data:")
    print(data.head())
    
    # Set the "Country/Region" column as the key
    data = data.set_index('Country/Region')
    
    # Set display options to prevent truncation of numbers
    pd.set_option('display.float_format', '{:,.0f}'.format)
    
    # Pull the value from the right-most cell for each row
    data['Total Cases'] = data.iloc[:, -1]
    
    # Sort the data by total cases in descending order
    data = data.sort_values(by='Total Cases', ascending=False)
    
    # Print the top 10 countries
    print("Top 10 Countries by Total Covid Cases:")
    print(data[['Total Cases']].head(10))

# Call the function to execute it
rank_countries_by_covid19_cases()