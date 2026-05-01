E911 Database Populator

This program is designed to scrape and clean data from an API containing information about Emergency Services road data, then create and populate the events table in the PostgreSQL database.

Python Based ETL
Language Version: Python 3.14.3
Database: PostgreSQL
Key Libraries: pandas, sqlalchemy, dotenv, requests

Database Schema:
Table: e911_roads

objectid - int - Unique object identifier

segment_id - int/str - Road segment identifier

rcl_uid - str - Centerline unique ID

street_full_name - str - Full street name (e.g. "North Main Street")

street_name - str - Base street name (e.g. "Main")

street_predir - str - Pre-directional (e.g. "N", "SW")

street_type - str - Street type suffix (e.g. "ST", "AVE", "RD")

street_postdir - str - Post-directional (e.g. "N", "SW")

road_name - str - Alternate road name

addr_left_from - int - Left side address range start

addr_left_to - int - Left side address range end

addr_right_from - int - Right side address range start

addr_right_to - int - Right side address range end

parity_left - str - Left side even/odd parity (e.g. "E", "O", "B")

parity_right - str - Right side even/odd parity

road_class - str/int - Road classification (e.g. highway, local)

oneway - str - One-way direction flag (e.g. "FT", "TF", or null)

speed - int - Speed limit (mph)

jurisdiction - str - Managing jurisdiction (e.g. "MDOT", "LOCAL")

route_num - str - Route number if applicable

town - str - Town name

city_left - str - City on left side of segment

city_right - str - City on right side of segment

county_left - str - County on left side

county_right - str - County on right side

state_left - str - State on left side

state_right - str - State on right side

zip_left - str - ZIP code on left side

zip_right - str - ZIP code on right side

psap - str - Public Safety Answering Point (911 call center)

date_updated - datetime64[ns] - Last update timestamp

date_effective - datetime64[ns] - Date record became effective

date_expire - datetime64[ns] - Date record expires

geom - str (JSON) - GeoJSON geometry string for PostGIS/JSONB

*Replace dummy values in env file accordingly, and run database_connection.py to initiate program.

Directory Table:
/

├── database_connection.py

├── parser.py

├── proposal.md

├── README.md
