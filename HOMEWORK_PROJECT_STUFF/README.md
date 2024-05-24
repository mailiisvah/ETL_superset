## Implementing an ETL Process and Data Visualization

The primary objective of this project was to implement an ETL (Extract, Transform, Load) pipeline to preprocess, transform, and load data from a public dataset into a data warehouse, and then visualize the data using Apache Superset. The dataset, titled "Tootuna arvele votmised kuu jooksul toetuste ja hyvitistega kaetuse ja maakonna ja soo ning vanusegrupi jargi.xlsx," contains information about new registered unemployed individuals in Estonia, categorized by date, county, gender, age group, and type of benefit or allowance.

Data Sources
The data for this project was sourced from the Estonian Open Data portal: https://avaandmed.eesti.ee/datasets/toetuste-ja-huvitistega-kaetus

NB! If you are wondering why there are some airquality and weather files in the repository, then just ignore these. I just had some problems with Docker and to make it easier I just put my HOMEWORK_PROJECT_STUFF in the same folder which consisted of my practical lesson work. 

## ETL Process
1. Data Extraction:
The dataset was downloaded as an Excel file and parsed as csv for initial preprocessing.

2. Data Transformation (Python 3):

- Code for this is located in the request_data.py.
- Installed pandas, requests and datetime libraries.
- Date Formatting: The date column in the dataset was reformatted to a standard date format (YYYY-MM-DD).
- Filtering Data: Data was filtered to include only records from the years 2004 and 2023. Especially wanted to look into the years 2020 and 2021, as these years were significantly impacted by the COVID-19 pandemic.
- Creating Parquet File: The cleaned and transformed data (unemployed_data_exported.csv) was then saved as a Parquet file (unemployed_data_exported.parquet) for efficient storage and retrieval. 

3. Data Load/Visualization 
Apache Superset was used for creating interactive and insightful visualizations. 
- Four key visualizations were created (dashboard_export.zip): 
    1. Monthly Registered Unemployed (2004-2023).
    2. Type of Benefit or Allowance by Percentage Over the Years 2004-2023
    3. Type of Benefit or Allowance by Percentage Over the Years 2020-2021
    4. Monthly Registered Unemployed in 2020-2021 by Gender, Age Group, and County
       
Also some additional visualisations (dashboard_export_additional.zip).

## How to Use This Repository
### Prerequisites
- Python 3 or higher (inside container)
- Docker
- Visual Studio (Optional)
- Git (Optional)
- Apache Superset (Set up with docker)

Clone my repository
- git clone ´https://github.com/mailiisvah/ETL_superset´

### Build and run the Docker container
- `docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=<super value>" --name superset my/superset:duckdb`
- `docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin`
- `docker exec -it superset superset db upgrade`
- `docker exec -it superset superset init`

Copy HOMEWORK_PROJECT_STUFF inside the container created above
- `docker cp HOMEWORK_PROJECT_STUFF superset:app/superset/HOMEWORK_PROJECT_STUFF`

Verify that files exists inside container
- `docker exec -it superset bash` goes inside the container`
- `cd superset/HOMEWORK_PROJECT_STUFF` navigates to directory where files are supposed to be
- `ls -a` see files inside the directory
- `python3 request_data.py` runs the script and creates parquet file

### OR

- Open VS code and open container within.
- Move files manually from HOMEWORK_PROJECT_STUFF to the container
- Run `python3 request_data.py`
Should have created parquet file


### Querying data and using superset

- Navigate to localhost:8080 and enter the credentials set up during the initialization process to log in. 
- Connect to DuckDB database and use SQL query to load the dataset into Superset for visualisation. 
- `SELECT * FROM read_parquet('/data/HOMEWORK_PROJECT_STUFF/parquet_hw/*.parquet')`

More tips can be found in the TUTORIAL.txt.

License
This project is licensed under the MIT License. 
