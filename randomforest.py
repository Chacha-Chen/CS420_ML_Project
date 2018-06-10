import pandas as pd
import numpy as np
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#from nolearn.dbn import DBN
import timeit
import getdata

y_train = np.fromfile("./data/label_train",dtype=np.uint8)
y_test = np.fromfile("./data/label_test",dtype=np.uint8)

X_train = getdata.X_train
X_train_deskew = getdata.X_train_deskew

X_test = getdata.X_test
X_test_deskew = getdata.X_test_deskew

X_train_deskew_reducedn = getdata.X_train_deskew_reducedn
X_test_deskew_reducedn = getdata.X_test_deskew_reducedn

X_train_standard=getdata.X_train_standard
X_test_standard=getdata.X_test_standard

X_train_deskew_standard=getdata.X_train_deskew_standard
X_test_deskew_standard=getdata.X_test_deskew_standard

X_train_deskew_reducedn_standard=getdata.X_train_deskew_reducedn_standard
X_test_deskew_reducedn_standard=getdata.X_test_deskew_reducedn_standard

clf_rf = RandomForestClassifier()
clf_rf.fit(X_train, y_train)
y_pred_rf = clf_rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
print( "random forest accuracy: ",acc_rf)

clf_rf = RandomForestClassifier()
clf_rf.fit(X_train_standard, y_train)
y_pred_rf = clf_rf.predict(X_test_standard)
acc_rf = accuracy_score(y_test, y_pred_rf)
print( "random forest accuracy (standard): ",acc_rf)


clf_rfd = RandomForestClassifier()
clf_rfd.fit(X_train_deskew, y_train)
y_pred_rfd = clf_rfd.predict(X_test_deskew)
acc_rfd = accuracy_score(y_test, y_pred_rfd)
print( "random forest accuracy with dekewed data: ",acc_rfd)

clf_rfd = RandomForestClassifier()
clf_rfd.fit(X_train_deskew_standard, y_train)
y_pred_rfd = clf_rfd.predict(X_test_deskew_standard)
acc_rfd = accuracy_score(y_test, y_pred_rfd)
print( "random forest accuracy with dekewed+standard data: ",acc_rfd)

clf_rfd = RandomForestClassifier()
clf_rfd.fit(X_train_deskew_reducedn, y_train)
y_pred_rfd = clf_rfd.predict(X_test_deskew_reducedn)
acc_rfd = accuracy_score(y_test, y_pred_rfd)
print( "random forest accuracy with dekewed + reduced noise data: ",acc_rfd)

clf_rfd = RandomForestClassifier()
clf_rfd.fit(X_train_deskew_reducedn_standard, y_train)
y_pred_rfd = clf_rfd.predict(X_test_deskew_reducedn_standard)
acc_rfd = accuracy_score(y_test, y_pred_rfd)
print( "random forest accuracy with dekewed+ reduced noise + standard data: ",acc_rfd)






#from sklearn.grid_search import GridSearchCV
#from sklearn.cross_validation import StratifiedKFold
#
#def main():
#    mnist = fetch_mldata("MNIST original")
#    X_all, y_all = mnist.data/255., mnist.target
#    print("scaling")
#    X = X_all[:60000, :]
#    y = y_all[:60000]
#
#    X_test = X_all[60000:, :]
#    y_test = y_all[60000:]
#
#    svm = SVC(cache_size=1000, kernel='rbf')
#
#    parameters = {'C':10. ** np.arange(5,10), 'gamma':2. ** np.arange(-5, -1)}
#    print("grid search")
#    grid = GridSearchCV(svm, parameters, cv=StratifiedKFold(y, 5), verbose=3, n_jobs=-1)
#    grid.fit(X, y)
#    print("predicting")
#    print "score: ", grid.score(X_test, y_test)
#    print grid.best_estimator_
#
#if __name__ == "__main__":
#    main()