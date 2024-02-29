# Jack Hayden - Technical Assessment

This repository contains the solution for a robust ETL (Extract, Transform, and Load) pipeline specifically tailored for review data management. It facilitates the extraction of reviews, transforms the data for optimal database storage, and manages updates and insertions of new reviews.

## ✅ Getting Started

Before running the scripts, you need to set up the environment.

1. Install all necessary Python libraries with:
   ```sh
   pip3 install -r requirements.txt
   ```

2. A `.env` file is required with these variables:
    - `DB_NAME` name of database to which you connect
    - `DB_HOST` host of database
    - `DB_USER` user connecting to the database

## 🗂️ Repository Structure

### `database`
 This section deals with setting up your database infrastructure.

- `db_setup.sh`: this is a shell script that runs the `schema.sql` file within PostgreSQL to create the required database.
- `schema.sql`: this contains the instructions to create the `trustpilot` database and the `reviews` table within it. This file is written in SQL.

 #### Setting Up the Database
 1. This database uses PostgreSQL. To install this with homebrew run: 
    ```sh
    brew install postgresql
    ```
 2. Initialise the database with:
    ```sh
    bash db_setup.sh
     ```
    This will run the instructions in `schema.sql` with PostgreSQL to create the necessary database and table.


### `pipeline`
This directory contains the scripts that extracts the reviews from a csv file, programmatically cleans the data and finally uploads them to the database. Additionally, reviews can be added and updated in the database.

- `dataops_tp_reviews.csv`: Mock review data in CSV format.
- `extract.py`: Defines a function for data extraction from CSV to a pandas DataFrame.
- `transform.py`: Contains functions to clean and standardize the DataFrame.
- `load.py`: Manages database connections and data uploading.
- `pipeline.py`: Integrates the functionality of `extract.py`,`transform.py` and `load,py` to set up a pipeline that can ingest the reviews csv data, clean it and upload it with a single command.
- `review_functions.py`: Provides functionality for adding and updating review records.
- `test_pipeline.py`: Contains unit tests for the pipeline to ensure reliability. Run with `pytest test_pipeline.py` to ensure the functions are properly working.

**Running the Pipeline:**
- Ensure the required python libraries are installed as noted in '✅ Getting Started.'
- Execute:
    ```sh
    python3 pipeline.py
    ```

### ➕ Adding a Review
**Steps:**
1. In `review_functions.py`, locate `add_review`.
2. Import `get_db_connection` function from `load.py`.
3. Prepare a review dictionary with the appropriate keys and values: ["reviewer_name","review_title", "review_rating", "review_content", "email_address", "country", "review_date"].
4. Run `add_review(conn, review_dict)` where `conn`: output of `get_db_connection` and `review_dict`: dictionary from the previous steps.

### ✏️ Updating a Review in the Database
**Steps:**
1. In `review_functions.py`, locate `update_review`.
2. Import `get_db_connection` from `load.py`.
3. Identify the review ID to update.
4. Run `update_review(conn, review_id, new_content)` where `conn`: output of `get_db_connection`, `review_id`: identified in step 3, `new_content`: updated review content.