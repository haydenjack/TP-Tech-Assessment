"This file contains unit tests for the functions."

import pytest
import pandas as pd

from pipeline.extract import extract_reviews
from pipeline.transform import to_snake_case, validate_email, format_column_names
from pipeline.review_functions import validate_new_review


def test_extract_reviews_no_file():
    "Tests that the correct error is raised when a wrong filepath is given."
    with pytest.raises(FileNotFoundError):
        extract_reviews("imaginary_file.csv")


def test_to_snake_case_basic():
    "Tests the snake case function is working correctly."
    assert to_snake_case("Hello World") == "hello_world"
    assert to_snake_case("The Quick Brown Fox Jumps Over the LaZy DOG") == "the_quick_brown_fox_jumps_over_the_lazy_dog"


def test_validate_email():
    "Ensures the function catches incorrect emails."
    assert validate_email("incorrect_email@nothing") == None
    assert validate_email("correct@email.com") == "correct@email.com"
    assert validate_email(123) == None


def test_format_column_names():
    "Tests column name formatting on unrelated dataset."
    test_df = pd.DataFrame({
        "First Name": ["Sally", "Mary", "John"],
        "Years Old": [50, 40, 30],
        "Drivers License": [True, False, False]
        })
    test_df_renamed = format_column_names(test_df)
    assert list(test_df_renamed.columns) == ["first_name", "years_old", "drivers_license"]
    

def test_validate_new_review_correct():
    "Tests a valid input will return a dictionary."
    mock_review = {
        "reviewer_name" : "John Doe",
        "review_title" : "Good Service",
        "review_rating" : 5,
        "review_content": "Overall great service.",
        "email_address" : "john@me.com",
        "country" : "USA",
        "review_date": "2024-02-27"}
    assert validate_new_review(mock_review) == mock_review


def test_validate_new_review_string_type():
    "Tests the function catches wrong data types."
    with pytest.raises(ValueError):
        validate_new_review("String")


def test_validate_new_review_int_type():
    "Tests the function catches wrong data types."
    with pytest.raises(ValueError):
        validate_new_review(55)


def test_validate_new_review_wrong_keys():
    "Tests the function catches wrong dictionary information."
    mock_wrong_review = {
        "first_name" : "John Doe",
        "review_title" : "Good Service",
        "review_rating" : 5,
        "review_content": "Overall great service.",
        "email_address" : "john@me.com",
        "country" : "USA",
        "review_date": "2024-02-27"}
    with pytest.raises(ValueError):
        validate_new_review(mock_wrong_review)
