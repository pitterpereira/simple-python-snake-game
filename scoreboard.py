from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # Lê o último recorde
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())

        self.color("white")
        # levanta a caneta para evitar linhas
        self.penup() 
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    # Limpa os dados da tela e seta novos
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # Aumenta o placar
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        # Se a nova pontuação for maior que a anterior, declarar novo recorde
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        # Escreve o último recorde no arquivo data.txt
        with open("data.txt", "w") as data:
            data.write(f"{self.high_score}")
        self.update_scoreboard()