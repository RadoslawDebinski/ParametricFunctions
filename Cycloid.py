import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from matplotlib.animation import FuncAnimation
import preFunc as pf

fig, ax = plt.subplots()
xdata, ydata = [], []
der, = ax.plot([], [], 'ro', ms = 1)
shift, =ax.plot([], [], 'go', ms = 1)
circle, =ax.plot(0,0)
gRad, =ax.plot([],[],'ok', ms = 1)
cycloid, = ax.plot([],[], 'mo', ms = 1)
ax.axis('equal')

steps = 1000
stepsForFigures = 50
rad = 2
derLeng = 1
speed = 1
cycloidx, cycloidy = [[],[]]

xaxis = np.linspace(0, 10, steps)
func = pf.PreFunc(np.sin)
backGroud = func.calc(xaxis)

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 2)
    return der,

def update(frame):
    #derivative as line
    a = (func.calc(frame + (1 / steps)) - func.calc(frame))/(1/steps)
    b = func.calc(frame) - a*frame
    x0 = frame - derLeng/2
    x1 = frame + derLeng/2
    der.set_xdata(np.linspace(x0, x1, stepsForFigures))
    der.set_ydata(np.linspace((a*x0+b), (a*x1+b), stepsForFigures))
    #Circle shift
    alpha = np.arctan2(func.calc(frame + (1 / steps)) - func.calc(frame),1/steps)
    alpha1 = np.pi/2 - alpha
    rx= -rad * np.cos(alpha1)
    ry= rad * np.sin(alpha1)
    shift.set_xdata(np.linspace(frame, (frame+rx), stepsForFigures))
    shift.set_ydata(np.linspace(func.calc(frame), (func.calc(frame)+ry), stepsForFigures))
    #Circle
    time = np.arange(0, 2 * np.pi, 0.05)
    circle.set_xdata(rad * np.cos(time) + frame + rx)
    circle.set_ydata(rad * np.sin(time) + func.calc(frame) + ry)
    #Guiding radius
    dx = frame + 10/steps
    dy = func.calc(dx) - func.calc(frame)
    derl = np.sqrt(np.square(dx)+np.square(dy))
    beta = derl / rad

    gRad.set_xdata(np.linspace((frame + rx), (frame + rx + rad*np.cos(beta)),stepsForFigures))
    gRad.set_ydata(np.linspace((func.calc(frame) + ry), (func.calc(frame) + ry + rad*np.sin(-beta)),stepsForFigures))
    #Cycloid
    cycloidx.append(frame + rx + rad*np.cos(beta))
    cycloidy.append(func.calc(frame) + ry + rad*np.sin(-beta))
    cycloid.set_xdata(cycloidx)
    cycloid.set_ydata(cycloidy)

    return der, shift, circle, gRad, cycloid

ani = FuncAnimation(fig, update, frames=xaxis,
                    init_func=init, interval = 0.1, blit=True, repeat=False)

plt.plot(xaxis, backGroud,'b', label='sin')
plt.title('Cycloid')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.autoscale()
plt.legend()
plt.show()











