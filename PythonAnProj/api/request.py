# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:16:43 2021

@author: Sarah
"""


import requests
import json
import pandas as pd

url = 'http://0.0.0.0:5000/apiThéoSarah/'


data=pd.read_fwf('C:\\Users\\salom\\Documents\\Python\\data.arff',sep=",",header=11,names=['Attr1','Attr2','Attr3','Attr4','Attr5','Attr6','Attr7','Attr8','Attr9','Attr10','result'])
import numpy as np
data[:].replace('?',np.nan,inplace=True)
data=data.dropna()

newFeatures=['Attr1','Attr2','Attr3']
X2= data.loc[:, newFeatures].values
X2=pd.DataFrame(X2)


j_data = X2.to_json()
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

r = requests.post(url, data=j_data, headers=headers)

print(r,r.text)
 
#try:
    #print(r,r.text)
#except requests.exceptions.ConnectionError:
    #r.status_code = "Connection refused"


