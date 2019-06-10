# Import required libraries.
import smtplib,argparse,socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Command-line arguments.
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--sender") 
argument_parser.add_argument("--recipient") 
argument_parser.add_argument("--relay") 
argument_parser.add_argument("--subject")
argument_parser.add_argument("--html")
arguments = argument_parser.parse_args()

# Creates the email message
email_message = MIMEMultipart('alternative')
email_message['Subject'] = arguments.subject
email_message['From'] = arguments.sender
email_message['To'] = arguments.recipient

# Checks if the user provided a HTMl file to use
# As the body of the email - if not, a line of
# Text explaining that no content was provided 
# Is added to the message. 
if(arguments.HTML == None):
    message_body = "No content was provided for this message"
    email_message.attach(MIMEText(message_body,'plain'))
else:
    message_body = ""
    message_html = open(arguments.html)
    for line in message_html:
        message_body += (line)   
    email_message.attach(MIMEText(message_body,'html'))

# Creates the SMTP Relay object. 
smtp_relay = smtplib.SMTP(str(arguments.relay))
# Sends the mail.
smtp_relay.sendmail(arguments.sender,arguments.recipient,email_message.as_string())




