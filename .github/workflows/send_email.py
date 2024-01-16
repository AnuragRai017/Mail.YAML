# Example script to send email using smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(request):
    # Email configuration
    sender_email = "your_outlook_email@example.com"
    receiver_email = "jprogramming04@gmail.com"
    subject = "Scheduled Email"
    body = "Hello, this is a scheduled email from Google Cloud Functions!"

    # ... (rest of your email sending code)

    return "Email sent successfully!"
