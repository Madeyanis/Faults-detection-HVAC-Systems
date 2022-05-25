import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import confusion_matrix
from seaborn import heatmap
import seaborn as sns
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from functions import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


uf = pd.read_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/uf_data.csv')
vs = pd.read_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/vs_data.csv')
vl = pd.read_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/vl_data.csv')
oad = pd.read_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/oad_data.csv')

print("Successfully loaded")

# data faulted and unfaulted (1°C, 2°C, 4°C, -1°C, -2°C and -4°C)
data = pd.concat([uf, vs, vl, oad])
x = data.drop(columns=['Fault', 'Time'])
y = data['Fault']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)



clf = RandomForestClassifier(n_estimators=150, verbose=1)
scores = cross_val_score(clf, x, y, cv=4)
print(scores)