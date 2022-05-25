from functions import *
import pandas as pd

path='/home/masdoua1/projetIA3_9/data/AHU/mzvav1/MZVAV-2-2.csv'

mz21 = pd.read_csv(path)

uf_days = ['8/27/2008', '8/28/2008', '8/29/2008', '8/30/2008', '8/31/2008', '9/1/2008',
           '9/4/2008', '9/5/2008', '2/11/2009', '5/6/2009', '5/7/2009', '5/8/2009', '5/15/2009']

valve_stuck_days = ['5/6/2008', '8/31/2007', '5/15/2008', '9/1/2007', '9/2/2007']

valve_leak_days = ['8/28/2007', '8/29/2007', '8/30/2007']

OA_damp_days = ['2/12/2008', '5/7/2008', '5/8/2008', '9/5/2007', '9/6/2007']


uf_index = index_data(mz21, uf_days)
valve_stuck_index = index_data(mz21, valve_stuck_days)
valve_leak_index = index_data(mz21, valve_leak_days)
oa_damp_index = index_data(mz21, OA_damp_days)

uf = dataLema(mz21, uf_index)
vs = dataLema(mz21, valve_stuck_index)
vl = dataLema(mz21, valve_leak_index)
oad = dataLema(mz21, oa_damp_index)

mz21 = pd.concat([uf, vs, vl, oad])

uf = changeColumnsName(uf)
vs = changeColumnsName(vs)
vl = changeColumnsName(vl)
oad = changeColumnsName(oad)

vs['Fault'] = 1
vl['Fault'] = 2
oad['Fault'] = 3

uf.to_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/uf_data.csv', index=False)  
vs.to_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/vs_data.csv', index=False) 
vl.to_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/vl_data.csv', index=False) 
oad.to_csv('/home/masdoua1/projetIA3_9/data/Data_arranged/oad_data.csv', index=False) 



print("successfully saved !")

