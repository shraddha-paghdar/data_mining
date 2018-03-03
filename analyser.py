import re
import csv

fh=open("dataset.CSV","r")
reader = csv.reader(fh, delimiter='/')
dataset={}
no_of_items={}
feature_set={}

for row in reader:
	no_of_items.setdefault(row[1],0)
	no_of_items[row[1]]+=1
	dataset.setdefault(row[1],{})
	split_data=re.split('[^a-zA-Z\']',row[0])
	
	for i in split_data:
		if len(i) > 2: #removing unnecessary words that are less than 2 characters
			dataset[row[1]].setdefault(i.lower(),0)
			
			dataset[row[1]][i.lower()]+=1  # Increase the word count on its occurence with label row[1]
			
			feature_set.setdefault(i.lower(),{})   # Initialze a dictionary for a newly found word in feature set
			
			feature_set[i.lower()].setdefault(row[1],0)
			
			feature_set[i.lower()][row[1]]+=1 # Increment the count for the word 

	


