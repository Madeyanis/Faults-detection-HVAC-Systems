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
from keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from keras.layers import Dense, Conv1D, Dropout, MaxPooling1D, LSTM, Flatten, Conv2D, MaxPooling2D, Reshape
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
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# one-hot
y_hot_train = to_categorical(y_train)
y_hot_test = to_categorical(y_test)

# dimension
X_train = np.expand_dims(X_train, axis=3)
X_test = np.expand_dims(X_test, axis=3)

# define the keras model
model = Sequential()
#model.add(Flatten(input_shape=(x.shape[1], x.shape[2])))
model.add(Conv1D(64, 1, activation='relu', padding='valid'))
model.add(Conv1D(64, 1, activation='relu', padding='valid'))
model.add(Conv1D(64, 1, activation='relu', padding='valid'))
model.add(Conv1D(64, 1, activation='relu', padding='valid'))
model.add(MaxPooling2D((2, 2)))
model.add(Dense(80, activation='relu'))
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))

# compile the keras model
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0005), metrics=['accuracy'] )

checkpoint_filepath = '/home/masdoua1/projetIA3_9/Scripts/model.h5'

# saving model
earlyStop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=150)
modelCheckPt = ModelCheckpoint('/home/masdoua1/projetIA3_9/Scripts/model.h5', save_weights_only=False, monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)

# fit the keras model on the dataset
history = model.fit(X_train, y_hot_train, epochs=1500, batch_size=500, shuffle=True, validation_split=0.1, callbacks=[earlyStop, modelCheckPt])

# evaluate the keras model
_, accuracy = model.evaluate(X_test, y_hot_test)
print('Accuracy of test database: %.2f' % (accuracy*100))

# convert the history.history dict to a pandas DataFrame:     
hist_df = pd.DataFrame(history.history) 

# save to csv: 
hist_csv_file = '/home/masdoua1/projetIA3_9/Scripts/history.csv'
with open(hist_csv_file, mode='w') as f:
    hist_df.to_csv(f)