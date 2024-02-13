rm -rf ./nytaxi_data
mkdir ./nytaxi_data

docker-compose up -d

pip install -r requirements.txt

python3 ingest_data.py --username admin --password admin --database_name postgre --port 5431