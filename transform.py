"This file contains the functionality to transform and clean review data."

import re
import pandas as pd

from extract import extract_reviews

EMAIL_REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def to_snake_case(words: str) -> str:
    "Converts words to snake case for consistency."
    if not isinstance(words, str):
        raise ValueError("Only str values can be converted.")
    return words.lower().replace(" ", "_")


def validate_email(email: str) -> str | None:
    "Ensures email has a valid format."
    if re.fullmatch(EMAIL_REGEX, email):
        return email
    return None


def format_column_names(df: pd.DataFrame) -> pd.DataFrame:
    "Converts data frame column names to snake case."
    for column in df.columns:
        df.rename(columns={column: to_snake_case(column)}, inplace=True)
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    "Ensures the data frame is properly cleaned and formatted."
    df = format_column_names(df)
    # Replaces invalid emails with None
    df["email_address"] = df["email_address"].apply(validate_email)
    # Converts review_date to datetime64 data type
    df["review_date"] = pd.to_datetime(df["review_date"], format="%Y-%m-%d")
    return df


if __name__ == "__main__":

    reviews = extract_reviews("dataops_tp_reviews.csv")
    df = transform(reviews)

    print(df.head(20))
