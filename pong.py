import turtle as tur
#creating record variables
playerAscore = 0
playerBscore = 0
#creating a new window
window = tur.Screen()
window.title("Turtle python pong game")
window.bgcolor("black")
window.setup(width= 800, height= 600)
window.tracer(0)
#creating left paddle
lp = tur.Turtle()
lp.speed(0)
lp.shape("square")
lp.color("white")
lp.shapesize(stretch_wid=5, stretch_len=1)
lp.penup()
lp.goto(-340, 0)
#creating right paddle
rp = tur.Turtle()
rp.speed(0)
rp.shape("square")
rp.color("white")
rp.shapesize(stretch_wid=5, stretch_len=1)
rp.penup()
rp.goto(340, 0)
#creating new ball
ball = tur.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,0)
ballXdirection = 0.5
ballYdirection = 0.5
#creating a new pen for updating scoreboard
pen = tur.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0                    player B: 0", align= 'center', font = ('Arial', 24, 'normal'))
#updating the position of left paddle
def lpUp():
    y = lp.ycor()
    y = y + 16
    lp.sety(y)
def lpDown():
    y = lp.ycor()
    y = y - 16
    lp.sety(y)
#updating the position of right paddle
def rpUp():
    y = rp.ycor()
    y = y + 16
    rp.sety(y)
def rpDown():
    y = rp.ycor()
    y = y - 16
    rp.sety(y)
#Assign playing keys
window.listen()
window.onkeypress(lpUp, 'w')
window.onkeypress(lpDown, 's')
window.onkeypress(rpUp, 'i')
window.onkeypress(rpDown, 'k')
#creating main loop
while True: 
    window.update()

    #moving the ball
    ball.setx(ball.xcor() + ballXdirection)
    ball.sety(ball.ycor() + ballYdirection)

    #creating border
    if ball.ycor()> 290: 
        ball.sety(290)
        ballYdirection = ballYdirection * -1
    if ball.ycor()< -290: 
        ball.sety(-290)
        ballYdirection = ballYdirection * -1

    if ball.xcor() > 390: 
        ball.goto(0,0)
        ballXdirection = ballXdirection
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Player A: {}                    player B: {}".format(playerAscore, playerBscore), align= 'center', font = ('Arial', 24, 'normal'))

    if ball.xcor() < -390: 
        ball.goto(0,0)
        ballXdirection = ballXdirection
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A: {}                    player B: {}".format(playerAscore, playerBscore), align= 'center', font = ('Arial', 24, 'normal'))
    
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rp.ycor() + 40 and ball.ycor() > rp.ycor() - 40):
        ball.setx(340)
        ballXdirection = ballXdirection * -1
    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < lp.ycor() + 40 and ball.ycor() > lp.ycor() - 40):
        ball.setx(-340)
        ballXdirection = ballXdirection * -1
    