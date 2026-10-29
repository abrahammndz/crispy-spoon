from extract import extract_weather_data
from transform import transform_weather_data
from load import load_to_postgres

def run_pipeline():
    try:
        print("Starting ETL Pipeline...")
        raw = extract_weather_data()
        cleaned_df = transform_weather_data(raw)
        load_to_postgres(cleaned_df)
        print("ETL Pipeline completed successfully.")
    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
