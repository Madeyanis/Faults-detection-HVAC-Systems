import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import confusion_matrix
from seaborn import heatmap
import seaborn as sns
from sklearn import tree
from sklearn.neural_network import MLPClassifier

print("success: Libraries loaded")


# data 1°C
data_f_1C = pd.read_csv("/home/masdoua1/projetIA3_9/data/Faults/Fault 1C/faulted_1C.csv", index_col=[0])

# data 2°C
data_f_2C = pd.read_csv('/home/masdoua1/projetIA3_9/data/Faults/Fault 2C/faulted_2C.csv', index_col=[0])
data_f_2C['Fault'] = 2

# data 4°C
data_f_4C = pd.read_csv('/home/masdoua1/projetIA3_9/data/Faults/Fault 4C/faulted_4C.csv', index_col=[0])
data_f_4C['Fault'] = 4

# data -1°C 
data_f_moins1C = pd.read_csv('/home/masdoua1/projetIA3_9/data/Faults/Fault -1C/faulted_moins1C.csv', index_col=[0])
data_f_moins1C['Fault'] = -1

# data -2°C 
data_f_moins2C = pd.read_csv('/home/masdoua1/projetIA3_9/data/Faults/Fault -2C/faulted_moins2C.csv', index_col=[0])
data_f_moins2C['Fault'] = -2

# data -4°C 
data_f_moins4C = pd.read_csv('/home/masdoua1/projetIA3_9/data/Faults/Fault -4C/faulted_moins4C.csv', index_col=[0])
data_f_moins4C['Fault'] = -4

# unfaulted data
data_uf_summer = pd.read_csv('/home/masdoua1/projetIA3_9/data/Unfaulted data/unfaulted_summer.csv', index_col=[0])
data_uf_spring = pd.read_csv('/home/masdoua1/projetIA3_9/data/Unfaulted data/unfaulted_spring.csv', index_col=[0])
data_uf_winter = pd.read_csv('/home/masdoua1/projetIA3_9/data/Unfaulted data/unfaulted_winter.csv', index_col=[0])
data_uf_automn = pd.read_csv('/home/masdoua1/projetIA3_9/data/Unfaulted data/unfaulted_automn.csv', index_col=[0])

print("success: Data loaded")


# data faulted and unfaulted (1°C, 2°C, 4°C, -1°C, -2°C and -4°C)
data = pd.concat([data_f_1C, data_f_2C, data_f_4C, data_f_moins1C, data_f_moins2C, data_f_moins4C, data_uf_summer, data_uf_spring, data_uf_winter, data_uf_automn])
x = data.drop(columns=['Fault', 'Time'])
y = data['Fault']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

print("success: concatenation of data")


## Neural network

clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(7, 30), random_state=1, verbose=True, max_iter=3000)
cv = ShuffleSplit(n_splits=1, test_size=0.3, random_state=0)
scores = cross_val_score(clf, x, y, cv=cv)
print(scores)

print("success: test of classifier")