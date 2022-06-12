from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.shape("square")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(pos_x,pos_y)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)