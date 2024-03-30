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

- remove these
<p align="center">
  <a href="https://https://github.com/faishalfaye/airflowdocker">
    <img src="https://github.com/faishalfaye/airflowdocker/assets/55538047/b9e21e41-e4e7-4d7b-9cd8-b4840719e4d8" alt="Logo" width="725" height="300">
  </a>
  <a href="https://https://github.com/faishalfaye/airflowdocker">
    <img src="https://github.com/faishalfaye/airflowdocker/assets/55538047/24f56a31-dd5d-4075-9530-d59626671e14" alt="Logo" width="725" height="530">
  </a>
  
- add these
<p align="center">
  <a href="https://https://github.com/faishalfaye/airflowdocker">
    <img src="https://github.com/faishalfaye/airflowdocker/assets/55538047/4471ee17-62b3-4bf4-91ca-f74503bc4685" alt="Logo" width="1250" height="100">
  </a>
