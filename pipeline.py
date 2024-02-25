"This file combines the functionality of the extract, transform and load scripts."

from extract import extract_reviews
from transform import transform
from load import get_db_connection, upload_dataframe

if __name__ == "__main__":

    raw_reviews = extract_reviews("dataops_tp_reviews.csv")
    
    clean_reviews = transform(raw_reviews)

    conn = get_db_connection()

    upload_dataframe(conn, clean_reviews)