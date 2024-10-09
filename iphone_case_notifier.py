import requests
from bs4 import BeautifulSoup
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from private_config.config import SENDER_EMAIL, EMAIL_PASSWORD, RECIPIENT_EMAIL

# Configuration
URL = 'https://dbrand.com/shop/ghost/iphone-14-pro-max-clear-cases'
CHECK_INTERVAL = 3
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email():
    """Function to send notification email when the product is available."""
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = 'Product Available!'

        email_body = f'The product is available for purchase: {URL}'
        msg.attach(MIMEText(email_body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        email_text = msg.as_string()

        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, email_text)
        server.quit()

        logging.info('Notification sent successfully!')
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def check_availability():
    """Function to check if the product is available."""
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        if "sold out" not in soup.text.lower():
            logging.info("The product is available for purchase!")
            send_email()
        else:
            logging.info("The product is not available at the moment.")
    except requests.RequestException as e:
        logging.error(f"Error accessing the website: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def start_scheduling():
    logging.info("Starting automatic availability check...")
    schedule.every(CHECK_INTERVAL).minutes.do(check_availability)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    start_scheduling()
