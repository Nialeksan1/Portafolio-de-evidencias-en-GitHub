import smtplib, ssl, getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import E

try:
    sender_email = input('From: ')
    receiver_email = input('To: ')
    password = getpass.getpass('Password: ')
    subject = input('Subject: ')
    filename = input('Attachment root: ')
    body = input('Compose email:\n')
    print('\nPlease wait until mail is sent . . .')

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message['Bcc'] = receiver_email

    #Add body to email
    message.attach(MIMEText(body, 'plain'))

    with open(filename, 'rb') as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    name = filename.split('\\')[-1]
    part.add_header('content-disposition', 'attachment', filename=name)

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    if '@gmail.com' in sender_email:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
    else:
        with smtplib.SMTP('smtp.outlook.office365.com', 587, timeout=20) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
    print('\nDone!')
except Exception as e:
    raise e