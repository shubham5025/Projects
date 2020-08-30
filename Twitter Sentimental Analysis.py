#Twitter Sentimental Analysis by NLP

#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import re
import nltk
nltk.download('stopwords')

#Importing the Dataset
dataset=pd.read_csv('Twitter Sentimental Analysis.csv')

#Cleaning the Text
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(len(dataset)):
    review=re.sub('[^a-zA-Z]',' ',dataset['tweet'][i])
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
    
#Creating the Bag of word model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=14000)
x=cv.fit_transform(corpus).toarray()
y=dataset.iloc[:,1]

#Applying Naive Bayes Classifier
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

#Fitting Classifier to the Training Set
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score 
cm=confusion_matrix(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)



#Fitting Decision Tree  Classifier
from sklearn.tree import DecisionTreeClassifier
classifier1=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier1.fit(x_train,y_train)

y_pred1=classifier1.predict(x_test)
cm1=confusion_matrix(y_test,y_pred1)
accuracy1=accuracy_score(y_test,y_pred1)

#Fitting Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
classifier2=RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=0)
classifier2.fit(x_train,y_train)

y_pred2=classifier2.predict(x_test)

cm2=confusion_matrix(y_test,y_pred1)
accuracy2=accuracy_score(y_test,y_pred1)
