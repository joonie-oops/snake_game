from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.title("My Snake Game")
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)
my_screen.listen()

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

my_screen.onkeypress(my_snake.up, "Up")
my_screen.onkeypress(my_snake.down, "Down")
my_screen.onkeypress(my_snake.left, "Left")
my_screen.onkeypress(my_snake.right, "Right")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    my_snake.move()

    if my_snake.head.xcor() > 285 or my_snake.head.xcor() < -285 or my_snake.head.ycor() > 285 or my_snake.head.ycor() < -285:
        print(my_snake.head.xcor(), my_snake.head.ycor())
        game_is_on = False

    if my_snake.head.distance(my_food) < 15:
        my_food.rand_position()
        my_snake.extend()
        my_scoreboard.update_score()

    if my_snake.snake_eat_self():
        game_is_on = False


my_scoreboard.end()












my_screen.exitonclick()