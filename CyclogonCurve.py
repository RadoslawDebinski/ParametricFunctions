import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import preFunc as pf


steps = 2000
stepsForFigures = 200
xaxis = np.linspace(0, 10, steps)
speed = 50
framesAmount = 4000

fig, ax = plt.subplots()
polygon, =ax.plot([],[], 'ko', ms = 1)
# Following inverse clock and start from right down
point1 = input()
point2 = input()
point3 = input()
function = input()
shiftx = input()
shifty = input()

gravCentx = [(float(point1[0]) + float(point2[0]) + float(point3[0]))/3]
gravCenty = [(float(point1[1]) + float(point2[1]) + float(point3[1]))/3]

polygonPoints, =ax.plot([float(point1[0]), float(point2[0]), float(point3[0])],[float(point1[1]), float(point2[1]), float(point3[1])], 'ro', ms = 1)
gravCent, = ax.plot(gravCentx, gravCenty, 'go', ms = 1)
cyclogonx, cyclogony = [[float(point2[0])],[float(point2[1])]]
cyclogon, = ax.plot(cyclogonx,cyclogony, 'mo', ms = 1)

#gRads, = ax.plot([],[], 'go', ms = 1)
ax.axis('equal')

func = pf.PreFunc(eval(function), float(shiftx), float(shifty))
backGroud = func.calc(xaxis)

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(-4, 4)
    return polygon,

def update(frame):

    pointsx = polygonPoints.get_xdata()
    pointsy = polygonPoints.get_ydata()

    gravCentx = [np.sum(pointsx)/3]
    gravCenty = [np.sum(pointsy)/3]
    # Sides of polygon
    sidesCordsx = np.concatenate(np.linspace(pointsx, np.roll(pointsx, -1), stepsForFigures), axis=None)
    sidesCordsy = np.concatenate(np.linspace(pointsy, np.roll(pointsy, -1), stepsForFigures), axis=None)
    #Rotation Axis change
    
    i = np.where(sidesCordsy <= (func.calc(sidesCordsx) + (1 / steps)))
    if np.size(i[0]) > 1:
        sidesCordsx = np.roll(sidesCordsx, -i[0][1])
        sidesCordsy = np.roll(sidesCordsy, -i[0][1])
    else:
        sidesCordsx = np.roll(sidesCordsx, -i[0])
        sidesCordsy = np.roll(sidesCordsy, -i[0])
    # Set angle and update points
    rad = np.sqrt(np.square(sidesCordsx-sidesCordsx[0]) + np.square(sidesCordsy-sidesCordsy[0]))
    alpha1 = (np.arctan2(sidesCordsy - sidesCordsy[0], sidesCordsx - sidesCordsx[0]) - (speed/steps))
    sidesCordsx = rad * np.cos(alpha1) + sidesCordsx[0]
    sidesCordsy = rad * np.sin(alpha1) + sidesCordsy[0]
    # Cyclogon calculate and append
    cRad = np.sqrt(np.square(cyclogon.get_xdata()[-1]-sidesCordsx[0]) + np.square(cyclogon.get_ydata()[-1]-sidesCordsy[0]))
    beta1 = (np.arctan2(cyclogon.get_ydata()[-1] - sidesCordsy[0], cyclogon.get_xdata()[-1] - sidesCordsx[0]) - (speed/steps))
    cyclogonx.append(cRad * np.cos(beta1) + sidesCordsx[0])
    cyclogony.append(cRad * np.sin(beta1) + sidesCordsy[0])
    # Gravity Center
    centerCordsx = np.concatenate(np.linspace(gravCentx, cRad * np.cos(beta1) + sidesCordsx[0], stepsForFigures), axis=None)
    centerCordsy = np.concatenate(np.linspace(gravCenty, cRad * np.sin(beta1) + sidesCordsy[0], stepsForFigures), axis=None)
    # Update poition
    polygon.set_xdata(sidesCordsx)
    polygon.set_ydata(sidesCordsy)
    polygonPoints.set_xdata(pointsx)
    polygonPoints.set_ydata(pointsy)
    cyclogon.set_data(cyclogonx, cyclogony)
    gravCent.set_data(centerCordsx, centerCordsy)

    return polygon, cyclogon, polygonPoints, gravCent

ani = FuncAnimation(fig, update, frames=framesAmount,
                    init_func=init, interval = 0.1, blit=True, repeat=False)

plt.plot(xaxis, backGroud,'b', label='background')
plt.title('Preparation for first laboratory WNO: Cyclogon')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.autoscale()
plt.legend()
plt.show()


# # Guiding radiuses
    # radsCordsx = np.concatenate(np.linspace(np.full(np.shape(sidesCordsx), sidesCordsx[0]), sidesCordsx, stepsForFigures), axis=None)
    # radsCordsy = np.concatenate(np.linspace(np.full(np.shape(sidesCordsy), sidesCordsy[0]), sidesCordsy, stepsForFigures), axis=None)








