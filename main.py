from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pongyy Game")
screen.tracer(0)

paddle_right=Paddle(350,0)
paddle_left=Paddle(-350,0)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collison with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()


    #collison with paddle
    if ball.distance(paddle_right)<50 and ball.xcor()>320 or ball.distance(paddle_left)<50 and ball.xcor()<-320:
        ball.bounce_x()


    #when right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()


    #when left paddle misses
    if ball.xcor()<-360:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()