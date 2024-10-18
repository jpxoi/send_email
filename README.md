# Email Sender

A simple email sender application built in Python that allows you to send emails with optional image attachments using Gmail's SMTP server. The application can be run interactively or with command-line arguments.

## Features

- Send emails with or without attachments
- Interactive input for email details
- Command-line interface for quick usage
- Basic error handling and logging
- Modular structure for easy maintenance

## Prerequisites

- Python 3.x
- A Gmail account

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jpxoi/send_email.git
   cd send_email
   ```

2. **Install dependencies (if any):**
   - Currently, this application does not require any external libraries beyond the Python standard library, so no additional installation is needed.

## Usage

You can run the application in two ways: interactively or with command-line arguments.

### Interactive Mode

Simply run the script without any arguments:

```bash
python email_sender.py
```

You will be prompted to enter your email credentials and email details.

### Command-Line Arguments

You can also provide the recipient's email, subject, body, and an optional attachment directly from the command line:

```bash
python email_sender.py recipient@example.com "Subject Here" "Body of the email" --attachment path/to/attachment.jpeg
```

### Example

To send an email with an attachment:

```bash
python email_sender.py recipient@example.com "Hello" "This is a test email" --attachment path/to/image.jpg
```

To send an email without an attachment:

```bash
python email_sender.py recipient@example.com "Hello" "This is a test email"
```

## Logging

All events, including errors, are logged to `email_sender.log` in the same directory as the script.

## Important Notes

- This application currently only supports sending emails from Gmail accounts. Ensure you use a valid Gmail address.
- Make sure to allow "Less secure apps" in your Google account settings to use this application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
