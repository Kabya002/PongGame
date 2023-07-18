from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LIVES = 5
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((380, 0))
paddle_l = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

lives_r = LIVES
lives_l = LIVES
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -340 or ball.distance(paddle_r) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    # detect R player
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        lives_r -= 1

    # detect L player
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        lives_l -= 1

    if lives_r == 0 or lives_l == 0:
        game_is_on = False
        score.game_over()

screen.exitonclick()
