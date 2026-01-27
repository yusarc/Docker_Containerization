import pandas as pd
from sqlalchemy import create_engine

# 1) Parquet dosyasını oku
df = pd.read_parquet("green_tripdata_2025-11.parquet")

# 2) Postgres bağlantısı (docker-compose ile çalışan DB)
engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")

# 3) Tabloya yaz
df.to_sql(
    name="green_taxi_trips",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=100000,
)
