from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        # levanta a caneta para evitar linhas
        self.penup() 
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    # Limpa os dados da tela e seta novos
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Aumenta o placar
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        # Centraliza o texto na tela
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)