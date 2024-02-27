"This file contains the functionality to extract review data from a csv file."

import pandas as pd


def extract_reviews(filepath: str) -> pd.DataFrame:
    "Converts a csv file into a pandas data frame."
    try:
        review_df = pd.read_csv(filepath)
        return review_df
    except FileNotFoundError as exc:
        raise FileNotFoundError("This file could not be found, try again.") from exc
