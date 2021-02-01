# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 20:52:42 2021

@author: Qi Jianxiang
"""

import pandas as pd

data = pd.read_csv('car_complain.csv')
# print(data)
result1 = data.groupby(['brand','car_model']).agg('count')
result1.rename({'一汽-大众':'一汽大众'},inplace=True)
a=result1.reset_index()
car_model_sum = a.groupby('brand').agg('count')
df = car_model_sum.sort_values('car_model',ascending=False)
print(df)
for i in range(600):
    problems=data['problem'][i]
    num=problems.count(',')
    data['problme_sum'] = num
result2=data.groupby('brand').agg('sum')
result2.rename({'一汽-大众':'一汽大众'},inplace=True)
car_complain_sum=result2.groupby('brand').agg('sum')
print(car_complain_sum)
df3 = pd.merge(df, car_complain_sum, on='brand')
df3['average']=df3['problme_sum']/df3['car_model']
df4=df3.sort_values('average', ascending=False)
print(df4)
