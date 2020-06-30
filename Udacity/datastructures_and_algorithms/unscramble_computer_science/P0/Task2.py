"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from collections import defaultdict
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
calls_dict = defaultdict(int)
for entry in calls:
    calls_dict[entry[0]] += int(entry[3])
    calls_dict[entry[1]] += int(entry[3])

phone_no = max(calls_dict, key = lambda item: calls_dict[item])
longest_time = calls_dict[phone_no]

print(f"{phone_no} spent the longest time, {longest_time} seconds, on the phone during September 2016.")
