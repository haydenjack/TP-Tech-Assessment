"This file combines the functionality of the extract, transform and load scripts."

from extract import extract_reviews
from transform import transform
from load import get_db_connection, upload_dataframe

if __name__ == "__main__":

    # Read in the reviews csv file as a pandas data frame
    raw_reviews = extract_reviews("dataops_tp_reviews.csv")

    # Cleans the data frame of invalid values
    clean_reviews = transform(raw_reviews)

    # Creates a connection the to database
    conn = get_db_connection()

    # Inserts the data frame into the database.
    upload_dataframe(conn, clean_reviews)
