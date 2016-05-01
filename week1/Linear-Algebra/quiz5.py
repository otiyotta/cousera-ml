# -*- coding:utf-8 -*-

import numpy as np
from sklearn import linear_model

#標準正規分布5*5の多次元配列
x=np.random.randn(3,3)
y=np.random.randn(3,3)
i=np.identity(3)

print "x=",x
print "y=",y
print "i=",i
print "x+y=",x+y
print "y+x=",y+x
print "x*i=",x.dot(i)
print "i*x=",i.dot(x)
print "x*y=",x.dot(y)
print "y*x=",y.dot(x)
print "x*y*x=",x.dot(y).dot(x)
print "y*x*y=",y.dot(x).dot(y)
