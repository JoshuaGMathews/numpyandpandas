import numpy as np 
array = np.random.randn(5, 3) 
print(array) 
array*100 

import numpy as np

array1 = np.arange(10, 21, 2)
array2 = np.reshape(array1, (2, 3))
print(array2)

import numpy as np 
array=np.arange(100).reshape(20, 5)
print("shape:", array.shape, "\narray:\n", array) 

import numpy as np
array6=np.random.normal(size=(20,5))# Creates a random normally distributed sample of size 20*5
array7=np.copy(array6)
array7=array7*100
print('array6:\n', array6)
print('array7:\n', array7)

import pandas as pd
data = ['Column 0','Column 1','Column 2','Column 3','Column 4','Column 5']
obj7 = pd.Series([0,100,200,300,400,500])
obj7.index = data
print(obj7)

import pandas as pd
data10 = {"state":["ohio","ohio","Arizona","Arizona"],"population":[1.5,1.7,3.6,4.1],"year":[2000,2001,2000,2002]}
frame10 = pd.DataFrame(data10); ##converting dictionary to pandas data frame
print(frame10)