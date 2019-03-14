import smtplib,argparse,socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("-s","--sender") 
argument_parser.add_argument("-r","--recipient") 
argument_parser.add_argument("-S","--SMTPRelay") 
argument_parser.add_argument("-H","--HTML")
arguments = argument_parser.parse_args()

sender_email_address = arguments.sender
recipient_email_address = arguments.recipient
smtp_relay_address = arguments.SMTPRelay

email_message = MIMEMultipart('alternative')
email_message['Subject'] = "Test Email"
email_message['From'] = sender_email_address
email_message['To'] = recipient_email_address

if(arguments.HTML == None):
    message_body = "No content was provided for this message"
    email_message.attach(MIMEText(message_body,'plain'))
else:
    message_body = ""
    message_html = open(arguments.HTML)
    for line in message_html:
        print(line.rstrip())
        message_body += (line)   
    email_message.attach(MIMEText(message_body,'html'))
    
email_message.attach(MIMEText(message_body,'html'))

smtp_relay = smtplib.SMTP("mx1.mtaroutes.com")
smtp_relay.sendmail(sender_email_address,recipient_email_address,email_message.as_string())




