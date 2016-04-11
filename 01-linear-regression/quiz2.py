# -*- coding:utf-8 -*-

import numpy as np
from sklearn import linear_model

#train data
#縦に並べないと、scikit-learnの入力で受け付けてくれない
x=np.array([[1,2,4,0]]).reshape(4,1)
y=np.array([[0.5,1,2,0]]).reshape(4,1)

#train model
regr = linear_model.LinearRegression()
regr.fit(x,y)

print '%s+%0.1f' %('intercept=',regr.intercept_[0])
print '%s+%0.1f' %('coef=',regr.coef_[0][0])
