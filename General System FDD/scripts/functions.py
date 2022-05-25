import pandas as pd

def index_data(mz21, uf_days):
    uf_index = list()
    for i in range(0, 26):
        t = mz21['Datetime'].iloc[i*1440]
        t = t.split()[0]

        for j1 in uf_days:
            if t == j1:
                uf_index.append(i)


    return uf_index



def dataLema(mz21, index):

    uf = list()
    for i in index:
        uf.append(mz21.iloc[i*1440:(i+1)*1440])
    uf = pd.concat(uf)

    return uf
    

def changeColumnsName(data):

    cols = data.columns.tolist()
    cols_new = ['Time', 'SA T', 'SA T Set', 'OA T', 'MA T', 'RA T',
                'SA Fan Stat', 'RA Fan Stat', 'SA Speed', 'RA Speed', 'EA Damper',
                'OA Damper', 'RA Damper', 'Cooling valve', 'Heating valve',
                'SA Pressure Set', 'SA Pressure', 'Occupancy', 'Fault']
    dii = dict(zip(cols, cols_new))
    data = data.rename(columns=dii)

    return data


def faultImposition(db):

    if str(db) == 'uf':
        db['Fault'] = 0
    elif str(db) == 'vs':
        db['Fault'] = 1
    elif str(db) == 'vl':
        db['Fault'] = 2
    elif str(db) == 'oad':
        db['Fault'] = 3 
    
    return db

def my_normalization_3d_columns(x):

    for i in range(x.shape[2]):
        x[:, :, i] = (x[:, :, i] - x[:, :, i].min())/ (x[:, :, i].max() - x[:, :, i].min())


    return x