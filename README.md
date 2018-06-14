# CS420 Course Project

## An Exploratory Study on MNIST dataset

<!--Data Preprocessing  | Accuracy
------------- | -------------
Original  | 0.1337
deskewed  | 0.6145
deskewed + noise reduced  | 0.9194-->

©Chacha Chen  
©Yunyan Hong   
©Yin Lin

- Data Preprocessing
	- image deskewing 
	- noise reduction
- Classical Learning Method:
 	 - Softmax, kNN, SVM, Random forest, Xgboost
	-  MLP, CNN, RNN, LSTM
	-  PCA , Autoencoder, k-Means

<!--##  softmax
### learning rate = 10
Accuracy: 0.1497  
Accuracy (deskewd): 0.6219  
Accuracy (deskewd+reduced noise): 0.8995

### learning rate = 1
Accuracy: 0.1262  
Accuracy (deskewd): 0.6452  
Accuracy (deskewd+reduced noise): 0.9118

### learning rate = 0.5
- Accuracy: 0.1337
- Accuracy (deskewd): 0.6145
- Accuracy (deskewd+reduced noise): 0.9194

### learning rate = 0.1
Accuracy: 0.1398  
Accuracy (deskewd): 0.6179  
Accuracy (deskewd+reduced noise): 0.9216

### learning rate = 0.01
Accuracy: 0.1370  
Accuracy (deskewd): 0.6401  
Accuracy (deskewd+reduced noise): 0.9113

### learning rate = 0.001
Accuracy: 0.1333  
Accuracy (standard): 0.2736  
Accuracy (deskewd): 0.5876  
Accuracy (deskewd + standard): 0.7233  
Accuracy (deskewd+reduced noise): 0.8820  
Accuracy (deskewd+reduced noise+standard): 0.9080

### learning rate = 0.01
Accuracy: 0.1370  
Accuracy (standard): 0.2559  
Accuracy (deskewd): 0.6401  
Accuracy (deskewd + standard): 0.7170  
Accuracy (deskewd+reduced noise): 0.9113  
Accuracy (deskewd+reduced noise+standard): 0.9198  
Accuracy (deskewd+reduced noise+standard+pca): 0.9199

### learning rate = 0.1
Accuracy: 0.1398  
Accuracy (standard): 0.1993  
Accuracy (deskewd): 0.6179  
Accuracy (deskewd + standard): 0.6500  
Accuracy (deskewd+reduced noise): 0.9216  
Accuracy (deskewd+reduced noise+standard): 0.9107  
Accuracy (deskewd+reduced noise+standard+pca): 0.9191

##  random-forest
random forest accuracy:  0.6919  
random forest accuracy (standard):  0.6465  
random forest accuracy with dekewed data:  0.8292  
random forest accuracy with dekewed+standard data:  0.8344  
random forest accuracy with dekewed + reduced noise data:  0.9532  
random forest accuracy with dekewed+ reduced noise + standard data:  0.5347


##  linear-svm with SGD
 
stochastic gradient descent accuracy:  0.1359   
stochastic gradient descent accuracy with standard data:  0.2186   
stochastic gradient descent accuracy with deskewed data:  0.5942   
stochastic gradient descent accuracy with deskewed + standard data:  0.7171   
stochastic gradient descent accuracy with deskewed + reduced noise :  0.904   
stochastic gradient descent accuracy with deskewed + reduced noise +standard:  0.9081

##  linear-svm 




## cos_knn



-->

<!--
one epoch = one forward pass and one backward pass of all the training examples

batch size = the number of training examples in one forward/backward pass. The higher the batch size, the more memory space you'll need.

number of iterations = number of passes, each pass using [batch size] 

number of examples. To be clear, one pass = one forward pass + one backward pass (we do not count the forward pass and backward pass as two different passes).


Example: if you have 1000 training examples, and your batch size is 500, then it will take 2 iterations to complete 1 epoch.-->
