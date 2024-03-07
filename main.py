import turtle as t

# Setup Screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Create Snake Body
starting_positions = [(0,0), (-20,0), (-40, 0)]
segments = [] 

for position in starting_positions:
    new_segment = t.Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(10)

# Close on Click
screen.exitonclick()