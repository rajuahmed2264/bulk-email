import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_f(email_data):
    # SMTP server settings
    smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with your SMTP server port #ssl 465 no ssl 587
    smtp_username = 'ezekiel.chatchef@gmail.com'
    smtp_password = 'mnqs ozhw eheq gsfd'

    # Sender and recipient email addresses
    sender_email = 'ezekiel.chatchef@gmail.com'
    recipient_email = email_data["receipt_email"]

    # Create a message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = email_data["subject"]

    # Add the email body
    body = email_data["body"]
    msg.attach(MIMEText(body, 'html'))

    # Establish an SMTP connection and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)

        server.starttls()  # Use TLS encryption
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        success_message = True
        
        
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        success_message = False

    return success_message