import motors
def forward(time):
    motors.forward(float(time))
    return "f" + time
def backward(time):
    motors.backward(float(time))
    return "b" + time
def turn_left(time):
    motors.left(float(time))
    return "l" + time
def turn_right(time):
    motors.right(float(time))
    return "r" + time
