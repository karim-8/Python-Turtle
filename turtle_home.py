
# Libaray inside Python sdk.
import turtle

# Window creation. 
window = turtle.Screen()
window.title("ping Pong Game")
window.bgcolor("grey")
window.setup(width=800, height=800)
window.tracer(0) # stops window from updating automatically.

# Method to creating the two paddles.
def createPaddle(paddleColor, paddleWidth, paddleLength, paddleX, PaddleY, paddleShape=None,):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.color(paddleColor)
    if paddleShape != None: paddle.shape(paddleShape) 
   # paddle.shape(paddleShape) 
    paddle.shapesize(stretch_wid = paddleWidth, stretch_len = paddleLength)
    paddle.penup()
    paddle.goto(paddleX,PaddleY)

createPaddle("yellow", 5, 1, -350, 0, "square",) # First Paddle
createPaddle("red", 5, 1, 350, 0, "square") # Second Paddle
createPaddle("white", 5, 1, 0, 0,"square") # Paddle ball


while True: 
    window.update() # Update screen everytime loop run in the game
        