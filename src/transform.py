import pandas as pd
from datetime import datetime

def transform_weather_data(raw_data):
    hourly = raw_data.get("hourly",{})

    df = pd.DataFrame({
        "temperature": hourly.get("temperature_2m"),
        "wind_speed": hourly.get("wind_speed_10m"),
        "recorded_at": hourly.get("time")
        })
    
    df['processed_at'] = datetime.now(timezone.utc) if 'timezone' in globals() else datetime.utcnow()

    df = df.dropna()

    print("Transformation and cleaning successful!")
    return df
