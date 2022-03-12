from turtle import Turtle
import random

# Classe herdada da classe Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Define o formato de círculo
        self.shape("circle")
        # Remove a "caneta" da tela para evitar a criação de linhas ao movimentar o score para cima
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """ Atualiza a posição da comida, gerando posições compatíveis com a posição 
        onde a cobra passa, já que ela se movimenta de 20 em 20 e a tela tem 560/560 """

        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)

