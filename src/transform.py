import pandas as pd
from datetime import datetime

def transform_weather_data(raw_data):
    current = raw_data.get("current",{})

    df = pd.DataFrame([{
        "latitude": raw_data.get("latitude"),
        "longitude": raw_data.get("longitude"),
        "temperature": current.get("temperature_2m"),
        "wind_speed": current.get("wind_speed_10m"),
        "recorded_at": current.get("time")
        }])
    
    df['processed_at'] = datetime.utcnow()
    df = df.dropna()

    print("Transformation and cleaning successful!")
    return df
