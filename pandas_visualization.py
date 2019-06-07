import psycopg2 as pg
import pandas.io.sql as psql
import plotly.graph_objs as go
import plotly 
from plotly.offline import init_notebook_mode, plot

plotly.tools.set_credentials_file(username='bpw8dd', api_key='H5XDEUc9KdVm8ZTQJ1Np')
init_notebook_mode(connected=True)

try:
    connection = pg.connect(
            host="localhost", 
            dbname="postgres",
            user="postgres", 
            password="*******")

    # Instantiate dataframe object with SQL table query
    df = psql.read_sql("SELECT * FROM teslaquotes", connection)
        
    # Set parameters of Candlestick plot
    trace = go.Candlestick(
            x=df['date'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close']
            )
    
    data = [trace]
    
    # Generates an offline candlestick graph using
    # the last 3 months of Tesla Data
    # Interactive; Can view the high,low,open,close
    # for each date on the x-axis
    # If open > close, the candlestick is red, and green 
    # if vice versa
    plot(data, filename='simple_candlestick.html')
    
except (Exception, pg.Error) as error:
    print ("Error while connecting to PostgreSQL", error)