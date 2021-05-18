import turtle
tortuguita = turtle.Turtle()
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'pink','light blue']
for i in range(300):
  tortuguita.color(colors[i%8])
  tortuguita.forward(300)
  tortuguita.left(170)
  tortuguita.speed(100)
