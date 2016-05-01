# -*- coding:utf-8 -*-

import numpy as np
from sklearn import linear_model

u=np.array([[-3,4,3]]).reshape(3,1)
v=np.array([3,1,5]).reshape(3,1)
print u.transpose().dot(v)

#arrayだと、*は要素ごとの掛け算注意
#print u.transpose() * v
