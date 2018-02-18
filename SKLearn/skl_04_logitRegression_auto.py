# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 2018

@author: Francesco

"""

import numpy as np
import pandas as pd
import matplotlib, matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

pd.options.mode.chained_assignment = None 

## Dati grezzi da csv (automobili data)
print("## Get the data")
DF_DATASET = pd.read_csv("dataset/automobile/imports-85.csv")
DF_DATASET.columns = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']

print("## index dei data: ")
DF_DATASET.set_index("engine-size", inplace=True)
print(DF_DATASET.index)
print(DF_DATASET.head())

## pulizia dataset:
print("\r\n## pulizia dataset")
#print(len(DF_DATASET.iloc[:,-1]))
prezzo_col = DF_DATASET.iloc[:,-1]
DF_DATASET.iloc[:,-1] = prezzo_col.map(lambda prezzo_i : np.nan if prezzo_i[:1]=='?' else prezzo_i[:])
DF_DATASET.dropna(inplace=True)
#print(len(DF_DATASET.iloc[:,-1]))
DF_DATASET.iloc[:,-1] = DF_DATASET.iloc[:,-1].map(lambda prezzo_i : int(prezzo_i))

y = DF_DATASET.iloc[:,-1]
#print(y.shape)

## Splitting di training e test set
print("## Splitting TRAINING and TEST set")
DF_train, DF_test = train_test_split(DF_DATASET, test_size=0.2)

DF_train.sort_index(inplace=True)
DF_test.sort_index(inplace=True)

## Preparo il modello ed eseguo il fit sui dati di test
print("## TRAIN: Prepare the model and fit it ")
regr = lm.LogisticRegression(C=10.0)
X_train = np.array(DF_train.index)[:, np.newaxis]
print("#### shape X (dominio): ")
#print(X_train.shape)
y_train = DF_train.iloc[:,-1] # 'price'
#print(y_train.shape)
regr.fit(X_train, y_train)
      
print("## PREDIZIONE su dati di test ")
X_test = np.array(DF_test.index)[:, np.newaxis]
#print("#### shape X (dominio di TEST): ")
#print(X_test.shape)
y_test = DF_test['price']
#print("#### shape Y (variabile dipendente di TEST): ")
#print(y_test.shape)

yp_on_test = [regr.predict(x) for x in DF_test.index]
#### Valutazione del modello (con lo stesso train set)
regr_score = regr.score(X_test, y_test) 
print("## SCORE del modello usato (TEST): "+str(regr_score))

#### confusion matrix
print("#### confusion matrix ")
cm = confusion_matrix(regr.predict(X_test), y_test)

print(cm) 
     
## Plot:
matplotlib.style.use("ggplot")
#### Plot di entrambi i set di valori (verifico y_test rispetto ai y predetti su X_test)
plt.plot(DF_test.index, y_test)
plt.plot(DF_test.index, yp_on_test)
plt.title("Logit Regression")
plt.xlabel("Engine-size")
plt.ylabel("Prezzo")
plt.legend(["Reale", "Predetto"], loc="lower right")

#### export plot
plt.savefig("my_plot_img/automobiliPrice-ridgeRegression.pdf")
