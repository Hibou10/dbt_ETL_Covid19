import os
import requests
import snowflake.connector
from dotenv import load_dotenv

# .env Datei laden
load_dotenv()

# API abrufen
url = "https://disease.sh/v3/covid-19/countries"
data = requests.get(url).json()

# Verbindung zu Snowflake
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse="DBT_WH",
    database="COVID_DB",
    schema="RAW_DATA"
)
cur = conn.cursor()

# Tabelle leeren (falls vorher schon mal geladen)
cur.execute("TRUNCATE TABLE COVID_RAW")

# Daten einfügen
for row in data:
    cur.execute("""
        INSERT INTO COVID_RAW (COUNTRY, CASES, TODAYCASES, DEATHS, TODAYDEATHS, TESTS, POPULATION)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row.get("country"),
        row.get("cases"),
        row.get("todayCases"),
        row.get("deaths"),
        row.get("todayDeaths"),
        row.get("tests"),
        row.get("population")
    ))

conn.commit()
cur.close()
conn.close()