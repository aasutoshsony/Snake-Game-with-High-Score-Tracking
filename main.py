import turtle #used for graphics
import time
import random #to generate random numbers

delay = 0.1
score = 0
high_score = 0

# for SNAKE BODY
bodies  = [] # for snake body/size 

# for GAME SCREEN
main_screen = turtle.Screen() 
main_screen.title= ('SNAKE GAME')
main_screen.bgcolor('white')
main_screen.setup(width=600,height=600)

# for SNAKE HEAD
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.fillcolor('red')
head.penup() #only start when movement is done
head.goto(0,0)
head.direction='stop'
 
# for SNAKE FOOD

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('black')
food.fillcolor('blue')
food.penup() #only start when movement is done
food.ht() #to hide food after being eaten 
food.goto(0,200)
food.st() # to show/create new food at another random place

# for SCORE BOARD

sb = turtle.Turtle()
sb.shape('square')
sb.fillcolor('black')
sb.penup()
sb.ht()
sb.goto(-280,250)
sb.write('Score: 0 | High Score: 0', font=('arial', 16,'bold'))

# FUNCTIONS
def moveup():
    if head.direction!='down':
        head.direction='up'
def movedown():
    if head.direction!='up':
        head.direction='down'
def moveleft():
    if head.direction!='right':
        head.direction='left'
def moveright():
    if head.direction!='left':
        head.direction='right'
def movestop():
    head.direction='stop'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20) 
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20) 

# Event Handling 
#(binding keyboard with code to perform actions)
main_screen.listen()
main_screen.onkey(moveup,'Up')
main_screen.onkey(movedown,'Down')
main_screen.onkey(moveleft,'Left')
main_screen.onkey(moveright,'Right')
main_screen.onkey(movestop,'space')

# MAIN LOOP (WHILE)
while True:
    main_screen.update()
    # CHECK COLLISION WITH BORDER
    if head.xcor()>280:
        head.setx(-280)
    if head.xcor()<-280:
        head.setx(280)
    if head.ycor()>280:
        head.sety(-280)
    if head.ycor()<-280:
        head.sety(280)

    # CHECK COLLISION WITH FOOD
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # INCREASE SNAKE LENGTH
        body=turtle.Turtle()
        body.penup()
        body.speed(0)
        body.shape('square')
        body.color('yellow')
        body.fillcolor('black')
        bodies.append(body) # to append new body

        # INCREASE SCORE 
        score+=10

        # CHANGE DELAY
        delay-=0.001  
        
        #UPDATE HIGHEST SCORE
        if score>high_score:
            high_score=score
        sb.clear()
        sb.write('Score: {} | high_score: {}'. format(score,high_score),font=('arial', 16,'bold') )

    # MOVE SNAKE BODY 
    for i in range(len(bodies) -1,-0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

        # When SNAKE HITS ITSELF (Check COLLISION)
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

            # HIDE BODY
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1

            # UPDATE SCCORE BOARD
            sb.clear()
            sb.write('Score: {} | high_score: {}'. format(score,high_score),font=('arial', 16,'bold') )
            
            
    time.sleep(delay) 
main_screen.mainloop()
