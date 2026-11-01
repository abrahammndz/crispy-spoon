import pandas as pd
from datetime import datetime

def transform_weather_data(raw_data):
    hourly = raw_data.get("hourly",{})

    df = pd.DataFrame({
        "temperature °C": hourly.get("temperature_2m"),
        "wind_speed km/h": hourly.get("wind_speed_10m"),
        "recorded_at": hourly.get("time")
        })
    
    df['recorded_at']=pd.to_datetime(df['recorded_at'])
    df["day"] = df["recorded_at"].dt.date
    df["hour"] = df["recorded_at"].dt.hour
    
    df['processed_at'] = (datetime.now(timezone.utc) if 'timezone' in globals() else datetime.utcnow()).replace(microsecond=0)

    df = df.dropna()

    print("Transformation and cleaning successful!")
    return df
