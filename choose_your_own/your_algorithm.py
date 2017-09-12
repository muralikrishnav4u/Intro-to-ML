#!/usr/bin/python
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]
#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()

### naming the classifier object clf and visualization code (prettyPicture) to show you the decision boundary

features_train, labels_train, features_test, labels_test = makeTerrainData()
########################## SVM #################################
### we handle the import statement and SVC creation for you here

t0 = time()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score

best_algorithm = None
best_accuracy_score = 0.0
best_kwargs = None
best_clf = None

# Training Random Forest Classifier

kwargs = {
	'n_estimators' : None,
	'criterion' : None,
	'max_features' : None,
	'max_depth' : None,
	'bootstrap' : None,
	'n_jobs' : -1
}

for n_estimators in range(1, 20):
	for criterion in ("gini", "entropy"):
		for max_features in ("auto", "sqrt", "log2", None):
			for max_depth in tuple(range(1, 11)) + (None,):
				for bootstrap in (True, False):
					kwargs['n_estimators'] = n_estimators
					kwargs['criterion'] = criterion
					kwargs['max_features'] = max_features
					kwargs['max_depth'] = max_depth
					kwargs['bootstrap'] = bootstrap

					clf = RandomForestClassifier(**kwargs)
					clf.fit(features_train, labels_train)
					pred = clf.predict(features_test)

					if accuracy_score(labels_test, pred) > best_accuracy_score:
						best_accuracy_score = accuracy_score(labels_test, pred)
						best_kwargs = kwargs
						best_algorithm = 'RandomForest'
						best_clf = clf

# Training AdaBoost Classifier 

kwargs = {
	'n_estimators' : None,
	'algorithm' : None
}

for n_estimators in range(40, 70):
	for algorithm in ("SAMME", "SAMME.R"):
		kwargs['n_estimators'] = n_estimators
		kwargs['algorithm'] = algorithm

		clf = AdaBoostClassifier(**kwargs)
		clf.fit(features_train, labels_train)
		pred = clf.predict(features_test)

		if accuracy_score(labels_test, pred) > best_accuracy_score:
			best_accuracy_score = accuracy_score(labels_test, pred)
			best_kwargs = kwargs
			best_algorithm = 'AdaBoost'
			best_clf = clf

# Training k-Nearest Neighbors Classifier

kwargs = {
	'n_neighbors' : None,
	'weights' : None,
	'algorithm' : None,
	'p' : None
}

for n_neighbors in range(1, 11):
	for weights in ('uniform', 'distance'):
		for algorithm in ("auto", "ball_tree", "kd_tree", "brute"):
			for p in (1, 2, 3):
				kwargs['n_neighbors'] = n_neighbors
				kwargs['weights'] = weights
				kwargs['algorithm'] = algorithm
				kwargs['p'] = p

				clf = KNeighborsClassifier(**kwargs)
				clf.fit(features_train, labels_train)
				pred = clf.predict(features_test)

				if accuracy_score(labels_test, pred) > best_accuracy_score:
					best_accuracy_score = accuracy_score(labels_test, pred)
					best_kwargs = kwargs
					best_algorithm = 'KNeighbors'
					best_clf = clf

# Training Naive Bayes Classifier

kwargs = None

clf = GaussianNB()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

if accuracy_score(labels_test, pred) > best_accuracy_score:
	best_accuracy_score = accuracy_score(labels_test, pred)
	best_kwargs = kwargs
	best_algorithm = 'GaussianNB'
	best_clf = clf

# Training Support Vector Classifier

kwargs = {
	'C' : None,
	'kernel' : None,
	'probability' : None,
	'shrinking' : None
}

import numpy as np

for C in np.arange(1.0, 3.5, 0.5):
	for kernel in ('linear', 'poly', 'rbf', 'sigmoid'):
		for probability in (True, False):
			for shrinking in (True, False):
				kwargs['C'] = C
				kwargs['kernel'] = kernel
				kwargs['probability'] = probability
				kwargs['shrinking'] = shrinking

				clf = SVC(**kwargs)
				clf.fit(features_train, labels_train)
				pred = clf.predict(features_test)

				if accuracy_score(labels_test, pred) > best_accuracy_score:
					best_accuracy_score = accuracy_score(labels_test, pred)
					best_kwargs = kwargs
					best_algorithm = 'SVC'
					best_clf = clf

print "The best classifier is", best_algorithm
print "With parameters:\n", best_kwargs
print "Accuracy:", best_accuracy_score

print "training time:", round(time()-t0, 3), "s"
try:
    prettyPicture(best_clf, features_test, labels_test)
except NameError:
    pass
