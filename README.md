# eStickFix
eStickFix is a glue to your data and your datalake

eStickFix is a data processing and quality assurance framework for automating ETL (Extract, Transform, Load) processes from Parquet files to MongoDB, with support for multiple datasets and tables. It is designed to streamline data transformations and quality checks while providing a seamless integration with MongoDB for easy data storage and dashboard creation.

## Features

- Automated ETL process for multiple datasets and tables
- Transformation and quality check scripts for each dataset/table
- MongoDB integration for data storage and dashboard creation
- Data partitioning by date using the `date_now` field
- Data navigation module for easier access to stored data
- Log generation for load statuses and errors

## Project Structure

The project is organized as follows:

[code]
eStickFix/
|-- app/
|   |-- templates/
|   |   |-- index.html
|   |   |-- etl_status.html
|   |-- app.py
|-- config/
|   |-- config1.yaml
|   |-- config2.yaml
|-- data_navigation.py
|-- etl.py
|-- data_loader.py
|-- sources.yaml
|-- log/
|-- transformations/
|   |-- dataset1/
|   |   |-- table1/
|   |   |   |-- ...
|   |   |-- table2/
|   |       |-- ...
|   |-- dataset2/
|   |   |-- ...
|-- qa/
|   |-- dataset1/
|   |   |-- table1/
|   |   |   |-- ...
|   |   |-- table2/
|   |       |-- ...
|   |-- dataset2/
|   |   |-- ...
|-- static/  # Static assets for the web interface (CSS, JS, etc.)
|-- templates/  # HTML templates for the web interface
|-- venv/  # Virtual environment
|-- README.md
[/code]
## Getting Started

1. Clone this repository to your local machine.
2. Install the required Python libraries using `pip`:

pip install pyyaml watchdog pandas pymongo paramiko 

3. Customize configuration files (`config1.yaml`, `config2.yaml`, etc.) in the `config` directory with your specific dataset, table, and date configurations. Example:

    date_now: "2023-08-25"
    dataset: "my_dataset1"
    tablename: "my_table1"
   
3.1 Primero, creemos el archivo config/sources.yaml en el mismo directorio config de tu script:

       config/sources.yaml:

   
sources:
  - type: ftp
    path: /remote/path/to/ftp/directory
    protocol: sftp
    username: your_ftp_username
    password: your_ftp_password
    dataset: dataset1
    table_name: table1

  - type: mysql
    host: localhost
    port: 3306
    username: your_mysql_username
    password: your_mysql_password
    database: your_database_name
    table: your_table_name
    query: "SELECT * FROM your_table_name"
    dataset: dataset2
    table_name: table2


4. Fill in transformation and quality check scripts for each dataset/table in the `transformation` and `qa` directories.
5. Run the ETL process using:


python etl.py


## Usage

- The ETL process listens for incoming Parquet files in the `etl/dataset/table` directory structure defined in the configurations.
- Transformations are applied based on the scripts provided in the `transformation` directory.
- Data quality checks are performed using scripts from the `qa` directory.
- Processed data is stored in MongoDB, and load statuses/errors are logged.

## License

This project is licensed under the GPL V3


