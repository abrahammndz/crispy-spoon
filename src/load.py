from sqlalchemy import create_engine, Table, Column, Integer, Float, DateTime, Date, MetaData
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(df):
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    metadata = MetaData()

    if not db_url:
        raise ValueError("DATABASE_URL is missing or not loaded!")
    
    weather_metrics = Table(
            "weather_metrics",
            metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("date", Date),
            Column("time", Integer),
            Column("temperature", Float),
            Column("wind_speed", Float),
            Column("recorded_at", DateTime),
            Column("processed_at",DateTime)
    )

    metadata.create_all(engine)

    df.to_sql('weather_metrics', con=engine, if_exists='append', index=False)
    print("Data successfully loaded into PostgreSQL warehouse!")
