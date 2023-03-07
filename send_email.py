import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

sender_email = ''
email_password = ''

recipient_email = ''

subject = ''
body = """
Replace this text with the body of your email
"""

em = EmailMessage()
em['From'] = sender_email
em['To'] = recipient_email
em['Subject'] = subject
em.set_content(body)

# Attachment
with open('foto.jpeg', 'rb') as file:
    file_data = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name

em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, email_password)
    smtp.sendmail(sender_email, recipient_email, em.as_string())