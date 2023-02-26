import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")
cars = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    for car in range(len(cars.all_cars)):
        if player.distance(cars.all_cars[car]) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        player.goto(0, -280)
        cars.next_level()
        scoreboard.level_up()


screen.exitonclick()
