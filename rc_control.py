# Simulated RC Car Control

def move(direction):
    if direction == "forward":
        return "Car moving forward"
    elif direction == "backward":
        return "Car moving backward"
    elif direction == "left":
        return "Car turning left"
    elif direction == "right":
        return "Car turning right"
    else:
        return "Invalid command"

# Test
commands = ["forward", "left", "right", "backward"]

for cmd in commands:
    print(move(cmd))
