
# 📌 NRPF WhatsApp Automation System

## 🚀 Overview  
This project automates WhatsApp messaging for **NSS (NRPF) activities**, ensuring timely delivery of **birthday wishes, images, and voice messages**. The system integrates with **Google Sheets**, dynamically scheduling messages based on upcoming birthdays.

---

## 🎯 Features  
✅ **Automated Birthday Messages** – Sends messages **10 days before** birthdays.  
✅ **Google Sheets Integration** – Fetches **Name, DOB, and WhatsApp Number** from a spreadsheet.  
✅ **Dynamic Scheduling** – Sends messages **randomly** within the 10-day window.  
✅ **Media Support** – Supports **text, images, and voice messages**.  
✅ **Status Tracking** – Updates **message_sent** status in Google Sheets.  
✅ **Annual Reset** – Resets sent statuses on **New Year's Day**.  
✅ **Live Debug Logging** – Displays real-time message-sending status.  
✅ **Birthday List Extraction** – Generates a **sorted list** of birthdays by month and status.  

---

## 🛠️ Installation Guide  

### 1️⃣ Clone the Repository  
git clone https://github.com/jerry53779/NRPF_WhatsApp_Automation.git
cd NRPF_WhatsApp_Automation

### 2️⃣ Install Required Dependencies  
Ensure you have **Python 3.x** installed, then run:  

pip install -r requirements.txt

### 3️⃣ Set Up Google Sheets API  
- Enable **Google Sheets API** and **Google Drive API** from the [Google Cloud Console](https://console.cloud.google.com/).  
- Download your \`credentials.json\` file and place it in the **project folder**.  
- The script will auto-generate a **token.json** file after authentication.

### 4️⃣ Update Google Sheets Configuration  
- Open the script and update \`SPREADSHEET_ID\` with your **Google Sheet ID**.  
- Ensure your **Google Sheet has the following columns**:  
  - **Column A:** Name  
  - **Column E:** DOB (Format: \`YYYY-MM-DD\`)  
  - **Column G:** WhatsApp Number  
  - **A column for message_sent status** (ensure the script finds it dynamically).  

---

## 🚀 Running the WhatsApp Bot  

### Step 1: Open WhatsApp Web Manually  
- Open [https://web.whatsapp.com](https://web.whatsapp.com/) and **scan the QR code** manually.  
- Keep WhatsApp Web **logged in** before running the bot.  

### Step 2: Run the Automation Script  
python whatsapp_bot.py

✅ **What This Does**:  
- Fetches data from Google Sheets.  
- Sends messages to people whose **birthdays are within the next 10 days**.  
- Updates the **message_sent** status.  

---

## 📌 Debugging & Live Status  
- The bot now **logs each message's status live**.  
- If a message fails, it prints **detailed error logs** for debugging.  
- A **30-second wait time** is added to prevent fast reload issues.  

---

## 📂 File Structure  
\`\`\`
📂 NRPF_WhatsApp_Automation
 ├── 📜 whatsapp_bot.py            # Main script for sending messages
 ├── 📜 requirements.txt           # Required dependencies
 ├── 📜 credentials.json           # Google API credentials (not included)
 ├── 📜 token.json                 # OAuth token (auto-generated)
 ├── 📜 README.md                  # Documentation
\`\`\`

---


