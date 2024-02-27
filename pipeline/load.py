"This file contains the functionality to load a data frame into a database."

from os import environ
from psycopg2 import connect, OperationalError
from psycopg2.extensions import connection
from dotenv import load_dotenv
import pandas as pd


load_dotenv()


def get_db_connection() -> connection:
    "Establishes connection to relevant database."
    try:
        return connect(dbname=environ["DB_NAME"],
                    host=environ["DB_HOST"],
                    user=environ["DB_USER"])
    except OperationalError:
        raise OperationalError("Could not establish connection to the database.")


def upload_dataframe(conn: connection, dataframe: pd.DataFrame) -> None:
    "Uploads extracted & transformed data to relevant database."
    insert_query = ("""
                    INSERT INTO reviews
                    (reviewer_name, review_title, review_rating, review_content, email_address, country, review_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """)

    list_dataframe = dataframe.values.tolist()

    with conn.cursor() as cur:
        cur.executemany(insert_query, list_dataframe)
        conn.commit()
    conn.close()
