## Project Name: JSON to PostgreSQL ETL with pgAdmin and Email Notifications
### Project Overview
This project implements an ETL pipeline that extracts data from a JSON file, transforms it, and loads it into a PostgreSQL database. The pipeline is orchestrated using Apache Airflow, and it is containerized using Docker to provide an easily reproducible environment. Additionally, pgAdmin is included to manage the PostgreSQL database through a web-based interface. The project also provides email notifications in case of task failures.
### Airflow DAG Configuration (dags/etl_dag.py)
This DAG orchestrates the ETL process. The DAG runs the Python ETL script (etl.py) inside a container, which extracts data from the JSON file, transforms it, and loads it into PostgreSQL.
Schedule: Runs daily at 9:00 AM (configured in the DAG with schedule_interval='00 9 * * *').
Email Notifications: If a task fails, an email notification is sent.
![image](https://github.com/user-attachments/assets/1290b774-962e-4442-82cd-3b27a4c66d0f)
![image](https://github.com/user-attachments/assets/a3e028f8-b171-4c4c-a817-3996591e404c)


## ETL Script Description
This Python ETL script performs the following steps:

1- Extracts data from a JSON file (input.json).

2- Transforms the data by:
- Flattening any nested JSON structures into a tabular format using pandas.json_normalize (column-wise flattening).

- Extracting the latitude and longitude from the pickupAddress_geoLocation field into separate columns (lat, long).

- Removing unnecessary columns (pickupAddress_geoLocation, dropOffAddress_geoLocation).

3- Loads the transformed data into a PostgreSQL database (main database) using SQLAlchemy and pandas.to_sql.

The script connects to the PostgreSQL database, appends the transformed data to a table named deliveries, and ensures that the database is updated with new data from the JSON file.
![image](https://github.com/user-attachments/assets/f997b8ac-a804-4394-ab12-d8af9d7ddad2)

### pgAdmin description 
It provides a web-based interface for managing and interacting with the PostgreSQL database.

pgAdmin runs as a Docker container, and it's configured with environment variables for login credentials:

Username: admin@admin.com

Password: admin
![image](https://github.com/user-attachments/assets/7c2ec08c-0b41-413f-ad05-bff4f476165f)

### how to optimize SQL queries for better performance:
1-  Use Indexes on columns used frequently in WHERE, JOIN, ORDER BY, and GROUP BY clauses

2- Avoid SELECT *

3- Avoid using DISTINCT unless absolutely necessary

4- Use Materialized Views to store precomputed results and speed up query performance.

5- Optimize Data Types

6- Use the most efficient data types. For instance, use INTEGER instead of BIGINT if values are small, and avoid TEXT when VARCHAR(n) would suffice.

![ERP](https://github.com/user-attachments/assets/f525fcc0-5d59-4443-8803-348344ab3f9f)

