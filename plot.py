from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def getAll(fstr, ncol):
  return [ [ float(val.split()[ncol]) for val in d.strip().split('\n') ] for d in fstr.strip().split('\n\n') ]

def getFirstRows(fstr, ncol):
  return [ float(d.strip().split('\n')[0].strip().split()[ncol]) for d in fstr.strip().split('\n\n') ]

def contourPlot(X, Y, Z):
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
  plt.show()

def linePlot(X):
  plt.plot(X)
  plt.show()

def main():
  fstr = open('data/field_23000', 'r').read()
  Z = np.array(getAll(fstr, 2))
  #linePlot(Z[0])
  X = np.arange(Z.shape[1])
  Y = np.array(getFirstRows(fstr, 0))
  X, Y = np.meshgrid(X, Y)
  contourPlot(X, Y, Z)

if __name__ == '__main__':
  main()
