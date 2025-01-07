#Started 11:09AM

import pdfkit
import os

#Function to read URLs from a file and return a clean list of URLs
def read_urls_from_file(file_path):
      try:
            with open(file_path, 'r') as file:
                  url_list = file.readlines()
            # Strip any extra whitespace characters (like newlines) from each name
            url_list = [url.strip() for url in url_list]
            return url_list
      except FileNotFoundError:
            print(f"The file at {file_path} was not found.")
            return []
      except Exception as e:
            print(f"An error occurred: {e}")
            return []

#Function to sanitize URLs for use as filenames     
def sanitize_url(url):
            return url.replace("://", "_").replace("/", "_").replace(".", "_")
      


# Define location of the txt file with list of URLs for conversion
script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, '722_url_list.txt')
url_list = read_urls_from_file(file_path)


# Loop thru export function to save each URL as a PDF
for url in url_list:
      # Use the sanitize_url function to create a safe filename
      sanitized_url = sanitize_url(url)
      # Define output file path
      output_file = os.path.join(script_dir, f'{sanitized_url}.pdf')
      # Convert the URL to a PDF
      pdfkit.from_url(url, output_file)
      # Print the results upon success
      print(f'Webpage saved as PDF: {output_file}')
      

      
print("\nFinished converting all URLs to PDFs.")

#Paused at 11:30AM to shit

#Resumed at 11:33AM to finish

#Finished at 11:42AM

#Total time: 30 minutes