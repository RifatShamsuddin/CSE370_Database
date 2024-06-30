import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = 'smtp.example.com'  # SMTP server address
smtp_port = 587  # SMTP server port
sender_email = 'your_email@example.com'  # Sender's email address
sender_password = 'your_password'  # Sender's email password
receiver_email = 'recipient@example.com'  # Recipient's email address

subject = 'Automated Email'  # Email subject
message = 'Hello, this is an automated email.'  # Email body

# Create a multipart message
email = MIMEMultipart()
email['From'] = sender_email
email['To'] = receiver_email
email['Subject'] = subject

# Attach the message to the email
email.attach(MIMEText(message, 'plain'))

# Send the email
try:
    # Establish a secure connection with the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(email)
    print("Email sent successfully!")
except Exception as e:
    print("An error occurred while sending the email:", str(e))