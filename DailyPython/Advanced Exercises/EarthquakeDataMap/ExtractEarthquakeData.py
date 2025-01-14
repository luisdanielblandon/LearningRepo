# you are expected to use Python to access the United States Geological Survey
# free API and download real-time earthquake events.

# API endpoint:
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson


# Export the data to a CSV file with the following columns:
# Magnitude (highlighted), Time, Location, Latitude, Longitude, Depth

# Import the libraries
import requests
import pandas as pd
import os

# API endpoint
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

script_dir = os.path.dirname(os.path.realpath(__file__))
file_dir = os.path.join(script_dir, "appdata")
os.chdir(file_dir)

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data
    data = response.json()
    
    # Extract the earthquake events
    earthquakes = data["features"]
    print(data["features"])
    
    # Initialize an empty list to store the earthquake data
    earthquake_data = []
    
    # Extract the required data from each earthquake event
    for event in earthquakes:
        properties = event['properties']
        points = event['geometry']
        magnitude = properties['mag']
        time = properties['time']
        latitude = points['coordinates'][1]
        longitude = points['coordinates'][0]
        
        # Append the data to the list
        earthquake_data.append([magnitude, time, latitude, longitude])
    
    # Create a DataFrame from the list of earthquake data
    df = pd.DataFrame(earthquake_data, columns=["Magnitude", "Time", "Latitude", "Longitude"])
    
    # Export the data to a CSV file
    df.to_csv("earthquake_data.csv", index=False)
    
    print("Data exported to earthquake_data.csv")
else:
    print(f"Failed to retrieve data: {response.status_code}")