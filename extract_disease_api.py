import requests
import snowflake.connector

# API abrufen
url = "https://disease.sh/v3/covid-19/countries"
data = requests.get(url).json()

# Verbindung zu Snowflake
conn = snowflake.connector.connect(
    user="HICHAMBOU",
    password="Slthishamaayda123#",
    account="kivkhcd-to59117",
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