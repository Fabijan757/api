TV Show Analysis – Project (API + MySQL + Tableau)

This project demonstrates a complete workflow for processing and analyzing TV show data using an API, a MySQL database, and Tableau visualizations. The goal was to automatically retrieve data about the highest-rated and lowest-rated TV shows, store it in a relational database, analyze it with SQL queries, and visualize the results through an interactive dashboard.

1. Data collection (API)
TV show data was retrieved via a public API (no API key required).
The collected data includes:
- show name
- rating
- genres
- language

The API was used within a Python script and the data was saved into CSV files:
- top_rated.csv
- lowest_rated.csv

2. Data import into MySQL
The data was loaded into MySQL into a table named 'tv_shows' with the following columns:
- id
- name
- rating
- genres
- language

3. SQL analysis
The performed analyses include:
- average rating by genre
- number of shows per genre
- sorting top-rated and lowest-rated shows
- filtering shows by genre

4. Visualizations (Tableau Dashboard)
Three charts were created:
- lowest-rated TV shows
- top-rated TV shows
- genre count and average rating analysis

5. Result
The project demonstrates a full data engineering pipeline:
API → CSV → MySQL → SQL analysis → Tableau Dashboard
