''' simple turtle clock app made for practice '''

import time
import turtle

class PythonLocalClock2:
    def __init__(self,window):
        self.window = window
        window.title("Python Local Clock ver. 2.1")

        window.bgcolor("goldenrod")
        window.setup(width=450, height=450)
        window.tracer(0)

        draw=turtle.Turtle()
        draw.hideturtle()
        draw.speed(0)
        draw.pensize(2)
        # draw h
        def draw_clock(h,m,s,draw):
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
            # draw min
            for i in range(12):
                draw.fd(190)
                draw.pendown()
                draw.width(2)
                draw.fd(20)
                draw.penup()
                draw.goto(0,0)
                draw.rt(30)
            # hours move
            draw.penup()
            draw.goto(0,0)
            draw.color('white')
            draw.width(6)
            draw.setheading(90)
            angle= 0.5*(60* h + m)
            draw.rt(angle)
            draw.pendown()
            draw.fd(120)
            #minutes move
            draw.penup()
            draw.goto(0,0)
            draw.color('white')
            draw.width(4)
            draw.setheading(90)
            angle= (m/60)*360
            draw.rt(angle)
            draw.pendown()
            draw.fd(175)
            # seconds move
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
            h = int(time.strftime("%I"))
            m= int(time.strftime("%M"))
            s= int(time.strftime("%S"))
            draw_clock(h,m,s,draw)
            window.update()
            time.sleep(1)
            draw.clear()


def main():
    window = turtle.Screen()
    app = PythonLocalClock2(window)
    window.mainloop()


if __name__ == '__main__':
    main()