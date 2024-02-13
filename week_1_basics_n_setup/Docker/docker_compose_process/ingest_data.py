## Usage: python3 ingest_data.py --username admin --password admin --database_name nytaxi

import os
import argparse
import subprocess
import pandas as pd
from tqdm import tqdm
import urllib.request
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Create the parser
parser = argparse.ArgumentParser(description='Data ingestion program using argparse')

# Add an argument
parser.add_argument('--username', type=str, help='Postgre sql username, Type string', default='admin')
parser.add_argument('--password', type=str, help='Postgre sql password, Type string')
parser.add_argument('--host', type=str, help='Postgre sql url, Type string', default='localhost')
parser.add_argument('--port', type=str, help='Postgre sql port, Type string', default='5432')
parser.add_argument('--database_name', type=str, help='Database name, Type string', default='nytaxi')

# Parse the command line arguments
args = parser.parse_args()
username = args.username
password = args.password
host = args.host
port = args.port
database_name = args.database_name

# Create the connection string
connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'

# Create the PostgreSQL engine
engine = create_engine(connection_string)

# Create database if not existed
if not database_exists(engine.url):
    create_database(engine.url)

# Get data if not downloaded
if not os.path.exists("yellow_tripdata_2021-01.csv.gz"):

    # Download data if it is not existed
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
    urllib.request.urlretrieve(url, "yellow_tripdata_2021-01.csv.gz")
    
    # Read data and unzip data
    df = pd.read_csv("yellow_tripdata_2021-01.csv.gz", compression="gzip", header=0, sep=",", quotechar='"', low_memory=False)

    # Remove and save the csv
    os.remove("yellow_tripdata_2021-01.csv.gz")
    df.to_csv("yellow_tripdata_2021-01.csv", index=False)

# Ingest data into postgre sql
b_output = subprocess.check_output(["wc", "-l", "yellow_tripdata_2021-01.csv"])
s_output = str(b_output).strip("b'").split(" ")[0]
shape = int(s_output)

data_chunk_iters = pd.read_csv("yellow_tripdata_2021-01.csv", chunksize=1000)

for chunk in tqdm(data_chunk_iters, total=round(shape/1000)):
    chunk.tpep_pickup_datetime = pd.to_datetime(chunk.tpep_pickup_datetime)
    chunk.tpep_dropoff_datetime = pd.to_datetime(chunk.tpep_dropoff_datetime)
    chunk.to_sql(name="taxi_drip", con=engine, if_exists="append", index=False)

# Remove original csv file 
os.system("rm -r yellow_tripdata_2021-01.csv")