def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


while at_goal() != True:
    if front_is_clear():
        if right_is_clear():
            turn_right()
        move()
    elif right_is_clear():
        turn_right()
        move()
    #   elif not right_is_clear():
    #       turn_left()
    else:
        turn_left()



