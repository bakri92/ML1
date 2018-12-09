import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,np.pi*2,100)
y = np.linspace(0,np.pi*2,100)

def phi(X):
    return np.cos(X)**2,np.sqrt(2)*np.cos(X)*np.sin(X),np.sin(X)**2

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(*phi(x))
fig.savefig("2biunitcircle.pdf",format="pdf")

xp = np.linspace(-10,10,100)
yp = np.linspace(-10,10,100)

XP,YP = np.meshgrid(xp,yp)

def phiplane(X,Y):
    return X**2,np.sqrt(2)*X*Y,Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(*phiplane(XP.flatten(),YP.flatten()))
fig.savefig("2biiplane.pdf",format="pdf")
