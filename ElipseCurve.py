import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from matplotlib.animation import FuncAnimation
import preFunc as pf
from sys import argv

steps = 4000
stepsForFigures = 20
framesAmount = 4000
xaxis = np.linspace(0, 20, steps)
speed = 200

fig, ax = plt.subplots()
polygon, =ax.plot([],[], 'ko', ms = 1)
# Generate elipse
time = np.arange(0, 2 * np.pi, 0.1)
elipsex, elipsey = np.array([[],[]])
a, b = 1, 1
elipsex = a * np.cos(time)
elipsey = b * np.sin(time) + 2
# Following inverse clock
polygonPoints, =ax.plot(elipsex,elipsey, 'ro', ms = 1)
cyclogonx, cyclogony = [[0.5],[5]]
cyclogon, = ax.plot(cyclogonx,cyclogony, 'mo', ms = 1)
gRads, = ax.plot([],[], 'go', ms = 1)
ax.axis('equal')

func = pf.PreFunc(np.sin ,0, 0, 1)
backGroud = func.calc(xaxis)

def init():
    ax.set_xlim(0, 20)
    ax.set_ylim(-4, 4)
    return polygon,

def update(frame):

    pointsx = polygonPoints.get_xdata()
    pointsy = polygonPoints.get_ydata()
    # Rotation Axis change
    i = np.where(pointsy <= (func.calc(pointsx) + (1/steps)))
    if np.size(i[0]) > 1:
        pointsx = np.roll(pointsx, -i[0][-1])
        pointsy = np.roll(pointsy, -i[0][-1])
    else:
        pointsx = np.roll(pointsx, -i[0])
        pointsy = np.roll(pointsy, -i[0])
    # Set angle and update points
    rad = np.sqrt(np.square(pointsx-pointsx[0]) + np.square(pointsy-pointsy[0]))
    alpha1 = (np.arctan2(pointsy - pointsy[0], pointsx - pointsx[0]) - (speed/steps))
    pointsx = rad * np.cos(alpha1) + pointsx[0]
    pointsy = rad * np.sin(alpha1) + pointsy[0]
    # Guiding radiuses
    radsCordsx = np.concatenate(np.linspace(np.full(np.shape(pointsx), pointsx[0]), pointsx, stepsForFigures), axis=None)
    radsCordsy = np.concatenate(np.linspace(np.full(np.shape(pointsy), pointsy[0]), pointsy, stepsForFigures), axis=None)
    # Sides of polygon
    sidesCordsx= np.concatenate(np.linspace(pointsx, np.roll(pointsx, -1), stepsForFigures), axis=None)
    sidesCordsy = np.concatenate(np.linspace(pointsy, np.roll(pointsy, -1), stepsForFigures), axis=None)
    # Cyclogon calculate and append
    cRad = np.sqrt(np.square(cyclogon.get_xdata()[-1]-pointsx[0]) + np.square(cyclogon.get_ydata()[-1]-pointsy[0]))
    beta1 = (np.arctan2(cyclogon.get_ydata()[-1] - pointsy[0], cyclogon.get_xdata()[-1] - pointsx[0]) - (speed/steps))
    cyclogonx.append(cRad * np.cos(beta1) + pointsx[0])
    cyclogony.append(cRad * np.sin(beta1) + pointsy[0])
    # Update poition
    polygon.set_xdata(sidesCordsx)
    polygon.set_ydata(sidesCordsy)
    gRads.set_xdata(radsCordsx)
    gRads.set_ydata(radsCordsy)
    polygonPoints.set_xdata(pointsx)
    polygonPoints.set_ydata(pointsy)
    cyclogon.set_data(cyclogonx, cyclogony)

    return polygon, cyclogon, polygonPoints, gRads

ani = FuncAnimation(fig, update, frames=framesAmount,
                    init_func=init, interval = 0.1, blit=True, repeat=False)

plt.plot(xaxis, backGroud,'b', label='background')
plt.title('Preparation for first laboratory WNO: Cyclogon')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.autoscale()
plt.legend()
plt.show()











