# sender.py
import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = os.getenv("BOT_EMAIL")
EMAIL_PASSWORD = os.getenv("BOT_EMAIL_PASS")

def send_email(to_email, message):
    msg = EmailMessage()
    msg["Subject"] = "Exciting Opportunity for You"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
