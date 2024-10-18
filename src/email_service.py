import os
import ssl
import smtplib
import mimetypes
import logging
from email.message import EmailMessage

class EmailSender:
    def __init__(self, sender_email, email_password):
        self.sender_email = sender_email
        self.email_password = email_password

    def create_email(self, recipient_email, subject, body, attachment_path=None):
        em = EmailMessage()
        em['From'] = self.sender_email
        em['To'] = recipient_email
        em['Subject'] = subject
        em.set_content(body)

        if attachment_path and os.path.exists(attachment_path):
            mime_type, _ = mimetypes.guess_type(attachment_path)
            if mime_type is not None:
                maintype, subtype = mime_type.split('/', 1)
                with open(attachment_path, 'rb') as file:
                    file_data = file.read()
                    em.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=os.path.basename(attachment_path))
            else:
                logging.warning(f'Could not determine MIME type for attachment: {attachment_path}')

        return em

    def send_email(self, recipient_email, subject, body, attachment_path=None):
        try:
            em = self.create_email(recipient_email, subject, body, attachment_path)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(self.sender_email, self.email_password)
                smtp.sendmail(self.sender_email, recipient_email, em.as_string())
                logging.info(f'Email sent to {recipient_email}.')
        except smtplib.SMTPAuthenticationError:
            logging.error('Authentication error: check your email and password.')
            print('Authentication error: check your email and password.')
        except smtplib.SMTPRecipientsRefused:
            logging.error(f'Recipient refused: {recipient_email}')
            print(f'Recipient refused: {recipient_email}')
        except Exception as e:
            logging.error(f'Error sending email: {e}')
            print(f'Error sending email: {e}')
