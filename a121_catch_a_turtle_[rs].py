# a121_catch_a_turtle.py

#-----import statements-----

import turtle as trtl

import random as rand


#-----game configuration----
shape_of_turtle = "circle"

color_of_turtle = "green"

size_of_turtle = "5"

#-----initialize turtle-----

rikhil = trtl.Turtle()

rikhil.shape(shape_of_turtle)

rikhil.color(color_of_turtle)

rikhil.shapesize(int(size_of_turtle))

#-----game functions--------

def rikhil_clicked(x, y):
  print("Rikhil was clicked!")

# def change_position():


#-----events----------------

rikhil.onclick(rikhil_clicked)

wn = trtl.Screen()
wn.mainloop()