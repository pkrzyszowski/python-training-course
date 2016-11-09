#a[start:stop:step]
In[2]: a = [1, 2, 3, 4]
In[3]: id(a)
Out[3]: 139854860398216
In[4]: b = a[:]
In[5]: b
Out[5]: [1, 2, 3, 4]
In[6]: id(b)
Out[6]: 139854860381448
In[7]: a == b
Out[7]: True
In[8]: a = [[0], [2], 3, 4]
In[9]: b = [:]
  File "<ipython-input-9-4875c4e3fdf9>", line 1
    b = [:]
         ^
SyntaxError: invalid syntax

In[10]: b = a[:]
In[11]: b
Out[11]: [[0], [2], 3, 4]
In[12]: b[0].append.('kuku')
  File "<ipython-input-12-332f70df3151>", line 1
    b[0].append.('kuku')
                ^
SyntaxError: invalid syntax

In[13]: b[0].append('kuku')
In[14]: a
Out[14]: [[0, 'kuku'], [2], 3, 4]
In[15]: b
Out[15]: [[0, 'kuku'], [2], 3, 4]
In[16]: a = [1, 2, 3, 4, 5, 6]
In[17]: len(a)
Out[17]: 6
In[18]: a[4]
Out[18]: 5
In[19]: b = a[0:4]
In[20]: b
Out[20]: [1, 2, 3, 4]
In[21]: b = a[0:4:1]
In[22]: b
Out[22]: [1, 2, 3, 4]
In[23]: c = a[0:4:2]
In[24]: c
Out[24]: [1, 3]
In[25]: a[:3]
Out[25]: [1, 2, 3]
In[26]: a[::3]
Out[26]: [1, 4]
In[27]: a[:]
Out[27]: [1, 2, 3, 4, 5, 6]
In[28]: a[:-1]
Out[28]: [1, 2, 3, 4, 5]
In[29]: a[:None]
Out[29]: [1, 2, 3, 4, 5, 6]
In[30]: list(reversed(a))
Out[30]: [6, 5, 4, 3, 2, 1]