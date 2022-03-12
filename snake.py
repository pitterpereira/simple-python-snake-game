from lib2to3.pytree import LeafPattern
from pickletools import UP_TO_NEWLINE
from tkinter import LEFT
from turtle import Turtle

# Posições iniciais dos segmentos da cobra
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Distância percorrida por movimento
MOVE_DISTANCE = 20

# Ângulos para direcionar a cobra
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # Método construtor
    def __init__(self):
        self.segments = []
        # Cria a cobra
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ Cria os 3 segmentos da cobra de acordo com as posições iniciais """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        """ Para cada segmento da cobra, começando do último...
        start = começa do final, stop = para no início, step = de 1 em 1, subtraindo """
        for seg_num in range(len(self.segments)-1, 0, -1):
            # Nova posição do segmento baseada no segmento anterior a ele
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            # Faz o segmento ir para a posição do segmento anterior
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
            """ Adiciona um novo segmento à cobra """

            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)

            self.segments.append(new_segment)
    
    def extend(self):
        """ Pega a posição do último da lista e adiciona lá """

        self.add_segment(self.segments[-1].position())
