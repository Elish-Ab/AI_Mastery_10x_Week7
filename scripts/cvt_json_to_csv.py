import json
import psycopg2
from dotenv import load_dotenv
import logging
import os

# Load environment variables from the .env file
load_dotenv()

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname=os.getenv('DATABASE'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=os.getenv('PORT')  # ensure PORT is in .env or default to 5432
)
cur = conn.cursor()

# Initialize logging
logging.basicConfig(filename="json_to_csv.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Path to your JSON files
json_files = [
    '/home/elisha-a/Desktop/week7/data/CheMed123.json',
    '/home/elisha-a/Desktop/week7/data/DoctorsET.json',
    '/home/elisha-a/Desktop/week7/data/EAHCI.json',
    '/home/elisha-a/Desktop/week7/data/lobelia4cosmetics.json',
    '/home/elisha-a/Desktop/week7/data/yetenaweg.json',
]


# Create the table only once
cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_data (
        message_id VARCHAR(255),
        message TEXT,
        date TIMESTAMP
    );
""")
logging.info('Table raw_data created (if it did not exist)')

logging.info('Table raw_data created (if it did not exist)')

# Read and insert data
for file in json_files:
    with open(file, 'r') as f:
        data = json.load(f)
        for record in data:
            # Extract fields
            user_id = record.get('message_id')
            text = record.get('message')
            date = record.get('date')
            
            # Insert data into PostgreSQL
            cur.execute("""
                INSERT INTO raw_data (message_id, message, date)
                VALUES (%s, %s, %s);
            """, (user_id, text, date))

logging.info('Data loaded into the DB')

# Commit and close
conn.commit()
cur.close()
conn.close()
