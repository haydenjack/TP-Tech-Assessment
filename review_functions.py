"This file contains the functionality to add to and update the review database."

from psycopg2.extensions import connection

from load import get_db_connection
from transform import validate_email


REVIEW_KEYS = ["reviewer_name",
               "review_title",
               "review_rating",
               "review_content",
               "email_address",
               "country",
               "review_date"]

# Create a function that adds a new review to the table
# Create a function that updates the review content

def add_review(conn: connection, review_data: dict) -> None:
    "Uploads a new review to the database."

    if not isinstance(review_data, dict):
        raise ValueError("Review data must be input as a dictionary.")
    if list(review_data.keys()) != REVIEW_KEYS:
        raise ValueError(f"Review data must contain required fields.\n{REVIEW_KEYS}")

    review_data["email_address"] = validate_email(review_data["email_address"])

    review_list = list(review_data.values())
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO reviews
                    (reviewer_name, review_title, review_rating, review_content, email_address, country, review_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """, review_list)
        conn.commit()
    conn.close()


if __name__ == "__main__":

    review_dict = {
        "reviewer_name" : "Jack Hayden",
        "review_title" : "Excellent Service",
        "review_rating" : 5,
        "review_content" : "Very impressed with this service. Fast delivery and good customer support.",
        "email_address" : "jackhayden@trustpilot.com",
        "country" : "UK",
        "review_date" : "2024-02-25"
    }

    conn = get_db_connection()

    add_review(conn, review_dict)