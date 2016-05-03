# -*- coding:utf-8 -*-

import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

# create samples
x=np.array([89,72,94,69]).reshape(4,1)
poly=PolynomialFeatures(degree=2)
xp=poly.fit_transform(x)
y=np.array([96,74,87,78]).reshape(4.1)

#train model
regr = linear_model.LinearRegression()
regr.fit(xp,y)

print "intercept=", regr.intercept_
print "coef=", regr.coef_
