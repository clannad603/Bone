import numpy as np
n,m=map(int,input().split(" "))
ls=np.zeros((1, n))
ls[0][m-1]=1
print(ls)
