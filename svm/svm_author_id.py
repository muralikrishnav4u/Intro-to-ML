#!/usr/bin/python
"""
    Using SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0    Chris has label 1
"""
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
############     SVM     #############
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

clf = SVC(C=10000.0, kernel = "rbf") #linear/rbf/

t0 = time()
clf.fit(features_train, labels_train) 
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predecting time:", round(time()-t1, 3), "s"
print "train features:%r train labels:%r test features:%r train labels:%r "% (len(features_train), len(labels_train), len(features_test), len(labels_test))
#type 1       #acc = clf.score(features_test, labels_test)
              #def submitAccuracy():
              #    return acc
#type 2       #print "accuracy of the model: %r" % clf.score(features_test, labels_test)
print "accuracy of the model: %r" % accuracy_score(labels_test, pred)
print len(pred)
print sum(pred)
type(pred)
print "output is: %r" % pred[10] 
print "output is: %r" % pred[26]
print "output is: %r" % pred[50]

#########################################################
