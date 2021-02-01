# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:38:59 2021

@author: Qi Jianxiang
"""

import numpy as np


studtype = np.dtype({'names':['姓名','语文','数学','英语'],\
                     'formats':['S32','f','f','f']})
students = np.array([("zhangfei", 68 , 65,30),("guanyu",95,76,98), \
                     ("liubei",98,86,88),("dianwei",90,88,77),("xuchu",80,90,90)], dtype=studtype)
print(students)
chinese = students['语文']
mathmatic = students['数学']
english = students['英语']
print('语文平均分:%f' %np.mean(chinese))
print('数学平均分:%f' %np.mean(mathmatic))
print('英语平均分:%f' %np.mean(english))
print('语文最低分:%d' %np.min(chinese))
print('数学最低分:%d' %np.min(mathmatic))
print('英语最低分:%d' %np.min(english))
print('语文成绩方差:%f'%np.var(chinese))
print('数学成绩方差:%f'%np.var(mathmatic))
print('英语成绩方差:%f'%np.var(english))
print('数学成绩标准差:%f'%np.std(mathmatic))
print('语文成绩标准差:%f'%np.std(chinese))
print('英语成绩标准差:%f'%np.std(english))

import pandas as pd
data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 77, 90]}
chengjibiao = pd.DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
chengjibiao['score_sum']=chengjibiao.sum(axis=1)
# print(chengjibiao)
chengjibiao2 = chengjibiao.sort_values('score_sum',ascending=0)
print('成绩由高到底排名：')
print(chengjibiao2)