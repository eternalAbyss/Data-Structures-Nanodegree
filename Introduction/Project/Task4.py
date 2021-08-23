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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Empty set initialization
callNumbersOut = {''}
callNumbersIn = {''}
textNumbersOut = {''}
textNumbersIn = {''}
telemarketingNumbers = {''}

# Separately storing incoming and outgoing call numbers
for call in calls:
    callNumbersOut.add(call[0])
    callNumbersIn.add(call[1])

# Separately storing incoming and outgoing text numbers
for text in texts:
    textNumbersOut.add(text[0])
    textNumbersIn.add(text[1])

# Removing empty fields from the set
callNumbersOut.remove('')
callNumbersIn.remove('')
textNumbersIn.remove('')
textNumbersOut.remove('')

# Checking if the numbers that called have received calls, texts or sent texts
for number in callNumbersOut:
    if not(number in textNumbersIn or number in textNumbersOut or number in textNumbersIn):
        telemarketingNumbers.add(number)

# Removing empty field from telemarketing numbers
telemarketingNumbers.remove('')

print("These numbers could be telemarketers: ")
for number in sorted(telemarketingNumbers):
    print(number)
