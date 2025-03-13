📢 NSS (NRPF) WhatsApp Automation System
📌 Project Description
This automation system is designed for NSS (NRPF) activities to streamline WhatsApp messaging. It automatically sends birthday wishes along with images and voice messages to NSS members whose birthdays fall within the next 10 days, provided the message has not already been sent. The system fetches data from Google Sheets and updates the status once messages are successfully sent. Additionally, a separate script extracts and organizes birthday data month-wise into a text file.

🛠️ Features
✅ Automated WhatsApp Messaging – Sends text, images, and voice messages to designated members.
✅ Google Sheets Integration – Fetches and updates data dynamically.
✅ Smart Scheduling – Sends messages 10 days before birthdays on a random day.
✅ Message Status Tracking – Updates message delivery status in Google Sheets.
✅ Debugging & Live Monitoring – Displays real-time logs for each message sent.
✅ Birthday List Extraction – Saves monthly birthday details into a text file, sorted by date.
✅ Error Handling & Authentication – Manages token expiry and missing data effectively.

🚀 Installation Guide
1️⃣ Prerequisites
Ensure you have the following installed on your system:

Python 3.10+
Google Chrome
Chrome WebDriver (Ensure compatibility with your Chrome version)
2️⃣ Clone the Repository
  git clone https://github.com/jerry53779/NSS-WhatsApp-Automation.git
  cd NSS-WhatsApp-Automation
3️⃣ Install Required Packages
Run the following command to install the dependencies:
  pip install -r requirements.txt
4️⃣ Set Up Google Authentication
Obtain API Credentials:

Go to Google Cloud Console.
Create a new project and enable Google Sheets API and Google Drive API.
Download the credentials.json file and place it inside the project directory.
Authenticate for the First Time:

Run the script to authenticate your Google account.
A browser window will open for authorization.
Once authorized, a token.json file will be created and used for future authentications.
📝 Usage Instructions
✅ Running the WhatsApp Bot
1.Open WhatsApp Web on Chrome and scan the QR code manually.
2.Ensure that Chrome WebDriver is installed and placed in the correct path.
3.Run the following command to start the bot:
  python whatsapp_bot.py
4.The bot will:
  Check for birthdays in the next 10 days
  Send messages only if "message_sent" is not "TRUE"
  Send text, image, and voice messages
  Update the Google Sheet with the sent status

🛠️ Troubleshooting
Issue	Solution
invalid_client: Unauthorized ->	Delete token.json and re-authenticate.
No such element: Unable to locate input field	-> Ensure WhatsApp Web is logged in and the correct XPath is used.
Messages are not being sent ->	Increase the wait time between actions to allow WhatsApp to load properly.
Invalid DOB format ->	Ensure the DOB format in Google Sheets is YYYY-MM-DD.
Chrome WebDriver not found ->	Download and place chromedriver.exe in the project directory.

