from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Gera o objeto do tipo tela
screen = Screen()

# Configurações do objeto do tipo tela
screen.setup(width=580, height=580)
screen.bgcolor("black")
screen.title("Snake")

# Desliga a atualização automática da tela, permitindo o uso dos updates manuais
screen.tracer(0)

# Analisa as entradas de botões
screen.listen()

# Inicia os objetos do tipo cobra, comida e scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Informa o estado do jogo
game_is_on = True

# Escuta os botões
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

# Enquanto o jogo estiver acontecendo...
while game_is_on:
    # Atualiza o estado da tela
    screen.update()

    # Seta uma pausa
    time.sleep(0.05)

    # Move a cobra na direção em que sua cabeça se encontra
    snake.move()

    # Se a cobra encontrar uma comida...
    if snake.head.distance(food) < 15:
        print("Comeu a comida!")
        # Aumenta o score
        scoreboard.increase_score()
        # Extende a cobra em 1
        snake.extend()
        # Reinicia a posição da comida
        food.refresh()

    # Se a cobra colidir com uma parede, reseta o jogo
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detecta colisão da cobra com sua cauda, saltando a cabeça
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Evita que a tela se feche após a execução. Ela se fechará com um clique
screen.exitonclick()