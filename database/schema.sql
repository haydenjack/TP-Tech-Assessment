DROP DATABASE IF EXISTS trustpilot;

CREATE DATABASE trustpilot;

\c trustpilot;

CREATE TABLE reviews (
    id INT GENERATED ALWAYS AS IDENTITY,
    reviewer_name VARCHAR(200),
    review_title VARCHAR(200) NOT NULL,
    review_rating SMALLINT NOT NULL,
    review_content TEXT NOT NULL,
    email_address VARCHAR(320),
    country VARCHAR(100),
    review_date DATE NOT NULL
);