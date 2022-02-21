# -	Scoreboard
# - Create screen
# -	Random moving left to right ball
# -	When ball hit left or right go to opposite direction
# -	When ball hit left or right go to opposite direction and touch wall
# -	When ball hit left or right go to opposite direction and miss
# -	Able to move left paddle
# -	Able to move right paddle

from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong")
screen.tracer(0)

screen.exitonclick()