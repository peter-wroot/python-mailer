# python-mailer

A simple Python script for sending emails based on HTML files. 

## Command-line switches

|Switch |Function           |
|-      |-                  |
|`-s`   |Sender Address     |
|`-r`   |Recipient Address  |
|`-S`   |SMTP Relay         |
|`-H`   |Path to HTML file  |

## Usage

`python-mailer.py -s sender@example.com -r recipient@example.com -S mail.example.com -H /home/user/templates/message.html`
