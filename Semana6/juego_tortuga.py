import turtle
import random
import time
score = 0
font = ("Arial", 24, "normal")

def updates():
  scorek.clear()
  scorek.write(score, font=font)

def checkFood():
  global score
  if player.distance(food) < 20:
    food.ht()
    food.goto(random.randint(-275,275),random.randint(-150,150))
    food.setheading(random.randint(0,360))
    food.st()
    score = score+1
    updates()
  if player.distance(enemy) < 15:
    enemy.ht()
    enemy.speed(0)
    enemy.goto(random.randint(-275,275),random.randint(-150,150))
    enemy.speed(2)
    enemy.st()
    if score > 0:
      score = score-1
      updates()

def move():
  enemy.speed(0)
  enemy.setheading(enemy.towards(player.xcor(), player.ycor()))
  enemy.speed(2)
  enemy.forward(9.5)

def l():
  player.left(10)

def r():
  player.right(10)

def u():
  player.forward(10)
  move()
  checkFood()

def d():
  player.backward(10)
  move()
  checkFood()
  

wn = turtle.Screen()


food = turtle.Turtle()
food.shape("triangle")
food.pu()
food.color("orange")
food.speed(0)
food.goto(random.randint(-275,275),random.randint(-150,150))
food.setheading(random.randint(0,360))

player = turtle.Turtle()
player.shape("arrow")
player.pu()
player.color("black")
player.speed(2)
player.goto(0,0)

enemy = turtle.Turtle()
enemy.ht()
enemy.shape("circle")
enemy.pu()
enemy.color("blue")
enemy.speed(0)
enemy.goto(random.randint(-275,275),random.randint(-150,150))
enemy.speed(2)
enemy.st()

scorek = turtle.Turtle()
scorek.ht()
scorek.pu()
scorek.speed(0)
scorek.goto(275,150)
updates()

wn.onkey(l, "Left")
wn.onkey(r, "Right")
wn.onkey(u, "Up")
wn.onkey(d, "Down")
wn.listen()
