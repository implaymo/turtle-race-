import random
import turtle
from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.bgcolor("grey")
race_on = False
# Window size
screen.setup(width=500, height=400)
# List of names
colors = ["purple", "yellow", "red", "blue", "black", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# User chooses the turtle color which he thinks will win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for item_index in range(0,6):
    # Main Turtle setup
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[item_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[item_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_on = True


while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 225:
            race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"The winner is {winning_color} turtle. You win!")
            elif user_bet != winning_color:
                print(f"The winner is {winning_color} turtle. You lost! ")
            else:
                print(f"Its a draw!")

        turtle.forward(randint(0,10))







screen.mainloop()