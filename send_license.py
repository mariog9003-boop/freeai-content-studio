import hashlib
import smtplib
from json import loads
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

# 🔒 MASTER SECURITY KEYS (Must match your app.py tokens)
SECRET_SALT = "MA_RE_O_2026_SECURITY_TOKEN_V1"

# 📧 AUTOMATED EMAIL OUTBOUND DISPATCH PERMISSIONS
SMTP_SERVER = "://gmail.com"             # Use ://yahoo.com for Yahoo, etc.
SMTP_PORT = 587
SENDER_EMAIL = "your-business-email@gmail.com"  # ⚠️ Replace with your active sender email
SENDER_PASSWORD = "your-app-password"          # ⚠️ Replace with your secret 16-character App Password

def generate_hardware_license(hardware_id):
    """Calculates the unique signature key mathematically tied to the buyer's machine ID."""
    clean_id = hardware_id.strip().upper()
    secure_hash = hashlib.sha256(f"{clean_id}-{SECRET_SALT}".encode()).hexdigest()
    return secure_hash[:12].upper()

def dispatch_license_email(buyer_email, buyer_name, hardware_id):
    """Compiles and automatically sends the activation key straight to the buyer's inbox."""
    premium_passcode = generate_hardware_license(hardware_id)
    
    subject = "🚀 Your FreeAI Content Studio Pro Lifetime Activation Key!"
    body = f"""Hi {buyer_name},

Thank you for your premium upgrade purchase! Your payment was processed successfully.

Because each license is strictly non-shareable and locked directly to your device browser structure, your custom activation credentials have been generated below:

📱 YOUR DEVICE ID: {hardware_id.upper()}
🔑 PREMIUM ACTIVATION KEY: {premium_passcode}

🛠️ How to activate your workspace:
1. Open your web app layout: https://streamlit.app
2. Expand the left-hand sidebar menu panel.
3. Paste this key code string directly into the 'Activation Key' text field box.

Your 15+ advanced creator styles, long-form copy text processing matrix engines, and unlimited execution speeds are now permanently active!

If you need any technical assistance, reply directly to this message.

Best regards,
Mario Gonzalez
Founder, FreeAI Content Studio Pro"""

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = buyer_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure network encryption layers
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, buyer_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending automatic email execution string: {str(e)}")
        return False

# --- WEBHOOK LISTENER HOOK ---
# This part intercepts the live transaction tracking payload from Buy Me a Coffee
if "payload" in st.query_params:
    try:
        raw_data = st.query_params.get("payload")
        json_payload = loads(raw_data)
        
        buyer_email = json_payload["response"]["supporter_email"]
        buyer_name = json_payload["response"].get("supporter_name", "Valued Customer")
        customer_device_id = json_payload["response"].get("custom_fields", {}).get("Device ID", "UNKNOWN")
        
        if customer_device_id != "UNKNOWN":
            dispatch_license_email(buyer_email, buyer_name, customer_device_id)
            st.write("🟢 Automation Dispatch Matrix Execution Complete.")
    except Exception as e:
        st.write(f"🔴 Automation Parsing Loop Idle: {str(e)}")
