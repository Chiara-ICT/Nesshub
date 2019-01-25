import os

config_ness = {
    'host': os.getenv("DB_HOST", "localhost"),
    'port': os.getenv("DB_PORT", 3307),
    'user': "root",
    'passwd': "chiara",
    'database': "nesshub"
}

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 3307)
DB_USER = "root"
DB_PASSWORD = "chiara"
DB_DATABASE = "nesshub"

DB_PUBLIC = "public"