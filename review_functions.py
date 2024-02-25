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


def update_review(conn:connection, review_id: int, review_update: str) -> None:
    "Updates the content of a review given the review id."
    update_query = """UPDATE reviews SET review_content = %s WHERE id = %s"""
    
    with conn.cursor() as cur:
        cur.execute(update_query, vars=(review_update, review_id))
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

    update_review(conn, 80, 'Updated from the python function')
