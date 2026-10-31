import requests

def extract_weather_data():
    url="https://api.open-meteo.com/v1/forecast?latitude=41.85&longitude=-87.65&past_days=10&hourly=temperature_2m,wind_speed_10m"
    response = requests.get(url)

    if response.status_code == 200:
        print("Extraction successful!")
        return response.json()
    else:
        raise Exception(f"API extraction failed with status code {resonse.status_code}")

if __name__=="__main__":
    data = extract_weather_data()
    print(data)

