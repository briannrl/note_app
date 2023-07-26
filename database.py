import harperdb
from decouple import config

HARPERDB_URL=config("HARPERDB_URL", cast=str)
HARPERDB_USERNAME=config("HARPERDB_USERNAME")
HARPERDB_PASSWORD=config("HARPERDB_PASSWORD")

db = harperdb.HarperDB(
    url=HARPERDB_URL,
    username=HARPERDB_USERNAME,
    password=HARPERDB_PASSWORD
)