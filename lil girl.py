import turtle
import random
import math

# Draw a heart
def draw_heart(t, size, color):
    t.begin_fill()
    t.color(color)
    t.left(140)
    t.forward(size)
    t.circle(-size // 2, 200)
    t.left(120)
    t.circle(-size // 2, 200)
    t.forward(size)
    t.end_fill()
    t.setheading(0)

# Draw some sparkles
def draw_sparkle(x, y):
    sparkle = turtle.Turtle()
    sparkle.hideturtle()
    sparkle.speed(0)
    sparkle.penup()
    sparkle.goto(x, y)
    sparkle.color("white")
    sparkle.pendown()
    for _ in range(8):
        sparkle.forward(10)
        sparkle.backward(10)
        sparkle.left(45)

# Draw Hello Kitty-like face (simplified)
def draw_hello_kitty():
    kitty = turtle.Turtle()
    kitty.speed(0)
    kitty.penup()
    kitty.goto(150, -200)
    kitty.pendown()
    kitty.color("black", "white")
    kitty.begin_fill()
    kitty.circle(40)  # Face
    kitty.end_fill()

    # Eyes
    for x in [-15, 15]:
        kitty.penup()
        kitty.goto(150 + x, -180)
        kitty.dot(10, "black")

    # Nose
    kitty.penup()
    kitty.goto(150, -190)
    kitty.dot(6, "orange")

    # Bow
    kitty.penup()
    kitty.goto(180, -160)
    kitty.color("hotpink")
    kitty.begin_fill()
    kitty.circle(8)
    kitty.end_fill()

    for angle in [20, -20]:
        kitty.penup()
        kitty.goto(180, -160)
        kitty.setheading(angle)
        kitty.begin_fill()
        kitty.circle(12, 180)
        kitty.end_fill()

# Draw hearts
def draw_hearts():
    screen = turtle.Screen()
    screen.bgcolor('lightpink')

    t = turtle.Turtle()
    t.speed(3)
    t.width(3)

    sizes = [250, 200, 150, 100, 50]
    colors = ['#e91e63', '#f06292', '#f8bbd9', '#fce4ec', '#e91e63']
    for size, color in zip(sizes, colors):
        t.penup()
        t.goto(0, -size // 2)
        t.pendown()
        draw_heart(t, size, color)

    t.hideturtle()

    # Add sparkles
    for _ in range(20):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        draw_sparkle(x, y)

    # Add cute text
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(0, 300)
    text.color("#880e4f")
    text.write("Made with Love 💕, For My Beautiful Samira💖", align="center", font=("Comic Sans MS", 18, "bold"))

    # Add Hello Kitty drawing
    draw_hello_kitty()

    turtle.done()

# Run everything
draw_hearts()
