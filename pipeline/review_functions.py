"This file contains the functionality to add to and update the review database."

from datetime import datetime
from psycopg2.extensions import connection

from transform import validate_email


REVIEW_KEYS = ["reviewer_name",
               "review_title",
               "review_rating",
               "review_content",
               "email_address",
               "country",
               "review_date"]
DATE_FORMAT = "%Y-%m-%d"


def validate_new_review(review_data: dict) -> dict:
    "Ensures a new review contains the relevant information in the correct format."

    # Checks the review data is a dictionary with the correct keys
    if not isinstance(review_data, dict):
        raise ValueError("Review data must be input as a dictionary.")
    if list(review_data.keys()) != REVIEW_KEYS:
        raise ValueError(f"Review data must contain required fields.\n{REVIEW_KEYS}")

    # Checks the date input is in a valid format, raises an error if not
    try:
        datetime.strptime(review_data["review_date"], DATE_FORMAT)
    except ValueError as exc:
        raise ValueError("Review date is invalid.") from exc

    # Validates the email address, replaces with None if invalid
    review_data["email_address"] = validate_email(review_data["email_address"])

    # Ensures each entry value is a str, except for the review_rating which should be an int
    if not all(isinstance(review_data[i], str) for i in review_data.keys() if i not in ["review_rating","email_address"]):
        raise ValueError("Invalid data types in the review information.")

    return review_data


def add_review(conn: connection, review_data: dict) -> None:
    "Uploads a new review to the database."
    try:
        review_data = validate_new_review(review_data)
    except ValueError as exc:
        raise ValueError("Could not upload new review, check review content.") from exc

    # Converts the dictionary to a list of values so it can be used as an execute parameter
    review_list = list(review_data.values())
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO reviews
                    (reviewer_name, review_title, review_rating, review_content, email_address, country, review_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """, review_list)
        conn.commit()
    # Close connection to database to prevent stale connections causing issues
    conn.close()


def update_review(conn:connection, review_id: int, review_update: str) -> None:
    "Updates the content of a review given the review id."
    if not isinstance(review_update, str):
        raise ValueError("Review can only be updated with str.")
    if not isinstance(review_id, int):
        raise ValueError("Review ID must be a valid integer.")

    update_query = """UPDATE reviews SET review_content = %s WHERE id = %s"""

    with conn.cursor() as cur:
        cur.execute(update_query, vars=(review_update, review_id))
        conn.commit()
    # Close connection to database to prevent stale connections causing issues
    conn.close()
