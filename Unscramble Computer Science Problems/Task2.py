"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from datetime import datetime
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

'''
getting the call record during September 2016.
'''
def getByMonth(phoneCall, month, year):
	timeStamp= phoneCall[2]
	dt= datetime.strptime(timeStamp, '%d-%m-%Y %H:%M:%S')
	if(dt.year==year and dt.month==month):
		return True
	else:
		return False



records= filter(lambda x: getByMonth(x,9,2016),calls)


'''
finding the total duration spent by a phone
'''

def trackDuration(dictionary, phoneNumber, duration):
	if(dictionary.get(phoneNumber)==None):
		dictionary[phoneNumber]= int(duration)
	else:
		dictionary[phoneNumber] = dictionary.get(phoneNumber)+ int(duration)

	return dictionary


dictionary={}

for record in records:
	outgoingNumber=record[0]
	incomingNumber=record[1]
	timeStamp=record[2]
	duration=record[3]

	dictionary= trackDuration(dictionary,outgoingNumber,duration)
	dictionary= trackDuration(dictionary, incomingNumber,duration)


'''
get the details for the phone number that spent most time on phone during september 2016
'''

phoneMax = max(dictionary.items(), key=lambda x: int(x[1]))

print(f"{phoneMax[0]} spent the longest time, {phoneMax[1]} seconds, on the phone during September 2016.")



