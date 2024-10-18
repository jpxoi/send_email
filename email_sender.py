import argparse
import logging
from src.email_service import EmailSender
from src.logger import setup_logging

def main():
    setup_logging()  # Set up logging
    parser = argparse.ArgumentParser(description='Send an email with an optional image attachment.')
    parser.add_argument('recipient_email', nargs='?', help='Recipient email address')
    parser.add_argument('subject', nargs='?', help='Email subject')
    parser.add_argument('body', nargs='?', help='Email body')
    parser.add_argument('--attachment', help='Path to image attachment (optional)', default=None)

    args = parser.parse_args()

    sender_email = input("Enter your email: ")
    email_password = input("Enter your email password: ")

    # Check for Gmail address
    if '@gmail.com' not in sender_email:
        print("Error: This application only supports Gmail accounts.")
        logging.error("Error: This application only supports Gmail accounts.")
        return

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
