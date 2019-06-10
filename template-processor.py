# Import required libraries. 
import bs4, argparse, os

# Command-Line Arguments. 
argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("--input")
argumentParser.add_argument("--output")
argumentParser.add_argument("--seek",      nargs='+',  default=[])
argumentParser.add_argument("--replace",   nargs='+',  default=[])
arguments = argumentParser.parse_args()

# Checks to see if the user has provided the same number of argument
# For both 'seek' and 'replace'
if len(arguments.seek) != len(arguments.replace):
    print("ERROR: count of 'seek' arguments does not equal count of 'replace' arguments")
    exit()

# Read in the template file.
openTemplateFile = open(arguments.input,"r")
openTemplateContents = openTemplateFile.read()

# Function to run through the input file and replace text. 
def processSeekArgument(templateContents):
    for i in range(0, len(arguments.seek)):
        templateContents = templateContents.replace(arguments.seek[i],arguments.replace[i])
    return templateContents

# Writes the completed report to disk. 
completeReportFile = open(str(arguments.output),"w")
completeReportFile.write(processSeekArgument(openTemplateContents))