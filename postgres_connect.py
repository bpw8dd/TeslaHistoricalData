# =============================================================================
# This file establishes a connection with Postgres,
# creates a table for Tesla Historical Quotes if it does
# not already exists, and loads data into the database 
# using a .csv file pulled from online.
# =============================================================================

import psycopg2

# =============================================================================
# Connecting to Postgres DB involves 3 parameters:
#         1) specify hostname where Postgres server is running 
#             (locally, in this case)
#         2) Pass in database name (postgres in this case because
#              of default installation)
#         3) Pass in username
# =============================================================================
try:
    connection = psycopg2.connect(
            host="localhost", 
            dbname="postgres",
            user="postgres", 
            password="Bathtub615")
    
    table_exists = True
    data_inserted = True
# Cursor created by connection object and lets us execute SQL commands
    cursor = connection.cursor()
    
    # Create initial table
    if (table_exists == False):
        cursor.execute("""CREATE TABLE teslaquotes(
        date text PRIMARY KEY,
        close float,
        volume integer,
        open float,
        high float,
        low float)""")
        connection.commit()
        #   table_exists = True
    
    # Load tesla historical data into Postgres
    if (data_inserted == False):
        with open('HistoricalQuotes.csv', 'r') as f:
            #skip the header row
            next(f)
            cursor.copy_from(f, 'teslaquotes', sep=',')
            connection.commit()
        #   data_inserted = True
    
    # Check if inserted by reading from table
    if (data_inserted == True):
        cursor.execute('SELECT * FROM teslaquotes')
        quotes = cursor.fetchall()
        print(quotes)
        
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)



