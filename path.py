import numpy as np
import time

p_y, i_y = 13 , 13 # Posicion inicial - Initial position
p_x, i_x = 0 , 0

visited = [] # Variable para guardar casillas visitadas - Variable to store visited cells
possible_directions = []

flag = False # Bandera de detención - Detention flag
goal = False

maze = np.array([
    [1, 1, 1, 1, 1, 1, 1],      # 0
    [1, 0, 0, 1, 0, 0, 1],      # 1
    [1, 1, 0, 1, 1, 0, 1],      # 2
    [1, 0, 0, 2, 0, 0, 1],      # 3
    [1, 0, 1, 0, 1, 0, 1],      # 4
    [1, 0, 1, 1, 0, 0, 1],      # 5
    [0, 1, 1, 1, 1, 1, 1],      # 6
    [0, 0, 0, 1, 0, 0, 1],      # 7
    [1, 0, 1, 1, 1, 0, 1],      # 8
    [1, 0, 1, 1, 0, 1, 1],      # 9
    [1, 0, 1, 1, 0, 0, 1],      # 10
    [1, 1, 1, 1, 1, 0, 1],      # 11
    [1, 0, 0, 1, 0, 0, 1],      # 12
    [1, 1, 1, 1, 1, 1, 1] 
    #0  1  2  3  4  5  6
    ])


directions = [
    (1, 0),  # Abajo - Down
    (-1, 0), # Arriba - Up
    (0, 1),  # Derecha - Rigth
    (0, -1),  # Izquierda - Left
    ]

def imprimir_laberinto(y, x, laberinto, path):
    laberinto[y, x] = 3
    symbols = {0: '█', 1: ' ', 2: '>', 3: 'o', '#': '#'}  # Símbolos para las paredes, pasillos y camino

    for y in range(len(laberinto)):
        for x in range(len(laberinto[0])):
            symbol = symbols[laberinto[y][x]] if (y, x) not in path else symbols['#']
            print(symbol, end=' ')
        print()

while flag == False:

    # Recorrer cada dirección
    for dy, dx in directions:
        new_y, new_x = p_y + dy, p_x + dx
        if 0 <= new_y < maze.shape[0] and 0 <= new_x < maze.shape[1]:
            if maze[new_y, new_x] == 2:
                visited.append((new_y, new_x))
                goal = True
                print("Completed \n")
                #print(visited)
            
            if maze[new_y, new_x] == 1:
                if (new_y, new_x) not in possible_directions:
                    possible_directions.append((new_y, new_x))

    visited.append((p_y, p_x))

    possible_directions = [(y, x) for (y, x) in possible_directions if (y, x) not in visited] # Improved possible directions

#    print(possible_directions)
#    print(p_y, p_x)
    
    if len(possible_directions) == 1:

        p_y = possible_directions[0][0]
        p_x = possible_directions[0][1]

        possible_directions.remove((p_y, p_x))
        
        #print(p_y, p_x, " ==1 ")

        # if goal:
        #     print(visited)

        #print(" ////////////// ")


    elif len(possible_directions) > 1:
        
        p_y = possible_directions[0][0]
        p_x = possible_directions[0][1]

        possible_directions.remove((p_y, p_x))

        #print(p_y, p_x, " > 1 ")
        
        # if goal:
        #     print(visited)
        
        #print(" ////////////// ")
    
    elif len(possible_directions) == 0:

        if goal == True and possible_directions == []:
            flag = True
            break

    #time.sleep(0.2) # just for debugging

imprimir_laberinto(i_y, i_x, maze, visited[1:len(visited) - 1])

print("\n Visited: ", visited)
#print("possible: ", possible_directions)