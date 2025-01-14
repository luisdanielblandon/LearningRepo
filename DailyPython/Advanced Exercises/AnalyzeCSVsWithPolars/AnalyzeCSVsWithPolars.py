# (1) The program makes a list of all the CSV files located
# in the “invoices” directory.
# (2) Then, the program iterates over the files and loads
# each file as a Polars dataframe.
# (3) The program calculates the total of the “Price” column of each file.
# (4) It also counts the total number of invoices for each file.
# (5) Then, the program prints the total price and the
# number of invoices for each file.
# (3) Then, the program calculates the total sum spent by each customer in
# all files and ranks the customers by the amount they have spent.
# (7) The dataframe created in step 2 is exported to a CSV file and a message
# is printed out in the command line that the report was saved successfully.
# (8) The program ends.

import polars as pl
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

def analyze_csvs_with_polars():
      # (1) The program makes a list of all the CSV files located
      # in the “invoices” directory.
      invoices_dir = os.path.join(script_dir,'appdata')
      print(invoices_dir)
      files = os.listdir(invoices_dir)
      print(files)
      csv_files = [f for f in files if f.endswith(".csv")]
      
      # (2) Then, the program iterates over the files and loads
      # each file as a Polars dataframe.
      for file in csv_files:
            df = pl.read_csv(f"{invoices_dir}/{file}")
      
            # (3) The program calculates the total of the “Price” column of each file.
            total_price = df["Total Price"].sum()
      
            # (4) It also counts the total number of invoices for each file.
            total_invoices = df.shape[0]
      
            # (5) Then, the program prints the total price and the
            # number of invoices for each file.
            print(f"File: {file}, Total Price: {total_price}, Total Invoices: {total_invoices}")
            
            # (6) Then, the program calculates the total sum spent by each customer in
            # all files and ranks the customers by the amount they have spent.
            customer_totals = df.group_by('Customer Name').agg(pl.sum('Total Price').alias('Total Spent'))
            customer_totals = customer_totals.sort('Total Spent', descending=True)
            print(customer_totals)
            
            # (7) The dataframe created in step 2 is exported to a CSV file and a message
            # is printed out in the command line that the report was saved successfully.
            df.write_csv(f"{invoices_dir}/{file}_report.csv")
            print(f"Report for {file} saved successfully.")
            
# (8) The program ends.
analyze_csvs_with_polars()