DROP DATABASE IF EXISTS trustpilot;

CREATE DATABASE trustpilot;

\c trustpilot;

CREATE TABLE reviews (
    id INT GENERATED ALWAYS AS IDENTITY,
    reviewer_name VARCHAR(200),
    review_title VARCHAR(200),
    review_rating SMALLINT,
    review_content TEXT,
    email_address VARCHAR(320),
    country VARCHAR(100),
    review_date DATE
);