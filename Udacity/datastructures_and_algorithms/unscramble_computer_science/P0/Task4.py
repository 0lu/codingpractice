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

set_telemarketers = { entry[0] for entry in calls }

for entry in texts:
    if entry[0] in set_telemarketers:
        set_telemarketers.remove(entry[0])
    if entry[1] in set_telemarketers:
        set_telemarketers.remove(entry[1])

for entry in calls:
    if entry[1] in set_telemarketers:
        set_telemarketers.remove(entry[1])

list_telemarketers = list(set_telemarketers)
list_telemarketers.sort()

print("These numbers could be telemarketers: ")
for entry in list_telemarketers:
    print(entry)
