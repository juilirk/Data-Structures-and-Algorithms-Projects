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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def bangalore_call(call):
	return call[0][0:5]=='(080)'

def get_area_code(call):
	call_num=call[1]

	if call_num[0:2]=='(0':
		return call_num[1:call_num.find(')')]

	if call_num[:3]=='140':
		return 140
	if call_num[0]=='7' or call_num[0]=='8' or call_num[0]=='9':
		return call_num[:4]


if __name__ == '__main__':
	prefix=[]

	#Part A

	for call in calls:
		if bangalore_call(call):
			prefix.append(get_area_code(call))

	num_list = list(set(prefix))
	num_list.sort()
	print("\nThe numbers called by people in Bangalore have codes:")
	for num in num_list:
		print(num)

	#Part B

	count=0

	for num in prefix:
		if num[:5]=='080':
			count+=1

	print(f"\n{round(count/len(prefix)*100,2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
