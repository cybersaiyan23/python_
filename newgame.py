import turtle

wn = turtle.Screen()
wn.title("game by gokul")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


paddle_a =turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(0,-270)

paddle_b =turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=1, stretch_len=5)
paddle_b.penup()
paddle_b.goto(0,270)

paddle_c =turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("white")
paddle_c.shapesize(stretch_wid=1, stretch_len=5)
paddle_c.penup()
paddle_c.goto(170,270)

paddle_d =turtle.Turtle()
paddle_d.speed(0)
paddle_d.shape("square")
paddle_d.color("white")
paddle_d.shapesize(stretch_wid=1, stretch_len=5)
paddle_d.penup()
paddle_d.goto(-170,270)

paddle_e =turtle.Turtle()
paddle_e.speed(0)
paddle_e.shape("square")
paddle_e.color("white")
paddle_e.shapesize(stretch_wid=1, stretch_len=5)
paddle_e.penup()
paddle_e.goto(-320,170)

paddle_f =turtle.Turtle()
paddle_f.speed(0)
paddle_f.shape("square")
paddle_f.color("white")
paddle_f.shapesize(stretch_wid=1, stretch_len=5)
paddle_f.penup()
paddle_f.goto(320,170)

pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)



ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = -0.5
ball.dy = -0.5


score_b=0
score_c=0
score_d=0
score_e=0
score_f=0




def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

def paddle_a_left():
    x = paddle_a.xcor()
    x -=20
    paddle_a.setx(x)

wn.listen()
wn.onkeypress(paddle_a_right,"Right")
wn.onkeypress(paddle_a_left,"Left")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() <-390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() < -290:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.ycor() < -250 and ball.ycor() > -270:
            if ball.xcor() < paddle_a.xcor() + 20 and ball.xcor() > paddle_a.xcor() - 20:
                ball.sety(-250)
                ball.dy *= -1

            if ball.xcor() > paddle_a.xcor() + 20 and ball.xcor() < paddle_a.xcor() +40:

                ball.sety(-250)
                ball.dy *= -1
                if ball.dx == -0.5:
                    ball.dx *= -1

                

            if ball.xcor() < paddle_a.xcor() - 20 and ball.xcor() > paddle_a.xcor() -40:
                ball.sety(-250)
                ball.dy *= -1
                if ball.dx == 0.5:
                    ball.dx *= -1     
        
             
       
        
    if score_b==0:
        if ball.ycor() > 250  and ball.ycor() < 290 and ( ball.xcor() < paddle_b.xcor() + 40 and ball.xcor() >paddle_b.xcor() - 40):
            ball.sety(250)
            ball.dy *= -1
            paddle_b.color("red")
            score_b += 1

    if score_b==1:
        if ball.ycor() > 250  and ball.ycor() < 290 and ( ball.xcor() < paddle_b.xcor() + 40 and ball.xcor() >paddle_b.xcor() - 40):
            ball.sety(250)
            ball.dy *= -1
            paddle_b.color("black")
            score_b += 1       
    
    if score_c==0:
        if ball.ycor() > 250  and ball.ycor() < 290 and ( ball.xcor() < paddle_c.xcor() + 40 and ball.xcor() >paddle_c.xcor() - 40):
            ball.sety(250)
            ball.dy *= -1
            paddle_c.color("red")
            score_c += 1

    if score_c==1:
        if ball.ycor() > 250  and ball.ycor() < 290 and ( ball.xcor() < paddle_c.xcor() + 40 and ball.xcor() >paddle_c.xcor() - 40):
            ball.sety(250)
            ball.dy *= -1
            paddle_c.color("black")
            score_c += 1
        
    if score_d==0:
        if ball.ycor() > 250  and ball.ycor() < 290 and ( ball.xcor() < paddle_d.xcor() + 40 and ball.xcor() >paddle_d.xcor() - 40):
            ball.sety(250)
            ball.dy *= -1
            paddle_d.color("red")
            score_d += 1

    if score_d==1:
        if ball.ycor() > 250  and ball.ycor() < 290 and ( ball.xcor() < paddle_d.xcor() + 40 and ball.xcor() >paddle_d.xcor() - 40):
            ball.sety(250)
            ball.dy *= -1
            paddle_d.color("black")
            score_d += 1


    if score_e==0:
        if ball.ycor() > 150  and ball.ycor() < 190 and ( ball.xcor() < paddle_e.xcor() + 40 and ball.xcor() >paddle_e.xcor() - 40):
            if ball.dy == 0.5:
                ball.sety(150)
            
            else:
                ball.sety(190)
            ball.dy *= -1
            ball.dx *= -1
            paddle_e.color("red")
            score_e += 1    
    if score_e==1:
        if ball.ycor() > 150  and ball.ycor() < 190 and ( ball.xcor() < paddle_e.xcor() + 40 and ball.xcor() >paddle_e.xcor() - 40):
            if ball.dy == 0.5:
                ball.sety(150)
            
            else:
                ball.sety(190)
            ball.dy *= -1
            ball.dx *= -1
            paddle_e.color("black")
            score_e += 1


    if score_f==0:
        if ball.ycor() > 150  and ball.ycor() < 190 and ( ball.xcor() < paddle_f.xcor() + 40 and ball.xcor() >paddle_f.xcor() - 40):
            if ball.dy == 0.5:
                ball.sety(150)
            
            else:
                ball.sety(190)
            ball.dy *= -1
            ball.dx *= -1
            paddle_f.color("red")
            score_f += 1

    if score_f==1:
        if ball.ycor() > 150  and ball.ycor() < 190 and ( ball.xcor() < paddle_f.xcor() + 40 and ball.xcor() >paddle_f.xcor() - 40):
            if ball.dy == 0.5:
                ball.sety(150)
            
            else:
                ball.sety(190)
            ball.dy *= -1
            ball.dx *= -1
            paddle_f.color("black")
            score_f += 1

    if score_c==2 and score_b ==2 and score_d==2 and score_e==2 and score_f==2 : 
        pen.write("You Won!!!", align="center", font=("Courier",24,"normal"))