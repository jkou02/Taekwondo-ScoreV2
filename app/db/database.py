from databases import Database

DATABASE_URL = "sqlite:///./events.db"  # Base de datos local

database = Database(DATABASE_URL)