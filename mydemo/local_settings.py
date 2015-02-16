
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "06b2778a-4ccb-45f3-a01b-97150209789942959d96-2774-4cde-9d69-016c155aa16308a27a57-5e26-4e8e-9aad-2a67cd2f5a7f"
NEVERCACHE_KEY = "87e5dd94-3843-4036-a630-594f493b6bb9e3050018-5db0-4616-aa36-1eb824b3dd33e96a90e8-97f6-40d3-a6ae-cc44d3b9e13a"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
