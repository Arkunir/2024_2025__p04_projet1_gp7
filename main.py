import sys
import random
import time
import os

# Définition des constantes
WIDTH, HEIGHT = 20, 20
SPEED = 0.5
BLOCK_SIZE = 1

# Création du serpent
snake = [(10, 10), (11, 10), (12, 10)]
direction = 'RIGHT'

# Création de la nourriture
food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
        random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

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

    # Changement de direction aléatoire
    if random.random() < 0.1:
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        directions.remove(direction)
        direction = random.choice(directions)ssww