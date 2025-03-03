import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "yourburneremail@gmail.com"
EMAIL_PASSWORD = "your-email-password"
ATTACHMENT_PATH = "Resume_John_DOE.docm"

if not os.path.exists(ATTACHMENT_PATH):
    print(f"Error: File '{ATTACHMENT_PATH}' not found.")
    sys.exit(1)

TARGET = sys.argv[1]

if os.path.isfile(TARGET):
    with open(TARGET, "r") as f:
        email_list = [line.strip() for line in f.readlines() if line.strip()]
else:
    email_list = [TARGET]

email_subject = "Job Application - John Doe (Cybersecurity Engineer)"
email_body = """Dear Hiring Manager,

I hope this email finds you well. I am excited to apply for the Cybersecurity Engineer position at your company.
I have attached my resume in Word format for your review.

Don't forget to **enable macros** to properly view the content of my resume.

Please let me know if you need any additional information. I appreciate your time and consideration
and look forward to your response.

Best regards,  
John Doe  
"""


def send_email(recipient):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = recipient
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_body, 'plain'))

    with open(ATTACHMENT_PATH, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(ATTACHMENT_PATH)}")
    msg.attach(part)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, recipient, msg.as_string())
        server.quit()
        print(f"✅ Email successfully sent to {recipient}!")
    except Exception as e:
        print(f"❌ Error sending email to {recipient}: {e}")

for email in email_list:
    send_email(email)
