import os
import json
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError, SessionPasswordNeededError
from dotenv import load_dotenv
import logging
# Initialize logging
logging.basicConfig(filename="telegram_scraper.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Api credentials
load_dotenv()
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
api_id = os.getenv('API_ID')

# Initialize Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# The channels to scrape
channels = [
    'https://t.me/DoctorsET',
    'https://t.me/CheMed123',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/yetenaweg',
    'https://t.me/EAHCI'
]

# Directory for storing images
image_dir = 'telegram_images'
os.makedirs(image_dir, exist_ok=True)

# Function to scrape and save messages and images
def scrape_telegram_channels():
    try:
        logging.info("Starting Telegram scraping process...")
        
        with client:
            for channel in channels:
                logging.info(f"Scraping channel: {channel}")
                
                # Ensure that the channel is a valid input
                try:
                    entity = client.get_entity(channel)
                except Exception as e:
                    logging.error(f"Failed to get entity for {channel}: {e}")
                    continue
                
                # Initialize a list to store message data
                messages_data = []
                
                for message in client.iter_messages(entity):
                    # Collect text-based messages
                    if message.text:
                        messages_data.append({
                            "message_id": message.id,
                            "message": message.text,
                            "date": str(message.date)
                        })
                    
                    # Collect media messages (images)
                    if message.media:
                        try:
                            file_path = client.download_media(message.media, file=image_dir)
                            logging.info(f"Downloaded image: {file_path}")
                        except Exception as e:
                            logging.error(f"Failed to download media from message {message.id}: {e}")
                
                # Save the scraped messages to a JSON file
                json_file = f"{channel.split('/')[-1]}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(messages_data, f, ensure_ascii=False, indent=4)
                logging.info(f"Data from {channel} saved to {json_file}")

    except FloodWaitError as e:
        logging.error(f"Flood wait error occurred: Need to wait {e.seconds} seconds")
    except SessionPasswordNeededError:
        logging.error("Two-step verification is enabled. Unable to scrape without password.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Start the scraping process
if __name__ == "__main__":
    scrape_telegram_channels()
    logging.info("Scraping completed.")
