import turtle
from turtle import Turtle, Screen
import random

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

ceiling = 290
floor = -290


class Paddle(Turtle):

    def __init__(self, start_x, start_y, shape="square"):
        #Turtle().__init__(self, shape=shape)
        super(Paddle, self).__init__(shape="square")
        self.speed(0)
        #self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(start_x, start_y)
        self.heightArea = (self.ycor() + 2.5*10, self.ycor() - 2.5*10)
        self.score = 0

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

class Ball(Turtle):

    def __init__(self, start_x, start_y, shape="square"):
        super(Ball, self).__init__(shape="square")
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(start_x, start_y)
        self.dx = 2 * (-1)**(random.randint(1, 9))
        self.dy = 2 * (-1)**(random.randint(1, 9))

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def boarderBounceY(self):
        if self.ycor() > (ceiling):
            self.sety(ceiling)
            self.dy *= -1

        if self.ycor() < (floor):
            self.sety(floor)
            self.dy *= -1

    def paddleBounce(self):
        if self.ycor() < abs(Paddle.heightArea[0] - Paddle.heightArea[1]):
            if self.xcor() < Paddle.xcor():
                self.setx(Paddle.xcor())
                self.dx *= -1
        




# Initilize
#score_board = scoreBoard()
paddleA = Paddle(-350, 0)
paddleB = Paddle(350, 0)
ball = Ball(0,0)

# Keyboard binding
wn.listen()
wn.onkeypress(paddleA.move_up, "w")
wn.onkeypress(paddleA.move_down, "s")
wn.onkeypress(paddleB.move_up, "Up")
wn.onkeypress(paddleB.move_down, "Down")


# ------------------ Main Loop --------------- #
mainLoop = True
while mainLoop:
    wn.update()

    #score_board.drawScore()

    turtle.color('deep pink')
    style = ('Courier', 30, 'italic')
    turtle.write(f'Score: {paddleA.score} | {paddleB.score}', font=style, align='center')
    turtle.hideturtle()


    ball.move()
    ball.boarderBounceY()


    if ball.xcor() > (390):
        ball.goto(0,0)
        turtle.clear()
        paddleA.score += 1
        ball.dx *= -1

    if ball.xcor() < (-390):
        ball.goto(0,0)
        turtle.clear()
        paddleB.score += 1
        ball.dx *= -1

    if (ball.xcor()) < (paddleA.xcor() + 10) and (ball.xcor() > paddleA.xcor()):
        if (ball.ycor() < paddleA.ycor() + 50) and (ball.ycor() > paddleA.ycor() - 50):
            #ball.setx(paddleA.xcor())
            ball.dx *= -1

    if (ball.xcor()) > (paddleB.xcor() - 10) and (ball.xcor() < (paddleB.xcor())):
        if (ball.ycor() < paddleB.ycor() + 50) and (ball.ycor() > paddleB.ycor() - 50):
            #ball.setx(paddleB.xcor())
            ball.dx *= -1