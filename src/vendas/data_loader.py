import sqlite3
import pandas as pd
from src.vendas.config import DATABASE_PATH, TABLE_NAME


def load_data() -> pd.DataFrame:
    """
    Load data from the SQLite database and return it as a pandas DataFrame.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", conn)
    conn.close()
    return df
