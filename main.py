from turtle import Screen
import time
from snake_class import Snake
from food import Food  # type: ignore
from score import Scoreboard # type: ignore

# Set up the screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=600 , height= 600)
screen.title("Snake Game")
screen.tracer(0)

# Create game objects
food = Food()
snake = Snake()
scoreboard = Scoreboard() 

# Listen for keyboard events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()  #helps avoiding delay in moving back part of the snake
    time.sleep(0.1) # control the speed of the snake
    snake.move()

    #detrect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

        snake.extend()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]: # for the first iteration , head - head distance is 0 so game over in 1st iteration, hence its necessary
        if snake.head.distance(segment) < 10:  
            pass
            game_on = False
            scoreboard.game_over()

screen.exitonclick()