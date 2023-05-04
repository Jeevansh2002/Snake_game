
from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Score

snake = Snake()
food = Food()
score = Score()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
is_game_on = True
screen.tracer(0)
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    score.score_board()

    #Collision with Turtle
    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.goto()
        score.increment()

    #Collision with wall
    if snake.snakes[0].ycor() > 295 or snake.snakes[0].ycor() < -295:
        score.high_score()
        snake.new_snake()


    #Getting from other side
    if snake.snakes[0].xcor() < -285:
        for i in snake.snakes:
            y_cor = snake.snakes[0].ycor()
            snake.snakes[0].goto(285, y_cor)
    if snake.snakes[0].xcor() > 285:
        for j in snake.snakes:
            y_cor_2 = snake.snakes[0].ycor()
            snake.snakes[0].goto(-285, y_cor_2)

    #Collision with it's own tail
    for i in snake.snakes:
        if snake.snakes[0] == i:
            pass
        elif snake.snakes[0].distance(i) < 10:
            score.high_score()
            snake.new_snake()




















screen.exitonclick()