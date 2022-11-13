import random

def picos(map, rayon, densite):

    x = 100  # Dimension x de la map
    y = 100  # Dimension y de la map

    for xi in range(1, x - rayon):
        for yi in range(1, y - rayon):
            if random.randint(0, 1/densite) == 0:
                for dx in range(-rayon, rayon+1):
                    for dy in range(-rayon, rayon+1):
                        map[0, yi + dy, xi + dx] = 1
    for xi in range(1, x - 1):
        for yi in range(1, y - 1):
            check = 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if map[0, yi + dy, xi + dx] == 0:
                        check = 0
            if check:
                map[1, yi, xi] = 1
    for xi in range(1, x - 1):
        for yi in range(1, y - 1):
            check = 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if map[1, yi + dy, xi + dx] == 0:
                        check = 0
            if check:
                map[2, yi, xi] = 1
    for xi in range(1, x - 1):
        for yi in range(1, y - 1):
            check = 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if map[2, yi + dy, xi + dx] == 0:
                        check = 0
            if check:
                map[3, yi, xi] = 1
