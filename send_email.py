import os
import ssl
import smtplib
import mimetypes
import argparse
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

        return em

    def send_email(self, recipient_email, subject, body, attachment_path=None):
        em = self.create_email(recipient_email, subject, body, attachment_path)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender_email, self.email_password)
            smtp.sendmail(self.sender_email, recipient_email, em.as_string())
            print(f'Email sent to {recipient_email}.')


def main():
    parser = argparse.ArgumentParser(description='Send an email with an optional image attachment.')
    parser.add_argument('recipient_email', nargs='?', help='Recipient email address')
    parser.add_argument('subject', nargs='?', help='Email subject')
    parser.add_argument('body', nargs='?', help='Email body')
    parser.add_argument('--attachment', help='Path to image attachment (optional)', default=None)

    args = parser.parse_args()

    sender_email = input("Enter your email: ")
    email_password = input("Enter your email password: ")

    email_sender = EmailSender(sender_email, email_password)

    # Check if command-line arguments are provided
    if args.recipient_email and args.subject and args.body:
        email_sender.send_email(args.recipient_email, args.subject, args.body, args.attachment)
    else:
        # Interactive input
        recipient_email = input("Enter recipient email: ")
        subject = input("Enter subject: ")
        body = input("Enter body: ")
        attachment_path = input("Enter path to attachment (optional, press Enter to skip): ")

        email_sender.send_email(recipient_email, subject, body, attachment_path or None)


if __name__ == '__main__':
    main()
