# Jack Hayden - Technical Assessment

This repository contains a solution for extracting, transforming and loading reviews into a database. It has additional functionality that allows reviews to be updated and new ones added to the database.

## 🗂️ Repository Structure

### `database`
 This directory contains the scripts needed to set up the initial database.

### `pipeline`
This directory contains the scripts that create the ETL pipeline, as well as adding & updating reviews.

## ✅ Getting Started

Before running the scripts, you need to set up the environment.

Run `pip3 install -r requirements` to install all necessary Python libraries.

A `.env` file is required with these variables:
- `DB_NAME` name of database to which you connect
- `DB_HOST` host of database
- `DB_USER` user connecting to the database