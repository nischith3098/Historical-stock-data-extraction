
//**mainfile.py**//

This script is used to scrape historical data from the yfinance package for multiple companies and store it in a SQLite database.

It starts by importing all the necessary libraries, including yfinance, config, pandas, and sqlite3. The config file is used to store the list of companies and the path to the SQLite database.

The main_db() function is then defined, which is used to create the SQLite database and store the historical data in it. The function starts by creating an empty dictionary called "data" and then creates a connection to the SQLite database using the path stored in the config file. It then enables the foreign key constraint, which is necessary to establish the database connection.

Next, the function creates a table called "historical_data" in the SQLite database, with columns for the company name, date, open price, high price, low price, close price, and volume. The function then iterates through the list of companies stored in the config file and uses the yfinance package to download the historical data for each company. The historical data is then stored in the "data" dictionary and inserted into the SQLite table using an "INSERT OR REPLACE" statement.

After all the historical data has been inserted into the table, the changes are committed to the database and the function retrieves all the data from the table and stores it in a pandas dataframe. The function then closes the database connection and returns a message indicating that the table was created and updated successfully.


//**apifile.py**//

This file is a Flask application that has several routes that allow the user to retrieve data from a historical_data table in a SQLite database. The database is connected to using the sqlite3 library and the path of the database file is imported from a separate config file. The routes include:

    "/get-all-data" - This route retrieves all the data from the historical_data table and returns it in JSON format.

    "/particular-day-data" - This route retrieves all the data for a particular date from the historical_data table. The date is passed as a query parameter in the URL. The data is returned in JSON format.

    "/particular-company-day-data" - This route retrieves all the data for a particular company and date from the historical_data table. The company and date are passed as query parameters in the URL. The data is returned in JSON format.

    "/particular-company-data" - This route retrieves all the data for a particular company from the historical_data table. The company is passed as a query parameter in the URL. The data is returned in JSON format.

    "/update-stock-company-data" - This route allows the user to update the stock data for a particular company and date in the historical_data table. The company, date, open price, high price, low price, close price, and volume are passed as form data in the request. The route returns a message indicating that the stock data was updated successfully.

    "/update-db" - This route calls a main_db() function from a separate mainfile module to update the historical_data table with new data.

The file also has two helper functions, db_connect() and db_close(), which are used to connect to and close the database connection respectively. The app.run() function is used to run the Flask application on a specified port with debug mode enabled.

//**config.py**//
This file consists the configuration file which has the list of companies and the creation of databases and its directory.
