
# Libaray inside Python sdk.
import turtle

# Window creation. 
window = turtle.Screen()
window.title("ping Pong Game")
window.bgcolor("grey")
window.setup(width=800, height=800)
window.tracer(0) # stops window from updating automatically.

#First Paddle
paddle1 = turtle.Turtle() # Intialize object from turtle
paddle1.speed(0) #Initialize speed of the animation
paddle1.color("yellow") # set color of the shape
paddle1.shape("square")     
paddle1.shapesize(stretch_wid = 5, stretch_len = 1) # Stretch the shape to meet the size
paddle1.penup() #stop object from drawing lines
paddle1.goto(-350,0) #set the initial position of the paddle
    
#Second Paddle
paddle2 = turtle.Turtle() # Intialize object from turtle
paddle2.speed(0) #Initialize speed of the animation
paddle2.color("yellow") # set color of the shape
paddle2.shape("square")     
paddle2.shapesize(stretch_wid = 5, stretch_len = 1) # Stretch the shape to meet the size
paddle2.penup() #stop object from drawing lines
paddle2.goto(350,0) #set the initial position of the paddle
    
 #Ball Creation
ball = turtle.Turtle() #Intialize the ball
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)   
ball.dx = 2.5 # ball speed To move diaognally 
ball.dy = 2.5 # ball speed delta

#Function to move the paddle up "Increasing Y Axis"
def movePaddleUp():
    y = paddle1.ycor() # Getting the  Y coordinates of the first paddle
    y +=20  # Increase each move by 20 
    paddle1.sety(y) #Updating the new place
    
def movePaddleDown():
    y = paddle1.ycor() # Calling Y coordinates
    y -=20  # Increase each move by 20 
    paddle1.sety(y) #Updating the new place    
    
def movePaddle2Up():
    y = paddle2.ycor() # Calling Y coordinates
    y +=20  # Increase each move by 20 
    paddle2.sety(y) #Updating the new place
    
def movePaddle2Down():
    y = paddle2.ycor() # Calling Y coordinates
    y -=20  # Increase each move by 20 
    paddle2.sety(y) #Updating the new place        
    
#Keyboard bindings # Listening when "w" or "s" Tapped and call the required func
window.listen()
window.onkeypress(movePaddleUp,"w")    
window.onkeypress(movePaddleDown,"s")
window.onkeypress(movePaddle2Up,"Up")    
window.onkeypress(movePaddle2Down,"Down")

#Function to move the paddle down


while True: 
    window.update() # Update screen everytime loop run in the game
    ball.setx(ball.xcor() + ball.dx) # Ball place in 0 then add 2.5 to the X Axis
    ball.sety(ball.ycor() + ball.dy) # Ball place in x then add 2.5 to the Y Axis
    
    #Top & Bottom Border Chek
    if ball.ycor() > 290: # If ball is on the top border
        ball.sety(290) # set y axis +290
        ball.dy *= -1 # Reverse to go reversed direction -2.5 instead of 2.5
        
    if ball.ycor() <-290: # If ball is on the bottom border
        ball.sety(-290) # set y axis -290
        ball.dy *= -1 # Reverse to go reversed direction 2.5 instead of -2.5
            
    if ball.xcor() > 390:   # if ball is right 
        ball.goto(0,0)  # Return ball to center
        ball.dx *= -1 # reverse the x direction
        
    if ball.xcor() < -390:    # if ball is left 
        ball.goto(0,0) # Return ball to center
        ball.dx *= -1 # reverse the x direction
        