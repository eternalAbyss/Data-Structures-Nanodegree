"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
maxDuration = 0
maxCallDetails = ()

for call in calls:
    if int(call[3]) > maxDuration:
        maxDuration = int(call[3])
        maxCallDetails = call

outputStr = "{} spent the longest time, {} seconds, on the phone during September 2016."
print(outputStr.format(maxCallDetails[0], maxCallDetails[3]))
