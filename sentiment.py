import re
import os
import csv
#from analyser import dataset,feature_set,no_of_items
import analyser
# To calculate the basic probability of a word for a category
def calc_prob(word,category):

	if word not in analyser.feature_set or word not in analyser.dataset[category]:
		return 0

	return float(analyser.dataset[category][word])/analyser.no_of_items[category]


# Weighted probability of a word for a category
def weighted_prob(word,category):
	# basic probability of a word - calculated by calc_prob
	basic_prob=calc_prob(word,category)

	# total_no_of_appearances - in all the categories
	if word in analyser.feature_set:
		tot=sum(analyser.feature_set[word].values())
	else:
		tot=0
		
	# (weight*assumedprobability + total_no_of_appearances*basic_probability)/(total_no_of_appearances+weight)
	# weight by default is taken as 1.0
	# assumed probability is 0.5 here
	weight_prob=((1.0*0.5)+(tot*basic_prob))/(1.0+tot)
	return weight_prob


# To get probability of the test data for the given category
def test_prob(test,category):
	# Split the test data
	split_data=re.split('[^a-zA-Z][\'][ ]',test)
	
	data=[]
	for i in split_data:
		if ' ' in i:
			i=i.split(' ')
			for j in i:
				if j not in data:
					data.append(j.lower())
		elif len(i) > 2 and i not in data:
			data.append(i.lower())

	p=1
	for i in data:
		p*=weighted_prob(i,category)
	return p

# Naive Bayes implementation
def naive_bayes(test):
	'''
		p(A|B) = p(B|A) * p(A) / p(B)
		Assume A - Category
			   B - Test data
			   p(A|B) - Category given the Test data	'''
	results={}
	for i in analyser.dataset.keys():
		# Category Probability
		# Number of items in category/total number of items
		cat_prob=float(analyser.no_of_items[i])/sum(analyser.no_of_items.values())

		# p(test data | category)
		test_prob1=test_prob(test,i)

		results[i]=test_prob1*cat_prob

	return results

positive = 0 #initialize positive comments counter
negative = 0 #initialize negative comments counter
counter = 0 # for counting number of reviews for a particular product
overall= 0 #for overall review
print("Enter Product Name")
text=input() #take input
asin_read=open("asin.csv" , 'r')
asin_reader = csv.reader(asin_read)

for asin in asin_reader:
	if asin[1] == text:
		product_name = asin[0]

cellphone_read=open("cellphone_15000.csv" , 'r') #open csv file to test the model
reader = csv.reader(cellphone_read) #read the csv file 

rows = [row for row in reader if row[0] == product_name] #store only those rows whoes entered ASIN number is same as asin number in csv file
counter = len(list(rows)) #counting total number of reviews for a entered product
for read in rows: #read those rows whos ASIN number is matched
	try:		
		text=read[4] #read only review text column from csv file
		result=naive_bayes(text) #give the comment to function
		if result['1'] > result['-1']:
			positive += 1 #increment the positive counter if comment is positive
		else:
			negative += 1 #increment the negative counter if comment is negative
		overall_review = read[3]
		overall += float(overall_review) 
		average_review = overall/counter
	except IndexError:
		text='null'
print("positive comments")
print (positive)
print("negative comments")
print (negative)
print("overall review")
print (average_review)
