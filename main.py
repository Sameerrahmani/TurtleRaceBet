from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Choose turtle", prompt="Which turtle will win the race? ").lower()
colors = ["red", "green", "orange", "purple", "blue", "yellow"]
positionY = [100, 70, 40, 10, -20, -50]
turtles = []


for turtle in range(0, 6):
  tim = Turtle(shape="turtle")
  tim.penup()
  tim.color(colors[turtle])
  tim.goto(x=-230, y=positionY[turtle])
  turtles.append(tim)


if user_bet:
  racing = True

while racing == True:
  for turtle in turtles:
    random_speed = random.randint(0, 10)
    turtle.forward(random_speed)
    if turtle.xcor() > 230:
      racing = False
      print(turtle.pencolor() + " has won the race")
      if user_bet == turtle.pencolor():
        print("You won the bet!")
      else:
        print("You didn't win the bet!")
  

screen.exitonclick()
