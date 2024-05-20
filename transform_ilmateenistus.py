import pandas as pd

# read in data from excel (required openpyxl)
df = pd.read_excel('ilmateenistus/Tartu-Toravere-2004-2023.xlsx', decimal=',')

# rename date related columns (not really needed, but did it anyway)
df = df.rename(columns={'Aasta': 'year', 'Kuu': 'month', 'Päev': 'day', 'Kell (UTC)': 'time'})

# merge date into single column and drop the original date columns
df['DateTime'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str) + '-' + df['day'].astype(str) + ' ' + df['time'].astype(str), format='%Y-%m-%d %H:%M:%S', utc=True)
df = df.drop(columns=['year', 'month', 'day', 'time'])


# export to parquet
df.to_parquet('ilmateenistus/Tartu-Toravere-2004-2023.parquet', index=False)