"This file contains the functionality to extract review data from a csv file."

import logging
import pandas as pd


def extract_reviews(filepath: str) -> pd.DataFrame:
    "Converts a csv file into a pandas data frame."
    try:
        review_df = pd.read_csv(filepath)
        return review_df
    except FileNotFoundError:
        logging.error("This file could not be found, try again.")
        return None


if __name__ == "__main__":

    reviews = extract_reviews("dataops_tp_reviews.csv")
