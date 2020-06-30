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
phone_set = set()

for entry in texts:
    phone_set.add(entry[0])
    phone_set.add(entry[1])

for entry in calls:
    phone_set.add(entry[0])
    phone_set.add(entry[1])

print(f"There are {len(phone_set)} different telephone numbers in the records.")