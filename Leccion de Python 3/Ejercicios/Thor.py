initial_tx = int(input('X Inicial: ' ))
initial_ty = int(input('Y Inicial: ' ))
light_x = int(input('X Final: ' ))
light_y = int(input('Y Final: ' ))
thor_x, thor_y = initial_tx, initial_ty

while True:

    direction_x = ""
    direction_y = ""

    if thor_x > light_x:
        direction_x = "W"
        thor_x -= 1
    elif thor_x < light_x:
        direction_x = "E"
        thor_x += 1
    elif thor_y > light_y:
        direction_y = "N"
        thor_y -= 1
    elif thor_y < light_y:
        direction_y = "S"
        thor_y += 1
    print(direction_y + direction_x)