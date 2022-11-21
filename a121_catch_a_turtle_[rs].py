# a121_catch_a_turtle.py

#-----import statements-----

import turtle as trtl

import random as rand


#-----game configuration----
shape_of_turtle = "circle"

color_of_turtle = "green"

size_of_turtle = 5

score = 0

font_setup = ("Arial", 20, "normal")

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

wn = trtl.Screen()

#-----initialize turtle-----

rikhil = trtl.Turtle()

score_writer = trtl.Turtle()

counter =  trtl.Turtle()

rikhil.shape(shape_of_turtle)

rikhil.color(color_of_turtle)

rikhil.shapesize(size_of_turtle)


#-----game functions--------


def rikhil_clicked(x, y):
  if timer_up == False:
    update_score()

    change_position()
  
  

def change_position():
  new_xpos = rand.randint(-400, 400)
  new_ypos = rand.randint(-300, 300) 
  rikhil.hideturtle()
  rikhil.goto(new_xpos, new_ypos)
  rikhil.showturtle()
  
def update_score():
  global score # gives this function access to the score that was created above
  score += 1
  score_writer.clear()
  score_writer.write("Score: " + str(score), font=font_setup)  
  
  
def score_setup():
  score_writer.penup()
  score_writer.hideturtle()
  score_writer.goto(-300, 200)
  score_writer.write("Score: " + str(score), font=font_setup)  



def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    
def countdown_setup():
  counter.penup()
  counter.hideturtle()
  counter.goto(200, 200)
#-----events----------------

wn.bgcolor("red")

rikhil.penup()

score_setup()
countdown_setup()
countdown()
rikhil.onclick(rikhil_clicked)




wn.mainloop()