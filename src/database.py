import sqlite3
import pandas as pd

from src.config import DATABASE_PATH


def load_data(tb) -> pd.DataFrame:
    """
    Load data from the SQLite database and return it as a pandas DataFrame.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    df = pd.read_sql_query(f"SELECT * FROM {tb}", conn)
    conn.close()
    return df
