import json
import pandas as pd
from sqlalchemy import create_engine

# Read and flatten the JSON
with open("data/input.json", "r") as f:
    json_raw = json.load(f)

df = pd.json_normalize(json_raw, sep='_')
df[['lat', 'lon']] = pd.DataFrame(df['pickupAddress_geoLocation'].tolist())
df.drop(columns='pickupAddress_geoLocation', inplace=True)
df.drop(columns='dropOffAddress_geoLocation', inplace=True)

# PostgreSQL connection
engine = create_engine("postgresql+psycopg2://root:root@postgres:5432/main")




# Write to PostgreSQL table using pandas
df.to_sql( name='deliveries', con=engine, if_exists='append', index=False )