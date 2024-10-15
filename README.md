**Week 7 Task - Telegram Data Scraping, Database Storage, and YOLO Training**

#Overview

This repository contains code and resources for the following tasks:

    1. Scraping data from Telegram channels.
    2. Storing the scraped data in a PostgreSQL database.
    3. Training a YOLO (You Only Look Once) model using scraped image data.
    4. ETL process for cleaning and transforming the data using DBT (Data Build Tool).


Repository Structure
```bash
      my_project/
    ├── main.py                 # FastAPI app for exposing collected data via API
    ├── database.py             # Database connection configuration using SQLAlchemy
    ├── models.py               # SQLAlchemy models for the database tables
    ├── schemas.py              # Pydantic schemas for data validation and serialization
    ├── crud.py                 # CRUD operations for interacting with the database
    ├── scrape_telegram.py      # Script for scraping Telegram data (text and images)
    ├── train_yolo.py           # YOLO model training script with scraped images
    ├── data/                   # Contains scraped data in JSON format
    │   ├── channel1.json       # Example JSON file for a Telegram channel
    │   ├── ...
    ├── etl_project/            # Contains DBT models and ETL code for data transformation
    │   ├── dbt_project.yml     # DBT project configuration
    │   ├── models/             # DBT models for transforming the raw data
    │   └── ...
    └── README.md               # This README file
```

Requirements

To run this project, you need the following tools and libraries installed:

    Python 3.x
    FastAPI for building APIs
    Uvicorn for running FastAPI apps
    SQLAlchemy for database interaction
    DBT (Data Build Tool) for data transformations
    YOLOv5 for object detection with images
    Telethon for Telegram scraping
    
Installation

  1. Clone the repository:
       
      ```
       bash
          git clone https://github.com/your-repo/week7-task.git
          cd week7-task
      ```
  2. Set up a virtual environment:
     
     ```
     bash
         python3 -m venv myenv
         source myenv/bin/activate
     ```
3. Install required dependencies:
   ```
   bash
         pip install -r requirements.txt
   ```

4. Set up PostgreSQL database:
   Make sure PostgreSQL is running, and update the database credentials in database.py

Usage
1. Scraping Telegram Data
The scrape_telegram.py script scrapes data (text and images) from Telegram channels and stores the data in the data/ directory.
    ```
      bash
  
        python scrape_telegram.py
    ```
2. Storing Scraped Data in the Database
The collected data can be processed and stored in a PostgreSQL database using the crud.py module.
   ```
    bash
      
      python main.py
    ```

Run the FastAPI app to expose APIs for interacting with the database.

3. Training YOLO with Scraped Images

The train_yolo.py script trains the YOLO model using images scraped from the Telegram channels.
 ```
  bash
    
    python train_yolo.py
 ```

4. Running the ETL Process

The ETL process transforms the raw scraped data into structured formats using DBT.
  ```
  bash
    
    cd etl_project
    dbt run
  ```
License

This project is licensed under the MIT License. See the LICENSE file for more details.



