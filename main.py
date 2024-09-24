import sys
import random
import time
import os

# Définition des constantes
WIDTH, HEIGHT = 80, 20
SPEED = 1
BLOCK_SIZE = 1

# Création du serpent
snake = [(20, 10), (22, 10), (24, 10)]
direction = 'RIGHT'

# Création de la nourriture
food = (40, 15)

# Boucle principale
while True:
    # Effacer l'écran
    os.system('cls' if os.name == 'nt' else 'clear')

    # Afficher le serpent et la nourriture
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print('\u2588', end='')  # Pixel noir
            elif (x, y) == food:
                print('\u2588', end='')  # Pixel noir
            else:
                print(' ', end='')
        print()

    # Attendre un peu pour contrôler la vitesse
    time.sleep(SPEED)

    # Lire les événements clavier
    direction_input = input("Direction (W/A/S/D) ? ")
    if direction_input.upper() == 'W' and direction != 'DOWN':
        direction = 'UP'
    elif direction_input.upper() == 'S' and direction != 'UP':
        direction = 'DOWN'
    elif direction_input.upper() == 'A' and direction != 'RIGHT':
        direction = 'LEFT'
    elif direction_input.upper() == 'D' and direction != 'LEFT':
        direction = 'RIGHT'

    # Déplacement du serpent
    head = snake[-1]
    if direction == 'UP':
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == 'LEFT':
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + BLOCK_SIZE, head[1])

    snake.append(new_head)

    # Vérification de la collision avec la nourriture
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0)

    # Vérification de la collision avec le bord de l'écran
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT):
        print("Game Over")
        sys.exit()