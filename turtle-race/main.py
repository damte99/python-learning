from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race?")
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']
turtles = []
is_race_on = True
for color in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[color].color(colors[color])
    curr_y = -85 + color * 30
    turtles[color].penup()
    turtles[color].goto(-230, curr_y)
while is_race_on:
    for timmy in turtles:
        if timmy.xcor() > 230:
            winner_color = timmy.pencolor()
            print(f"{winner_color} turtle won!")
            if winner_color == user_bet:
                print("You win!")
            else:
                print("You lose.")
            is_race_on = False
            break
        new_forward = random.randint(0, 10)
        timmy.forward(new_forward)

screen.exitonclick()
