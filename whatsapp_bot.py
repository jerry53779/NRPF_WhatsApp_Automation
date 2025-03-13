import time
import socket
import gspread
import datetime
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ✅ Internet check
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("✅ Internet connection is active.")
        return True
    except OSError:
        print("❌ No internet connection. Retrying later...")
        return False

# ✅ Google Sheets authentication
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE")
TOKEN_FILE = "token.json"

def authenticate_google_sheets():
    creds = None
    print("🔄 Checking for existing Google authentication token...")
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        print("✅ Existing token found and loaded.")
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("🔄 Token expired. Refreshing token...")
                creds.refresh(Request())
            else:
                print("🚀 No valid credentials found. Initiating new authentication...")
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                creds = flow.run_local_server(port=8080, redirect_uri_trailing_slash=False)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
            print("✅ New authentication token saved.")
    return creds

# ✅ Get Google Sheet
def get_google_sheet():
    try:
        print("🔄 Connecting to Google Sheets...")
        creds = authenticate_google_sheets()
        client = gspread.authorize(creds)
        sheet_id = os.getenv("SHEET_ID")
        sheet = client.open_by_key(sheet_id)
        worksheet = sheet.worksheet("Sheet1")
        print("✅ Successfully connected to Google Sheets.")
        return worksheet
    except Exception as e:
        print(f"❌ Failed to access Google Sheet: {e}")
        return None

# ✅ Send WhatsApp Message with Debug Logs
def send_whatsapp_message(driver, number, name):
    try:
        print(f"📤 Opening chat for {name} ({number})...")
        
        driver.get(f"https://web.whatsapp.com/send?phone={number}")
        time.sleep(10)  

        print("🔍 Searching for message input box...")
        input_box = driver.find_element(By.XPATH, '//footer//div[@contenteditable="true"]')
        print("✅ Found input box!")

        messages = [
            "Hey",
            "I'm your bot",
            "https://your-link-here.com"
        ]

        for msg in messages:
            print(f"📨 Sending text: {msg}")
            input_box.send_keys(msg)
            input_box.send_keys(Keys.ENTER)
            time.sleep(5)

        print("📂 Attaching image...")
        attachment = driver.find_element(By.XPATH, '//span[@data-icon="attach-menu-plus"]')
        attachment.click()
        time.sleep(2)

        image_upload = driver.find_element(By.XPATH, '//input[@accept="image/*"]')
        image_upload.send_keys("path_to_image.jpg")
        time.sleep(5)
        print("📷 Image uploaded!")

        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()
        time.sleep(2)
        print("✅ Image sent.")

        input_box.send_keys(f"NAME: {name}\nCOLLEGE: Sample College\nNSS UNIT NO: 123\nDOB: 01-01-2000\nTREE NAME: Sample Tree")
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)
        print("✅ Additional text message sent.")

        voice_messages = [
            "path_to_voice_1.opus",
            "path_to_voice_2.opus",
            "path_to_voice_3.opus"
        ]

        for voice in voice_messages:
            print(f"🔊 Sending voice message: {voice}")
            attachment.click()
            time.sleep(2)
            voice_upload = driver.find_element(By.XPATH, '//input[@accept="audio/*"]')
            voice_upload.send_keys(voice)
            time.sleep(5)
            send_button.click()
            time.sleep(2)
            print(f"✅ Voice message {voice} sent.")

        print(f"✅ All messages sent to {number} ({name}).")

    except NoSuchElementException as e:
        print(f"❌ Element not found while sending to {number} ({name}): {e}")
    except Exception as e:
        print(f"❌ Unexpected error while sending to {number} ({name}): {e}")

# ✅ Main Bot Logic with Debugging
def run_bot():
    if not check_internet():
        return
    
    sheet = get_google_sheet()
    if not sheet:
        return
    
    print("✅ Google Sheets connection established.")

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=path_to_user_data_dir")
    service = Service("path_to_chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://web.whatsapp.com")
    print("🔄 Waiting for WhatsApp Web login...")
    time.sleep(20)  # ⏳ Ensure user logs in
    print("✅ Logged into WhatsApp Web.")

    data = sheet.get_all_values()
    
    today = datetime.date.today()
    
    for row in data[1:]:  # ✅ Skipping first row (headers)
        name, dob, number, message_sent = row[0], row[4], row[6], row[-1]
        
        try:
            dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
        except ValueError:
            print(f"⚠️ Invalid DOB format for {name}. Skipping...")
            continue
        
        days_until_birthday = (dob_date.replace(year=today.year) - today).days
        
        if 0 <= days_until_birthday <= 10 and message_sent.strip().lower() != "true":
            print(f"🎉 Sending birthday messages to {name} ({number})...")
            send_whatsapp_message(driver, number, name)
            
            row_index = data.index(row) + 1
            sheet.update_acell(f"H{row_index}", "TRUE")
            print(f"✅ Updated 'message_sent' status for {name}.")

    print("✅ All eligible messages sent. Exiting...")
    driver.quit()

if __name__ == "__main__":
    print("🚀 Starting WhatsApp Bot Scheduler...")
    run_bot()
