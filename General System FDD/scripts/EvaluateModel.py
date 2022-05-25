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
from keras.callbacks import EarlyStopping, ModelCheckpoint
from functions import *
from keras.models import Sequential, load_model
from tensorflow.keras.optimizers import Adam
from keras.layers import Dense, Conv1D, Dropout, MaxPooling1D, LSTM, Flatten, Conv2D, MaxPooling2D
import os
from seaborn import heatmap
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import MinMaxScaler
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

uf = pd.read_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/uf_data.csv')
vs = pd.read_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/vs_data.csv')
vl = pd.read_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/vl_data.csv')
oad = pd.read_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/oad_data.csv')

print("Successfully loaded")

# data faulted and unfaulted (1°C, 2°C, 4°C, -1°C, -2°C and -4°C)
data = pd.concat([uf, vs, vl, oad])
x = data.drop(columns=['Fault', 'Time'])
y = data['Fault']
x = np.array(x)
x2 = np.zeros([x.shape[0], 17, x.shape[1]])


for i in range(x.shape[0]- x2.shape[1]):
    x2[i, :, :] = x[i : i + x2.shape[1], :]
    
x = x2

del x2, data   

# normalization for differents columns and split
x = my_normalization_3d_columns(x)
# one-hot
y_hot = to_categorical(y)

# load model
# load the model
new_model = load_model('/home/masdoua1/projetIA3_9/Scripts/model.h5')

print(x.shape, y_hot.shape)

# evaluate the keras model
_, accuracy = new_model.evaluate(x, y_hot)
print('Accuracy: %.2f' % (accuracy*100))

y_pred = new_model.predict(x)
print("y_pred = ", y_pred.shape)
print("y_hot = ", y_hot.shape)
con_mat = confusion_matrix(y_hot.argmax(axis=1), y_pred.argmax(axis=1))

print(con_mat)
print(con_mat.sum(axis=0)[3])
print(con_mat[0, 0])

c = np.zeros([4, 4])

for i in range(con_mat.shape[0]):
    for j in range(con_mat.shape[1]):
        c[i, j] = con_mat[i, j] / con_mat.sum(axis=0)[j]
    
c = c * 100
    
np.set_printoptions(precision=2, suppress=True)
print(c)


