# Your task for this project is to create a Python script that stores various system metrics any time it is executed.

# The program should make use of the psutil library to store various computer metrics in a CSV file. Here is what the CSV file should look like:

# (2) When the script is executed for the first time it creates a CSV file, adds a header (i.e., timestamp, cpu_usage, etc.), measures the metrics, and adds those metrics as a row of data in the CSV. (3) When the script is executed for the second time, it adds a new row with data in the existing CSV file. (4) Any time the script is executed, a new row with data is stored. (5) Optionally, upload the script to a service such as PythonAnywhere.com to schedule it for execution at a certain time every day.

# Required libraries: psutil, csv, os, datetime


import psutil
import csv
import os
import datetime

# Create a function that will store the system metrics in a CSV file
def store_system_metrics():
    # Define the file name
    file_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(file_path,'metricslogs/system_metrics.csv')
    
    # Define the header
    header = ['timestamp', 'cpu_usage', 'memory_usage', 'disk_usage']
    
    # Check if the file exists
    if not os.path.exists(file_name):
        # If the file does not exist, create it and write the header
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
    
    # Get the current timestamp
    timestamp = datetime.datetime.now()
    
    # Get the CPU usage
    cpu_usage = psutil.cpu_percent()
    
    # Get the memory usage
    memory_usage = psutil.virtual_memory().percent
    
    # Get the disk usage
    disk_usage = psutil.disk_usage('/').percent
    
    # Create a list with the metrics
    metrics = [timestamp, cpu_usage, memory_usage, disk_usage]
    
    iterator = 0
    
    # Print the metrics to the console
    for metric in metrics:
        print(header[iterator])
        print(metric,'\n')
        iterator += 1
    
    # Append the metrics to the CSV file
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(metrics)
        
# Call the function to store the system metrics
store_system_metrics()