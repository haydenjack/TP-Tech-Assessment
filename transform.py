"This file contains the functionality to transform and clean review data."

import re
import pandas as pd

from extract import extract_reviews

EMAIL_REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def to_snake_case(words: str) -> str:
    "Converts string to snake case for consistency."
    if not isinstance(words, str):
        raise ValueError("Only str values can be converted.")
    return words.lower().replace(" ", "_")


def validate_email(email: str) -> str | None:
    "Ensures email has a valid format."
    if re.fullmatch(EMAIL_REGEX, email):
        return email
    return None


def format_column_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    "Converts data frame column names to snake case."
    for column in dataframe.columns:
        dataframe.rename(columns={column: to_snake_case(column)}, inplace=True)
    return dataframe


def transform(dataframe: pd.DataFrame) -> pd.DataFrame:
    "Ensures the data frame is properly cleaned and formatted."
    dataframe = format_column_names(dataframe)
    # Replaces invalid emails with None
    dataframe["email_address"] = dataframe["email_address"].apply(validate_email)
    # Converts review_date to datetime64 data type
    dataframe["review_date"] = pd.to_datetime(dataframe["review_date"], format="%Y-%m-%d")
    return dataframe


if __name__ == "__main__":

    reviews = extract_reviews("dataops_tp_reviews.csv")
    df = transform(reviews)

    print(df.head(20))
