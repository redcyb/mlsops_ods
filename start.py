from src import *


INITIAL_JSON_DATA = "data/raw/initial.json"
INITIAL_CSV_DATA = "data/interim/initial.csv"
CLEANED_CSV_DATA = "data/interim/clean.csv"
FEATURED_DATA = "data/processed/featured.csv"


if __name__ == "__main__":
    select_region(INITIAL_JSON_DATA, INITIAL_CSV_DATA)
    clean_data(INITIAL_CSV_DATA, CLEANED_CSV_DATA)
    add_features(CLEANED_CSV_DATA, FEATURED_DATA)
