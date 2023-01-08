# ParametricFunctions

The project involves dynamically changing the axis of rotation to simulate the movement of a cyclogon, such as a traingle on a curve. Another goal of the project was to avoid using "for" statements and learn how to write without loops. This requirement was imposed as a result of optimization and practice.

File CyclogonCurve.py:
- This program collaborates with preFunc.py (like others in this project) to create curve. Next, it will calculate frames of movement for object given by the operator. -- Input parameters: 
  - Triangle points:
    - point1 = input() 
    - point2 = input()
    - point3 = input()
- Given a Numpy library function with the np prefix:
    - function = input()
- Function shifts in the X and Y axes:
    - shiftx = input()
    - shifty = input()
    
File ElipseCurve.py:
- In this project, we jump over data input. It can be considered as a demo to show the possibilities of a changeable axis algorithm. By changing line's
time = np.arange(0, 2 * np.pi, 1) last parameter we can manage step of points created on a circular plan. The curve is predifined as a simple sinus. We can convert a circle into an ellipse by changing the a and b parameters. Sample graphics:
![image](https://user-images.githubusercontent.com/83645103/211212284-a78e6caf-e432-4c03-a8f6-2757201f7f04.png)
![image](https://user-images.githubusercontent.com/83645103/211212312-15124f62-97a1-48a0-854e-aa82bb463696.png)
![image](https://user-images.githubusercontent.com/83645103/211212358-b83d2d8a-ed77-4ee0-a19b-ac6c47254388.png)
