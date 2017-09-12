#!/usr/bin/python
""" Using Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0  and   Chris has label 1
"""
import sys
#from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#######         Decision tress       ########

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

print len(features_train[0])
from sklearn.metrics import accuracy_score
print "accuracy of the model: %r" % round((accuracy_score(pred, labels_test)),3)


