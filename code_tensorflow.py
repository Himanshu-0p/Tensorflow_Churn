# -*- coding: utf-8 -*-
"""Code_Tensorflow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DzaCRNEQF24q5jP3HAonjQ-5y4YIrFvu
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('/content/Churn.csv')

X = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

y_train.head()

from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

from keras.models import Sequential
from keras.layers import Dense, Input

model = Sequential()
model.add(Input(shape=(X_train.shape[1],)))  # shape = (number of features,)
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))  # For binary classification

model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])

model.fit(X_train,y_train,epochs=200,batch_size=32)

y_hat = model.predict(X_test)
y_hat = [0 if val < 0.5 else 1 for val in y_hat]

y_hat

accuracy_score(y_test,y_hat)

model.save('tfmodel')

model.save('tfmodel.keras') # Add the .keras extension to the filename