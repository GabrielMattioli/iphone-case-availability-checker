# iPhone Case Availability Checker

An automated tool that monitors dbrand's website for iPhone case availability and sends email notifications when the product is in stock.

## Description

This Python script periodically checks the availability of iPhone cases on dbrand's website. When the product becomes available, it sends an email notification to the specified recipient.

## Features

- Automated checking of product availability
- Email notifications when the product is in stock
- Configurable check interval
- Logging for monitoring and debugging

## Requirements

- Python 3.x
- Required Python packages:
  - requests
  - beautifulsoup4
  - schedule

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/iphone-case-availability-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd iphone-case-availability-checker
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `private_config/config.py` file with the following content:
   ```python
   SENDER_EMAIL = 'your_email@example.com'
   EMAIL_PASSWORD = 'your_email_password'
   RECIPIENT_EMAIL = 'recipient@example.com'
   ```
2. Adjust the `URL` and `CHECK_INTERVAL` variables in `iphone_case_notifier.py` if needed.

## Usage

Run the script:

```bash
python iphone_case_notifier.py
```