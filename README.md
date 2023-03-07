# Send Emails with Python
This code allows you to send an email with an attachment using the SMTP protocol. It imports the necessary modules and defines the sender and recipient email addresses, email password, subject, and body of the email.

## Description
This Python code sends an email message with an attachment using the Simple Mail Transfer Protocol (SMTP). It uses the `EmailMessage` class from the `email.message` module to create an email message object, attaches an image to the email, and sends it to the recipient using the Gmail SMTP server.

## Requirements
* Python 3.4 or higher
* Python Certificates installed using the `Install Certificated.command` file included with your Python installer
* The `os`, `email.message`, `ssl`, and `smtplib` modules are required.

## Usage
1. Replace the placeholders for `sender_email`, `email_password`, `recipient_email`, `subject`, and `body` with actual values for the sender email address, email password, recipient email address, email subject, and email body, respectively.
2. Replace the filename `foto.jpeg` with the name of the file you want to attach.
3. Run the code.

## Code Explanation
The code can be divided into several parts:

### Importing Modules
```python
import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr
```

These lines of code import the necessary modules for the script to run.
* `os`: Provides a way of interacting with the operating system.
* `EmailMessage`: Provides the ability to create email messages.
* `ssl`: Provides a way of establishing a secure SSL context for the SMTP connection.
* `smtplib`: Provides an interface to the SMTP server.
* `imghdr`: Provides a way of determining the type of image file.

### Setting Email Details
```python
sender_email = ''
email_password = ''

recipient_email = ''

subject = ''
body = """
Replace this text with the body of your email
"""
```
These lines of code define the sender email address, email password, recipient email address, email subject, and email body. Replace the placeholders with actual values.

### Creating an Email Message Object
```python
em = EmailMessage()
em['From'] = sender_email
em['To'] = recipient_email
em['Subject'] = subject
em.set_content(body)
```

These lines of code create an email message object using the `EmailMessage` class. The `From`, `To`, `Subject`, and `Content` fields are set using the object's attributes.

### Attaching an Image
```python
with open('foto.jpeg', 'rb') as file:
    file_data = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name

em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')
```

These lines of code read an image file and attach it to the email message. Replace the filename `foto.jpeg` with the name of the file you want to attach.

### Establishing a Secure Connection
```python
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, email_password)
    smtp.sendmail(sender_email, recipient_email, em.as_string())
```

These lines of code establish a secure SSL connection to the SMTP server and send the email message. The `ssl.create_default_context()` method creates a default SSL context with the appropriate security settings. The `smtplib.SMTP_SSL()` method creates an SMTP_SSL object that establishes a secure connection to the SMTP server. The `login()` method logs in to the sender email address. The `sendmail()` method sends the email message to the recipient.