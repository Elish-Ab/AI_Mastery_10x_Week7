import os
import json
import pandas as pd
from sqlalchemy import create_engine
import logging

# Set up logging
logging.basicConfig(
    filename='etl_process.log',  # Log file name
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Step 1: Extract
data_directory = '../data'  # Path to the data directory
dataframes = []

logging.info("Starting data extraction...")

try:
    for filename in os.listdir(data_directory):
        if filename.endswith('.json'):
            logging.info(f"Processing file: {filename}")
            with open(os.path.join(data_directory, filename)) as f:
                data = json.load(f)
                df = pd.json_normalize(data)  # Flatten JSON data
                dataframes.append(df)

    # Combine all dataframes into one
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        logging.info(f"Combined dataframe shape: {combined_df.shape}")
    else:
        logging.warning("No JSON files found or dataframes are empty.")

    # Step 2: Transform
    logging.info("Starting data transformation...")
    # Example transformation: Drop rows with null values
    cleaned_df = combined_df.dropna()
    logging.info(f"Cleaned dataframe shape: {cleaned_df.shape}")

    # Step 3: Load
    logging.info("Loading data into the database...")
    try:
        # Connect to the database (adjust connection string as necessary)
        engine = create_engine('postgresql://elish:elish@localhost:5432/telegram_data_db')
        cleaned_df.to_sql('raw_data', engine, if_exists='replace', index=False)
        logging.info("Data loaded successfully.")
    except Exception as e:
        logging.error(f"Error loading data: {e}")
except Exception as e:
    logging.error(f"Error during extraction: {e}")
