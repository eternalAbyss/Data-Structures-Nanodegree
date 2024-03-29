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

duration_dict = {}
for call in calls:
    if call[0] in duration_dict:
        duration_dict[call[0]] += int(call[3])
    else:
        duration_dict[call[0]] = int(call[3])
    if call[1] in duration_dict:
        duration_dict[call[1]] += int(call[3])
    else:
        duration_dict[call[1]] = int(call[3])

maxDuration = max(duration_dict.values())
number_list = list(duration_dict.keys())
duration_list = list(duration_dict.values())
index = duration_list.index(maxDuration)

outputStr = "{} spent the longest time, {} seconds, on the phone during September 2016."
print(outputStr.format(number_list[index], duration_list[index]))
