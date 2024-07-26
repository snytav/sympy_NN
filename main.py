
from sympy import *
import numpy as np

Nx=3
Ny = 1
ww = symbols('w0:%d:%d'%(Ny,Nx))
ww = np.array(list(ww))
ww = ww.reshape(Ny,Nx)
print('ww ',ww)
Nx = 1
xx = symbols('x0:%d:%d'%(Ny,Nx))
print('xx ',xx)


def Linear(ww,x):
  ff = []
  print('',x)
  for i in range(ww.shape[0]):
      f = 0
      for j in range(ww.shape[1]):
          f[i] = f[i] + ww[i][j]*x[j]
          print(j,ww[i][j],x[j],f)
      ff.append(f)
  ff = np.array(ff)
  return ff

f = Linear(ww.T,xx)