import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text
from parser import get_roads_dataframe


load_dotenv()
DB_URI = os.getenv('DATABASE_URL')
ARCGIS_URL = "https://services1.arcgis.com/RbMX0mRVOFNTdLzd/arcgis/rest/services/Maine_E911_Roads_Feature/FeatureServer/0/query"

engine = create_engine(DB_URI)

def run_full_fetcher():
    """Fetches all features from ArcGIS and saves to geojson."""
    print("Step 1: Fetching Data")
    features = []
    offset = 0
    page_size = 1000

    while True:
        params = {
            "where": "1=1",
            "outFields": "*",
            "resultRecordCount": page_size,
            "resultOffset": offset,
            "f": "geojson"
        }

        r = requests.get(ARCGIS_URL, params=params)
        r.raise_for_status()
        data = r.json()
        page = data.get("features", [])

        if not page:
            break

        features.extend(page)
        offset += page_size
        # Updated to simple dynamic progress bar
        print(f"Fetched {len(features)} / ???")

    # check output directory exists
    os.makedirs("outputs", exist_ok=True)
    filepath = "outputs/e911_roads.geojson"

    geojson_output = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(filepath, "w") as f:
        json.dump(geojson_output, f)

    print(f"Done. Saved to {filepath}")
    return filepath

def load_to_postgres(geojson_file, table_name="e911_roads"):
    print("STEP 2: Parsing Data")
    df = get_roads_dataframe(geojson_file)
    
    # 2. Check if table exists (Explicitly looking in maine)
    inspector = inspect(engine)
    if inspector.has_table(table_name, schema='maine'):
        print(f"Table '{table_name}' exists in schema 'maine'. Checking for duplicates...")
        
        # Use a plain string here for read_sql to keep it simple
        query = f"SELECT objectid FROM maine.{table_name}"
        existing_ids = pd.read_sql(query, engine)['objectid']
        
        df = df[~df['objectid'].isin(existing_ids)]
        
        if df.empty:
            print("Database is up to date.")
            return
        
        print(f"Found {len(df)} new records to add.")
        mode = 'append'
    else:
        print(f"Table '{table_name}' not found in 'maine'. Creating a fresh table.")
        mode = 'replace'

    # 3. Insert into Database
    try:
        print(f"Step 3: Upload to Database ({mode.upper()}) ---")
        df.to_sql(
            table_name, 
            engine, 
            schema='maine',      
            if_exists=mode, 
            index=False, 
            chunksize=1000,
            method='multi' 
        )
        print("Upload complete.")

        with engine.connect() as conn:
            # Explicitly naming columns so the table is easy to read in the console
            res = conn.execute(text(f"SELECT objectid, street_full_name, town FROM maine.{table_name} LIMIT 5"))
            test_df = pd.DataFrame(res.fetchall(), columns=res.keys())
            print(test_df.to_string(index=False)) # to_string makes it look cleaner

    except Exception as e:
        print(f"An error occurred during upload: {e}")
        
if __name__ == "__main__":
    # Execute the entire pipeline
    try:
        path = run_full_fetcher()
        load_to_postgres(path)
        print("\nPipeline execution finished successfully.")
    except Exception as e:
        print(f"\nPipeline failed: {e}")
