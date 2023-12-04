from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)  # ---------------- tracer is used for turn of/on the animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #     DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #     DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    #     DETECT COLLISION WITH TAIL
    for segment in snake.segments:
        if segment == snake.head:                      # -- snake.head = segments[0]
            pass
        elif snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
