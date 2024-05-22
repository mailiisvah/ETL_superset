import pandas as pd
import requests
import datetime

def fetch_air_range():
    url = 'https://avaandmed.eesti.ee/api/datasets/b981a0ba-7ac8-443e-89a4-30515e4d9c80/files/66e56ee3-990b-4434-9d5d-574cf331f637/download'

    response = requests.post(url)
    response.encoding = 'utf-8'  # Set the response encoding to UTF-8

    return response.text

def fetch_data():
        print(f'Fetching data')
        data = fetch_air_range()
        with open(f'csv_hw/unemployed_data_exported.csv', 'w', encoding='utf-8') as f:
            f.write(data)

fetch_data()

# Read the CSV file into a DataFrame
df = pd.read_csv('csv_hw/unemployed_data_exported.csv', encoding='utf-8')

# Convert the 'Kuupäev' column to Date format
df['Kuupäev'] = pd.to_datetime(df['Kuupäev'], format='%m/%d/%y')
df = df[(df['Kuupäev'].dt.year >= 2004) & (df['Kuupäev'].dt.year <= 2023)]
df['Kuupäev'] = df['Kuupäev'].dt.date

df.to_parquet('parquet_hw/unemployed_data_exported.parquet')