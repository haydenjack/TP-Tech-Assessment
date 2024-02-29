"This file contains the functionality to transform and clean review data."

import re
import pandas as pd


EMAIL_REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
DATE_FORMAT = "%Y-%m-%d"


def to_snake_case(words: str) -> str:
    "Converts string to snake case."
    if not isinstance(words, str):
        raise ValueError("Only str values can be converted.")
    return words.lower().replace(" ", "_")


def validate_email(email: str) -> str | None:
    "Ensures email is a string and has a valid format."
    if isinstance(email, str):
        if re.fullmatch(EMAIL_REGEX, email):
            return email
    return None


def format_column_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    "Converts data frame column names to snake case for consistency."
    for column in dataframe.columns:
        dataframe.rename(columns={column: to_snake_case(column)}, inplace=True)
    return dataframe


def transform(dataframe: pd.DataFrame) -> pd.DataFrame:
    "Ensures the data frame is properly cleaned and formatted."
    dataframe = format_column_names(dataframe)
    # Replaces invalid emails with None
    dataframe["email_address"] = dataframe["email_address"].apply(validate_email)
    # Converts valid dates to datetime, replaces invalid dates with NaT (errors="coerce")
    dataframe["review_date"] = pd.to_datetime(dataframe["review_date"],
                                              format=DATE_FORMAT,
                                              errors="coerce")
    # Removes reviews that have an invalid date (NaT)
    dataframe = dataframe.loc[dataframe.review_date.notnull()]
    return dataframe
