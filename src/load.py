from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(df):
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)

    if not db_url:
        raise ValueError("DATABASE_URL is missing or not loaded!")

    df.to_sql('weather_metrics', con=engine, if_exists='append', index=False)
    print("Data successfully loaded into PostgreSQL warehouse!")
