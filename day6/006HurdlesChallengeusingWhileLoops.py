# Hurdle 3

def turn_right():
    for i in range(0,3):
        turn_left()

def jump_over():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if  wall_in_front():
        jump_over()
    else:
        move()