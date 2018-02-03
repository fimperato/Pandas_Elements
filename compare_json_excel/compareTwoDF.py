# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 

@author: Francesco
"""

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A1': [1, 2, 3, 4], 'B1': ['a', 'b', 'c', 'd']})
df2 = pd.DataFrame({'A1': [1, 2, 3, 5], 'B1': ['a', 'd', 'c', 'e']})

print("\r\nComparazione dei due ")
df3 = df1.merge(df2, how='outer', on='A1', suffixes=['_1', '_2'])
df3['check'] = df3.B1_1 == df3.B1_2

print(df3)

## valori diversi per caso non trovato su B1 (in più su B2)
print("\r\nValori diversi per caso non trovato su B1 (in più su B2)")
VAL_IN_PIU_SU_B2 = df3[df3.B1_1.isnull()]
print(VAL_IN_PIU_SU_B2)

print("\r\nValori diversi per caso non trovato su B2 (in più su B1)")
VAL_IN_PIU_SU_B1 = df3[df3.B1_2.isnull()]
print(VAL_IN_PIU_SU_B1)

## JSON Import

## Case 1.
print("\r\nJSON Import [1]")
data = [{'name': 'vikash', 'age': 27}, {'name': 'Satyam', 'age': 14}]
df_by_json1 = pd.DataFrame.from_dict(data, orient='columns')
print(df_by_json1)

## Case 2. with nested column we can normalize:
print("\r\nJSON Import [2]")
from pandas.io.json import json_normalize
data = [ {
    'name': {
      'first': 'vikash',
      'last': 'singh'
    },
    'age': 27
  }, {
    'name': {
      'first': 'satyam',
      'last': 'singh'
    },
    'age': 14
  }
]
df_by_json2 = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
print(df_by_json2)

## Case 3.
print("\r\nJSON Import [3]")
import urllib.request
import json
from pprint import pprint

#path1 = '42.974049,-81.205203|42.974298,-81.195755'
#request1=urllib.request('http://maps.googleapis.com/maps/api/elevation/json?locations='+path1+'&sensor=false')

#with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
#    data = json.loads(url.read().decode())
#    print(data)
    
data = json.load(open('json\jsonmaps_geocoded.json'))
pprint(data)
NORMALIZED_DATA3 = json_normalize(data['results'])

## Case 3.1
print("\r\nJSON Import -> to DF [3.1]")
df_by_json3 = pd.DataFrame.from_dict(NORMALIZED_DATA3, orient='columns')
print(df_by_json3)
