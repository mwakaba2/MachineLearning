#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score 

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 


classifier = SVC(C=10000.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
    gamma=0.0, kernel='rbf', max_iter=-1, probability=False,
    random_state=None, shrinking=True, tol=0.001, verbose=False)

t0 = time()
classifier.fit(features_train, labels_train)
print "Training time: ", round(time() - t0, 3),"s"

t1 = time()
prediction = classifier.predict(features_test)
chris = [x for x in prediction if x == 1]
print(len(chris))

print "Predicting time: ", round(time() - t1, 3),"s"
score = accuracy_score(labels_test, prediction, normalize=True)
print score

	

