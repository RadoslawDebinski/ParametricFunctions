import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from matplotlib.animation import FuncAnimation
import preFunc as pf


steps = 2000
stepsForFigures = 200
xaxis = np.linspace(0, 10, steps)
speed = 20
framesAmount = 4000

fig, ax = plt.subplots()
polygon, =ax.plot([],[], 'ko', ms = 1)
# Following inverse clock and start from right down
polygonPoints, =ax.plot([1, 1, 0, 0],[0, 1, 1, 0], 'ro', ms = 3)
cyclogonx, cyclogony = [[-0.5],[2]]
cyclogon, = ax.plot(cyclogonx,cyclogony, 'mo', ms = 1)
gRads, = ax.plot([],[], 'co', ms = 1)
ax.axis('equal')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 2)
    return polygon,

def update(frame):

    pointsx = polygonPoints.get_xdata()
    pointsy = polygonPoints.get_ydata()
    # Rotation Axis change
    if pointsy[1] <= (1/steps):
        pointsx = np.roll(pointsx, -1)
        pointsy = np.roll(pointsy, -1)
    # Set angle and update points
    rad = np.sqrt(np.square(pointsx-pointsx[0]) + np.square(pointsy-pointsy[0]))
    alpha1 = (np.arctan2(pointsy, pointsx - pointsx[0]) - (speed/steps))
    pointsx = rad * np.cos(alpha1) + pointsx[0]
    pointsy = rad * np.sin(alpha1)
    # Guiding radiuses
    radsCordsx = np.concatenate(np.linspace(np.full(np.shape(pointsx), pointsx[0]), pointsx, stepsForFigures), axis=None)
    radsCordsy = np.concatenate(np.linspace(np.full(np.shape(pointsy), pointsy[0]), pointsy, stepsForFigures), axis=None)
    # Sides of polygon
    sidesCordsx= np.concatenate(np.linspace(pointsx, np.roll(pointsx, -1), stepsForFigures), axis=None)
    sidesCordsy = np.concatenate(np.linspace(pointsy, np.roll(pointsy, -1), stepsForFigures), axis=None)
    # Cyclogon calculate and append
    cRad = np.sqrt(np.square(cyclogon.get_xdata()[-1]-pointsx[0]) + np.square(cyclogon.get_ydata()[-1]-pointsy[0]))
    beta1 = (np.arctan2(cyclogon.get_ydata()[-1], cyclogon.get_xdata()[-1] - pointsx[0]) - (speed/steps))
    cyclogonx.append(cRad * np.cos(beta1) + pointsx[0])
    cyclogony.append(cRad * np.sin(beta1))
    # Update poition
    polygon.set_xdata(sidesCordsx)
    polygon.set_ydata(sidesCordsy)
    gRads.set_xdata(radsCordsx)
    gRads.set_ydata(radsCordsy)
    polygonPoints.set_xdata(pointsx)
    polygonPoints.set_ydata(pointsy)
    cyclogon.set_data(cyclogonx, cyclogony)

    return polygon, cyclogon, gRads, polygonPoints

ani = FuncAnimation(fig, update, frames=framesAmount,
                    init_func=init, interval = 0.1, blit=True, repeat=False)

plt.plot(xaxis, np.zeros(np.shape(xaxis)),'b', label='background')
plt.title('Cyclogon')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.autoscale()
plt.legend()
plt.show()











