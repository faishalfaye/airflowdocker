# Running Airflow in Docker with a local MySql Database

  

I wanted to install Airflow 2.6.1 in Docker with a local MySql Database as backend

  

1. Install MySql

- sudo apt update

- sudo apt install mysql-server

- check if the mysql server is running with: sudo systemctl status mysql.service. if it isn't running yet, run: sudo systemctl start mysql.service

  

2. Setting up a MySQL Database

- sudo mysql or sudo mysql -u root -p

- CREATE DATABASE airflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

- CREATE USER 'airflow_user' IDENTIFIED BY 'airflow_pass';

- GRANT ALL PRIVILEGES ON airflow_db.* TO 'airflow_user';

  

3. Fetch docker-compose.yaml

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.1/docker-compose.yaml'

  

4. Edit docker-compose.yaml

- remove some lines
- 
