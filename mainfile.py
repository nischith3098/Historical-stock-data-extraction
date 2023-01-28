#importing all the necessary libraries
import yfinance as yf
import config as cf
import pandas as pd
import sqlite3
import os

def main_db():
#creating an empty dictionary
    data = {}

#Creating the database 
    conn = sqlite3.connect(cf.path) 
    cursor = conn.cursor()

#Enabling the foreign key constraint. This is done to establish the database connection.
    conn.execute("PRAGMA foreign_keys = 1")

#Craeting table
    conn.execute("DROP TABLE IF EXISTS historical_data" )
    conn.execute("""CREATE TABLE historical_data
    (SLno INTEGER PRIMARY KEY, company varchar(225),Date date, Open float, High float, 
    Low float, Close float,Volume float)""")

#Iterating through the list of companies
    for company in cf.companies:

#Retreving the historical data for each company present in the list of companies
        hist = yf.download(company, start = '2020-01-01', end = '2021-01-01')
        data[company] = hist
        
        # Loop through the rows in the historical data
        for index, row in hist.iterrows():
        # Insert the data into the sqllite table
            cursor.execute("INSERT OR REPLACE INTO historical_data (company, Date ,Open, High ,Low , Close, Volume) \
            VALUES (?,?,?,?,?,?,?)", (company, index.date(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume']))
            

    # Commit the changes to the database    
    conn.commit()


    cursor.execute("SELECT * FROM historical_data")
    all_data = cursor.fetchall()
    #print(all_data)
    columns = ['SLno','company','Date','Open','High','Low','Close','Volume']
    table = pd.DataFrame(all_data, columns=columns)
    # Close the database connection
    conn.close()
    return "Table created and updated successfully"