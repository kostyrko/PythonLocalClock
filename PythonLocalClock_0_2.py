'''simple application made for practice 
shows current time in an analoge clock format'''

import time
import turtle
window = turtle.Screen()
window.bgcolor("gray")
window.setup(width=500, height=500)
window.title("Python Local Clock v0.2")
window.tracer(0)

draw=turtle.Turtle()
draw.hideturtle()
draw.speed(0)
draw.pensize(2)

def draw_clock(h,m,s,draw):
   #face
   draw.up()
   draw.goto(0,210)
   draw.setheading(180)
   draw.color('black')
   draw.width(3)
   draw.pendown()
   draw.circle(210)

   draw.penup()
   draw.goto(0,0)
   draw.setheading(90)
   
   #draw hours
   for _ in range(12):
      draw.fd(190)
      draw.pendown()
      draw.width(2)
      draw.fd(20)
      draw.penup()
      draw.goto(0,0)
      draw.rt(30)

   #draw minutes
   # for _ in range(60):
   #    draw.fd(205)
   #    draw.pendown()
   #    draw.fd(5)
   #    draw.penup()
   #    draw.goto(0,0)
   #    draw.rt(6)
   
   #hours hand
   draw.penup()
   draw.goto(0,0)
   draw.color('white')
   draw.width(6)
   draw.setheading(90)
   angle= (h/12)*360
   draw.rt(angle)
   draw.pendown()
   draw.fd(120)

   #minutes hand
   draw.penup()
   draw.goto(0,0)
   draw.color('white')
   draw.width(4)
   draw.setheading(90)
   angle= (m/60)*360
   draw.rt(angle)
   draw.pendown()
   draw.fd(175)

   #seconds hand
   draw.penup()
   draw.goto(0,0)
   draw.color('white')
   draw.width(2)
   draw.setheading(90)
   angle= (s/60)*360
   draw.rt(angle)
   draw.pendown()
   draw.fd(175)

while True:
   h= int(time.strftime("%I"))
   m= int(time.strftime("%M"))
   s= int(time.strftime("%S"))
   draw_clock(h,m,s,draw)
   #update referes to window.tracer
   window.update()
   time.sleep(1)
   draw.clear()


window.mainloop()
