import turtle as t
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    # screen.write(scoreboard)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nommm")
        food.refresh()
        scoreboard.update_score()
        snake.add_segment()


screen.exitonclick()
