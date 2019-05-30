import motors
def forward(time):
    motors.forward(time)
    return "f" + time
def backward(time):
    motors.backward(time)
    return "b" + time
def turn_left(time):
    motors.left(time)
    return "l" + time
def turn_right(time):
    motors.right(time)
    return "r" + time