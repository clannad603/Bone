import numpy as np
n=int(input())
l=[]
ls=[]
for i in range(n):
    l.append(0.)
for i in range(n):
    ls.append(l[:])
for i in range(n):
    ls[i][i]=i+1
ls=np.array(ls)
print(ls)

