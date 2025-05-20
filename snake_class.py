from turtle import Turtle

# Constants
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]   # Initial snake body positions
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self. segments = []  # Empty list to store the turtle segments
        self.create_snake()
        self.head = self.segments[0]  #it should be after create snake bcos othervise there is no value
    

    def create_snake(self):
        """loop to initialize the snake """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self , position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """loop to move body along the head """
        for seg_num in range( len(self.segments)-1 , 0 ,-1):
            new_x = self.segments[ seg_num - 1 ].xcor()
            new_y = self.segments[ seg_num - 1 ].ycor()
            self.segments[seg_num].goto(new_x , new_y)
        self.head.forward(MOVE_DISTANCE)     

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
         if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)