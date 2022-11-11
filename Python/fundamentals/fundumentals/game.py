import turtle
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=1000, height=800)
wn.tracer(0)



# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"q")
wn.onkeypress(paddle_a_down,"a")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
# Main game loop
while True:
    wn.update()
    # ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.xcor() + ball.dy)
    # border checking
    if ball.ycor() > 385:
        ball.sety(385)
        ball.dy *= -2
        
    if ball.ycor() < -385:
        ball.sety(-385)
        ball.dy *= -2