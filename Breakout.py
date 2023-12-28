# Breakout Game
import turtle
import random
import time

win = turtle.Screen()
win.title("Breakout Game")
win.setup(width=600, height=600)
win.bgcolor("black")
win.tracer(0)

# Border
border = turtle.Turtle()
border.speed(0)
border.color("blue")
border.penup()
border.goto(-295, 295)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(580)
    border.rt(90)
border.hideturtle()

score = 0
lives = 5

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 2
ball.dy = 2

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("white")
paddle.penup()
paddle.goto(0, -250)

# Set the paddle speed
paddle_speed = 20

# Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.goto(100, 255)
score_pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
score_pen.hideturtle()

# Score
lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.color("white")
lives_pen.penup()
lives_pen.goto(-100, 255)
lives_pen.write("Lives: 5", align="center", font=("Courier", 24, "normal"))
lives_pen.hideturtle()

# Bricks
num_bricks = 30
bricks = []
colors = ["chocolate4", "dark goldenrod4", "dark orange", "dark goldenrod1"]
for i in range(num_bricks):
    brick = turtle.Turtle()
    brick.speed(0)
    brick.shape("square")
    brick.shapesize(stretch_wid=1.2, stretch_len=4.4)
    brick.color(random.choice(colors))
    brick.penup()
    x = -245 + ((i % 6) * 96)
    y = 240 - ((i // 6) * 32)
    brick.goto(x, y)
    bricks.append(brick)


# Paddle movements
def paddle_right():
    x = paddle.xcor()
    x += paddle_speed
    if x > 230:
        x = 230
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x -= paddle_speed
    if x < -240:
        x = -240
    paddle.setx(x)


# Keyboard input
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

while True:
    win.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with paddle
    if ball.ycor() < -230 and (paddle.xcor() - 53 < ball.xcor() < paddle.xcor() + 53):
        ball.sety(-230)
        ball.dy *= -1

    # Ball collision with border
    if ball.xcor() > 275:
        ball.setx(275)
        ball.dx *= -1

    if ball.xcor() < -280:
        ball.setx(-280)
        ball.dx *= -1

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    # Check for loss condition
    if ball.ycor() < -275 and lives < 1:
        paddle.goto(0, -250)
        ball.hideturtle()
        lives_pen.goto(0, 0)
        lives_pen.write("Game Over!", False, align="center", font=("Courier", 36, "normal"))
        time.sleep(1)

    if ball.ycor() < -275 and lives > 0:
        paddle.goto(0, -250)
        ball.goto(0, -230)
        ball.dx *= -1
        lives -= 1
        lives_pen.clear()
        lives_pen.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))

    # Ball collision with Bricks:
    for brick in bricks:
        if (brick.xcor() - 45 < ball.xcor() < brick.xcor() + 45) and (
                brick.ycor() - 20 < ball.ycor() < brick.ycor() + 20):
            brick.goto(1000, 1000)
            ball.dy *= -1
            score += 10
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Check for win condition
        if score == num_bricks * 10:
            ball.hideturtle()
            score_pen.goto(0, 0)
            score_pen.write("You Win!", False, align="center", font=("Courier", 36, "normal"))
            time.sleep(1)
            break
