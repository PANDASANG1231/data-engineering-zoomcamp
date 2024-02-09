rm -rf ./nytaxi_data
mkdir ./nytaxi_data

docker network create pg-network

docker run -itd \
    --name nytaxi \
    --network=pg-network \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=admin \
    -v ./nytaxi_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:14

docker run -itd \
    --name pgadmin \
    --network=pg-network \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="admin" \
    -p 80:80 \
    dpage/pgadmin4

python3 ingest_data.py --username admin --password admin --database_name nytaxi
