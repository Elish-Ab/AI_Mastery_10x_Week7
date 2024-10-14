import json
import psycopg2
import os

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname=os.getenv('dbname'),  
    user=os.getenv('user'),             
    password=os.getenv('password'),           
    host=os.getenv('host'),            
    port=os.getenv('port')                  
)
cursor = conn.cursor()

# Load JSON files from the specified directory
json_directory = "/home/elisha-a/Desktop/week7/data"  # Adjust this path to your actual directory
for filename in os.listdir(json_directory):
    if filename.endswith(".json"):
        file_path = os.path.join(json_directory, filename)
        with open(file_path, "r") as file:
            data = json.load(file)

        # Create the table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_telegram_data (
            message_id INT PRIMARY KEY,
            message TEXT,
            date TIMESTAMP
        );
        """)

        # Insert JSON data into the table
        for record in data:
           # Inside your loop where you insert data
            try:
                cursor.execute("""
                    INSERT INTO raw_telegram_data (message_id, message, date)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (message_id) DO NOTHING;
                """, (record['message_id'], record['message'], record['date']))
            except Exception as e:
                print(f"Error inserting record: {e}")


            

conn.commit()
cursor.close()
conn.close()
