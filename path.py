import numpy as np

p_y, p_x = 4, 0 # Posicion inicial - Initial position
path = [(p_y, p_x)] # Variable donde guardar el camino final - Variable to store final path
visited = [(p_y, p_x)] # Variable para guardar casillas visitadas - Variable to store visited cells

flag = False # Bandera de detención - Detention flag

maze = np.array([
    [1, 1, 2],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 0]
])

directions = [
    (1, 0),  # Abajo - Down
    (-1, 0), # Arriba - Up
    (0, 1),  # Derecha - Rigth
    (0, -1)  # Izquierda - Left
    ]

checkpoints =[]
possible_directions = []

def imprimir_laberinto(y, x, laberinto, path):
    laberinto[y, x] = 3
    symbols = {0: '█', 1: ' ', 2: '|> ', 3: 'o', '#': '#'}  # Símbolos para las paredes, pasillos y camino

    for y in range(len(laberinto)):
        for x in range(len(laberinto[0])):
            symbol = symbols[laberinto[y][x]] if (y, x) not in path else symbols['#']
            print(symbol, end=' ')
        print()

while flag == False:

    # Recorrer cada dirección
    for dy, dx in directions:
        new_y, new_x = p_y + dy, p_x + dx
        # Verificar si la nueva posición está dentro de los límites
        if 0 <= new_y < maze.shape[0] and 0 <= new_x < maze.shape[1]:
            if maze[new_y, new_x] == 2:
                path.append((new_y, new_x))
                
                #if checkpoint len == 0: flag = True
                
                flag = True
                print("Completed")
                break
            
            if maze[new_y, new_x] == 1:
                # if checar si ya está en path
                possible_directions.append((new_y, new_x))
    
    if len(possible_directions) == 1:

        p_y = possible_directions[0][0]
        p_x = possible_directions[0][1]

        path.append((p_y, p_x))
        visited.append((p_y, p_x))

        possible_directions = []
        print(path)

    elif len(possible_directions) > 1:
        
        for (y, x) in possible_directions:
            if (y, x) in visited:
                possible_directions.remove((y, x))

        if len(possible_directions) == 1:

            p_y = possible_directions[0][0]
            p_x = possible_directions[0][1]

            path.append((p_y, p_x))
            visited.append((p_y, p_x))

            possible_directions = []        
        #if possible directions > 1, y,x append checkpoint, elegir una 
        # pass

imprimir_laberinto(4, 0, maze, path[1:len(path) - 1])

print(path)
print(visited)