import numpy as np

p_y, i_y = 6 , 6 # Posicion inicial - Initial position
p_x, i_x = 0 , 0
path = [(p_y, p_x)] # Variable donde guardar el camino final - Variable to store final path
visited = [(p_y, p_x)] # Variable para guardar casillas visitadas - Variable to store visited cells

flag = False # Bandera de detención - Detention flag
goal = False

# maze = np.array([
#     [1, 1, 1, 1, 1, 1, 2],      # 0
#     [1, 0, 0, 0, 1, 0, 0],      # 1
#     [1, 1, 0, 1, 1, 1, 0],      # 2
#     [0, 1, 1, 1, 1, 1, 0],      # 3
#     [1, 1, 0, 1, 1, 1, 1],      # 4
#     [0, 1, 0, 1, 0, 0, 1],      # 5
#     [1, 1, 0, 1, 0, 1, 1]       # 6
#     #0  1  2  3  4  5  6
# ])

maze = np.array([
    [1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1]
])

directions = [
    (1, 0),  # Abajo - Down
    #(-1, 0), # Arriba - Up
    (0, 1),  # Derecha - Rigth
    (0, -1),  # Izquierda - Left
    (-1, 0)
    ]

checkpoints =[]
possible_directions = []

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
        # Verificar si la nueva posición está dentro de los límites
        if 0 <= new_y < maze.shape[0] and 0 <= new_x < maze.shape[1]:
            if maze[new_y, new_x] == 2:
                path.append((new_y, new_x))
                goal = True
                #if checkpoint len == 0: flag = True
                # if possible_directions == []:
                #     flag = True
                #     print("Completed")
                #     break
            
            if maze[new_y, new_x] == 1:
                # if checar si ya está en path
                possible_directions.append((new_y, new_x))

    for (y, x) in possible_directions:
            if (y, x) in visited:
                possible_directions.remove((y, x))  # Si ya visitó la casilla, eliminar esa como posible camino a tomar

    print(possible_directions)
    
    if len(possible_directions) == 1:

        p_y = possible_directions[0][0]
        p_x = possible_directions[0][1]

        try: 
            if path_1 == []: #Si existe y no está vacio
                path_1.append((p_y, p_x))
            else:
                path.append((p_y, p_x))
        except:
            pass
#        path.append((p_y, p_x))
        
        visited.append((p_y, p_x))
        
        possible_directions = []
        
        print(p_y, p_x, " ==1 ")


    elif len(possible_directions) > 1:

        visited.append((p_y, p_x))

        #checkpoints.append((p_y, p_x)) #guarda esa posicion para regresar despeus
        
        p_y = possible_directions[0][0]
        p_x = possible_directions[0][1]

       # possible_directions = []   ### CHECAR ESTO BIEN

        path_1 = []
        path_1.append((p_y, p_x))
        visited.append((p_y, p_x))
        print(p_y, p_x, " > 1 ")
    
    elif len(possible_directions) == 0:

        if goal == True and possible_directions == []:
            flag = True
            break

        #p_y = checkpoints[0][0]
        #p_x = checkpoints[0][1]
        
       # checkpoints.pop()
        print("xd: ", possible_directions)
        print(p_y,", " , p_x, " == 0 ")
        #regresar a checkpoint
        #eliminar checkpoint y path_1

        #if possible directions > 1, y,x append checkpoint, elegir una 
        # pass

imprimir_laberinto(i_y, i_x, maze, visited[1:])

print("Path: ", path)
print("Path 1: ", path_1)
print("visited: ", visited)
print("possible ", possible_directions)
#print("check: ", checkpoints)