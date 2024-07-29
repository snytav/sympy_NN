
from sympy import *
import numpy as np

Nx=3
Ny = 1

def array_of_vars(Ny,Nx):
    xx = []
    for i in range(Ny):
        xline = []
        for j in range(Nx):
            xl = var('x_%d%d' % (i,j))
            xline.append(xl)
        xx.append(xline)
    return xx
xx = array_of_vars(Nx,Ny)
print('xx ',xx)

ww = symbols('w0:%d:%d'%(Ny,Nx))
ww = np.array(list(ww))
ww = ww.reshape(Ny,Nx)
print('ww ',ww)
Nx = 1
xx = symbols('x0:%d:%d'%(Ny,Nx))
print('xx ',xx)

A = Matrix(3, 3, lambda i,j: Symbol('a_%d%d' % (i,j)))
print(A)

aa = symarray('a', 3)
print(aa)






def Linear(ww,x):
  ff = []
  print('',x)
  for i in range(ww.shape[0]):
      f = 0
      for j in range(ww.shape[1]):
          f = f + ww[i][j]*x[j]
          print(j,ww[i][j],x[j],f)
      ff.append(f)
  ff = np.array(ff)
  return ff

f = Linear(ww.T,xx)