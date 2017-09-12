#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts). The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }
    {features_dict} is a dictionary of features associated with that person.
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print(enron_data)
#print str(enron_data)
print 'Type of enron dataset is :', type(enron_data)
print "No. of persons in the dataset: %r" % len(enron_data)
print 'Number of features per person: {0}'.format(len(enron_data.values()[0]))
print 'Number of features per person: {0}'.format(enron_data.items()[0])
# How many POIs are there in the E+F dataset?
print 'No. of actual POIs(E+F dataset):', len(dict((key, value) for key, value in enron_data.items() if value["poi"]))
#print 'Number of POI\'s:', len([x for x, y in enron_data.items() if y['poi']])
# How many POIs are there in total?
poi_reader = open('../final_project/poi_names.txt', 'r')
poi_reader.readline() # skip url
poi_reader.readline() # skip blank line
poi_count = 0
for poi in poi_reader:
	poi_count += 1
print 'no. of POIs hand picked are:', poi_count
print "Total value of stocks belonging to James Prentice:", enron_data["PRENTICE JAMES"]['total_stock_value']
print "Emails from Wesley Colwell to POI:", enron_data['COLWELL WESLEY']["from_this_person_to_poi"]
print "Value of stock options exercised by Jeffrey K Skilling:", enron_data['SKILLING JEFFREY K']['exercised_stock_options']
# Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)? How much money did that person get?
most_paid = 'murali'
highest_payment = 0
for key in ('LAY KENNETH L', 'FASTOW ANDREW S', 'SKILLING JEFFREY K'):
    if enron_data[key]['total_payments'] > highest_payment:
        highest_payment = enron_data[key]['total_payments']
        most_paid = key
print "%r took most money and he took away home: %r" %(most_paid, highest_payment)
# How many have quantified salary
print "folks with quantified salary:", len(dict((key,value) for key,value in enron_data.items() if value['salary']!= 'NaN')) 
print "folks with known email address:", len(dict((key,value) for key,value in enron_data.items() if value['email_address']!= 'NaN'))
no_total_payments = len(dict((key,value) for key,value in enron_data.items() if value['total_payments'] == 'NaN'))
print "folks with no payments: ", float(no_total_payments)/len(enron_data) * 100, "%"
#How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
POIs = dict((key,value) for key, value in enron_data.items() if value['poi'] == True)
number_POIs = len(POIs)
print "No. of actual POIs:", number_POIs
no_total_payment = len(dict((key, value) for key, value in POIs.items() if value["total_payments"] == 'NaN'))
print "POIs in the E+F dataset have “NaN” for their total payments:", no_total_payment
print "percentage of POI’s as a whole", float(no_total_payment)/number_POIs * 100, "%"
