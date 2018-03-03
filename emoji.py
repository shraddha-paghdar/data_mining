import csv
import re

def stripNonAlphaNum(text):
    return re.compile(r'\W+', re.UNICODE).split(text)     # Given a text string, remove all non-alphanumeric characters (using Unicode definition of alphanumeric).

emoji_read=open("emoji.csv" , 'r') #open csv file to test the model
reader = csv.reader(emoji_read) #read the csv file

print('enter the symbol')
symbol = input()
symbol_unicode=symbol.encode('unicode-escape') 
data=symbol_unicode.decode()
testing_data=stripNonAlphaNum(data)
for row in reader:
	for x in testing_data:
		if row[0] == x:
			print(row[1])



# counter = 0
# overall= 0 #initialize positive comments counter
# print("Enter ASIN number")
# text=input() #take input
# cellphone_read=open("cellphone_15000.csv" , 'r') #open csv file to test the model
# reader = csv.reader(cellphone_read) #read the csv file 
# rows = [row for row in reader if row[0] == text] #store only those rows whoes entered ASIN number is same as asin number in csv file
# counter = len(list(rows))
# for read in rows: #read those rows whos ASIN number is matched
# 	try:		
# 		overall_review = read[3]
# 		overall += float(overall_review) 
# 		average_review = overall/counter
# 	except IndexError:
# 		text='null'
# print("overall review")
# print(counter)
# print (average_review)