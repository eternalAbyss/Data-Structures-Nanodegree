"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

Numbers = set()

for text in texts:
    Numbers.add(text[0])
    Numbers.add(text[1])

for call in calls:
    Numbers.add(call[0])
    Numbers.add(call[1])

outputStr = "There are {} different telephone numbers in the records."
print(outputStr.format(len(Numbers)))
