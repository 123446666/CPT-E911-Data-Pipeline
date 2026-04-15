import json
import pandas as pd

# Fields to keep and their cleaned column names
FIELD_MAP = {
    "OBJECTID": "objectid",
    "SEGMENTID": "segment_id",
    "RCL_UID": "rcl_uid",
    "ST_FULLNAME": "street_full_name",
    "ST_NAME": "street_name",
    "ST_PREDIR": "street_predir",
    "ST_POSTTYP": "street_type",
    "ST_POSTDIR": "street_postdir",
    "RDNAME": "road_name",
    "L_ADD_FROM": "addr_left_from",
    "L_ADD_TO": "addr_left_to",
    "R_ADD_FROM": "addr_right_from",
    "R_ADD_TO": "addr_right_to",
    "LPARITY": "parity_left",
    "RPARITY": "parity_right",
    "RDCLASS": "road_class",
    "ONEWAY": "oneway",
    "SPEED": "speed",
    "MDOTJURIS": "jurisdiction",
    "ROUTE_NUM": "route_num",
    "TOWN": "town",
    "LCITY": "city_left",
    "RCITY": "city_right",
    "LCOUNTY": "county_left",
    "RCOUNTY": "county_right",
    "LSTATE": "state_left",
    "RSTATE": "state_right",
    "LZIPCODE": "zip_left",
    "RZIPCODE": "zip_right",
    "PSAP": "psap",
    "DATEUPDATE": "date_updated",
    "EFFECTIVE": "date_effective",
    "EXPIRE": "date_expire"
}

def parse_feature(feature):
    """Extracts properties and geometry from a single GeoJSON feature."""
    props = feature["properties"]
    # Extract only the mapped fields and rename them
    row = {clean: props.get(api) for api, clean in FIELD_MAP.items()}
    # Attach the geometry as a json string for postgis/jsonb insertion
    row["geom"] = json.dumps(feature["geometry"])
    return row

def get_roads_dataframe(geojson_path):
    """
    Parses a GeoJSON file and returns a clean Pandas DataFrame 
    formatted for SQL injection.
    """
    print(f"Opening {geojson_path}...")
    with open(geojson_path, "r") as f:
        data = json.load(f)
    
    features = data.get("features", [])
    print(f"Parsing {len(features)} features...")
    
    # Process all features
    parsed_rows = [parse_feature(f) for f in features]
    
    # Create DataFrame
    df = pd.DataFrame(parsed_rows)
    
    # Convert ESRI/ArcGIS millisecond timestamps to Postgres-friendly datetimes
    date_cols = ['date_updated', 'date_effective', 'date_expire']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], unit='ms', errors='coerce')
    
    print("DataFrame conversion complete.")
    return df
