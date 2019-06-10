# python-mailer

A simple Python script for sending emails based on HTML files. 

## Command-line switches

|Switch          |Function           |
|-               |-                  |
|`--sender`      |Sender Address     |
|`--recipient`   |Recipient Address  |
|`--relay`       |SMTP Relay         |
|`--html`        |Path to HTML file  |
|`--subject`     |Email Subject Line |

## Usage

`python python-mailer.py \`  
`-s sender@example.com \`  
`-r recipient@example.com \`  
`-S mail.example.com \`  
`-H /home/user/templates/message.html \`  

# template-processor

A simple template-processor.py script is also included. This script will replace an arbitrary number of strings within a text-based template file with substitute strings provided by the user. The items are substituted based on their index in each array (index 0 in the "seek" array will be replaced in index 0 in the "replace" array, and so on.)

## Command-line switches

|Switch         |Function                           |
|-              |-                                  |
|`--input`      |Path to template file.             |
|`--output`     |Path to save the completed file to |
|`--seek`       |List of strings to replace         |
|`--replace`    |List of substitute strings         |

## Usage

`python3 template-processor.py \`  
`--input input.html \`  
`--output output.html \`  
`--seek item1 item2 item3 \`  
`--replace sub1 sub2 sub3 \`  