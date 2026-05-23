import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
from matplotlib.colors import Normalize 
import time 
import sympy as sy
import keyboard

# Graphing Function 
def descent_run(learning_rate, starting_point, func_string):
    MAX_NUMBER_OF_STEPS  = 300
    PRECISION = 0.025
    global eq,dr
    steps = 0 
    def f(x):
        return eval(eq, {"x": x})

    #Derivative Equation
    def df(x):
        return eval(dr,{"x":x} )

    # Tangent line generator
    def tangent_line(x0, length=2):
        slope = df(x0)
        xs = np.array([x0 - length/2, x0 + length/2])
        ys = f(x0) + slope * (xs - x0)
        return slope
    #Operate from the app


    # Initial point
    
    eq = func_string
    #Write the stringed equation out that is passable to the sy.diff() function
    norm = Normalize(vmin = 0 , vmax = 1)

    expression = sy.sympify(eq) 
    nx = sy.Symbol('x')
    dr = str(sy.diff(expression, nx))

    x = starting_point
    lr = learning_rate

    # Set up plot
    xs = np.linspace(-50, 50, 400)
    plt.ion()
    fig, ax = plt.subplots()
    ax.plot(xs, f(xs), label="f(x)")

    # Create point and tangent line ONCE
    point = ax.scatter([x], [f(x)], color='red', s=60)

    m = tangent_line(x)
    cmap = cm.autumn
    color = cmap(norm(abs(m)))
    tangent = ax.axline(xy1= (x, f(x)), slope = m, color = color,label = "Tangent Line")

    sm = cm.ScalarMappable(norm = norm, cmap =cmap)
    cbar = plt.colorbar(sm, ax = ax)
    cbar.set_label("Slope: (Distance from Goal) ")

    ax.grid()


    ax.set_ylim(-50, 50)
    

    
    # Gradient descent loop
    for step in range(MAX_NUMBER_OF_STEPS):
        if keyboard.is_pressed("x"): exit()
        steps += 1 
        time.sleep(0.15)
        # Update x
        x = x - lr * df(x)
        # Update point
        point.set_offsets([x, f(x)])

        # Update tangent line
        m = tangent_line(x)
        color = cm.autumn(norm(abs(m)))
        tangent.set(xy1 = (x,f(x)), slope = m, color = color)

        if abs(m) <=PRECISION: break # close enough, and I don't want the program to run all day just cause it very slightly overshoots around the vertex

        plt.pause(0.05)

    plt.ioff()
    plt.show()
    print("Number of Steps: ", steps)
# worry about the step later, let's just solve for replotting sequences 


