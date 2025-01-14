# Using the data pulled by ExtractEarthquakeData.py, create
# an interactive map that displays the earthquake locations.

# Your task is to create a map of earthquakes using that CSV
# file. The map should look like the file mapsample.jpg in __images__.

# Each earthquake is represented by a circle and the circle
# radius represents the magnitude of the earthquakes. When
# the user hovers the cursor over a circle, a popup shows the
# location description of the earthquake.

# Required libraries: requests, folium, streamlit, streamlit-folium


import requests
import folium
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
file_dir = os.path.join(script_dir, "appdata")
os.chdir(file_dir)

# Load the data from the CSV file (earthquake_data.csv)
data = pd.read_csv('earthquake_data.csv')

# Test print to verify structure
print(data.head())


# Create a map centered at the mean latitude and longitude
earthquake_map = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=3)

# Add a marker for each earthquake event
for index, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['Magnitude'] * 2,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.5,
        popup=f"Magnitude: {row['Magnitude']}"
    ).add_to(earthquake_map)
    
# Display the map

st.title("Earthquake Data Map")
st_folium(earthquake_map)
# Save the map to an HTML file
earthquake_map.save("earthquake_map.html")