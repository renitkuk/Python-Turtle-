import turtle
import random


# Screen setup

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)


screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)



# Draw a flower

def flower(x, y):
    t.goto(x, y)

    colors = [
        "#ffb6c1",
        "#ff69b4",
        "#ff8fab",
        "#ffc0cb",
        "#ff99aa"
    ]

    t.color(random.choice(colors))
    t.dot(random.randint(2, 5))



# Recursive tree

def tree(length, angle, thickness):

    # Stop condition
    if length < 8:

        # Add flowers
        for _ in range(random.randint(2, 5)):
            x = t.xcor() + random.randint(-10, 10)
            y = t.ycor() + random.randint(-5, 10)

            flower(x, y)

        return

    # Branch color
    if length > 40:
        t.color("#7a2635")
    else:
        t.color("#a64d5c")

    t.pensize(thickness)

    # Draw branch
    t.pendown()
    t.forward(length)
    t.penup()

    # Save position and direction
    position = t.position()
    heading = t.heading()

    # Left branch
    t.setheading(heading + angle)

    tree(
        length * 0.72,
        angle * 0.9,
        max(thickness * 0.72, 1)
    )


    t.goto(position)
    t.setheading(heading)

    # Right branch
    t.setheading(heading - angle)

    tree(
        length * 0.72,
        angle * 0.9,
        max(thickness * 0.72, 1)
    )


    t.goto(position)
    t.setheading(heading)


# Start tree

t.goto(0, -350)
t.setheading(90)

tree(
    length=120,
    angle=28,
    thickness=5
)


screen.update()


turtle.done()
