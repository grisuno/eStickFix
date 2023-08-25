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


eStickFix/
|-- config/
| |-- config1.yaml
| |-- config2.yaml
|-- etl/
| |-- dataset1/
| | |-- table1/
| | | |-- ...
| | |-- table2/
| | |-- ...
| |-- dataset2/
| | |-- ...
|-- transformation/
| |-- dataset1/
| | |-- table1/
| | | |-- ...
| | |-- table2/
| | |-- ...
| |-- dataset2/
| | |-- ...
|-- qa/
| |-- dataset1/
| | |-- table1/
| | | |-- ...
| | |-- table2/
| | |-- ...
| |-- dataset2/
| | |-- ...
|-- log/
|-- data_navigation.py
|-- etl.py

## Getting Started

1. Clone this repository to your local machine.
2. Install the required Python libraries using `pip`:

pip install pyyaml watchdog pandas pymongo


3. Customize configuration files (`config1.yaml`, `config2.yaml`, etc.) in the `config` directory with your specific dataset, table, and date configurations. Example:

    date_now: "2023-08-25"
    dataset: "my_dataset1"
    tablename: "my_table1"

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


