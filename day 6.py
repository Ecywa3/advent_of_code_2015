lights = [[0 for _ in range(1000)] for _ in range(1000)]


def turn_on(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = 1


def turn_off(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = 0


def toggle(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = 1 - lights[x][y]


with open('6.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if parts[0] == 'turn':
            action = parts[1]
            x1, y1 = map(int, parts[2].split(','))
            x2, y2 = map(int, parts[4].split(','))
            if action == 'on':
                turn_on(x1, y1, x2, y2)
            elif action == 'off':
                turn_off(x1, y1, x2, y2)
        elif parts[0] == 'toggle':
            x1, y1 = map(int, parts[1].split(','))
            x2, y2 = map(int, parts[3].split(','))
            toggle(x1, y1, x2, y2)

lights_lit = sum(sum(row) for row in lights)

print(f" {lights_lit}")

lights = [[0 for _ in range(1000)] for _ in range(1000)]


def turn_on2(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] += 1


def turn_off2(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = max(0, lights[x][y] - 1)


def toggle2(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] += 2


with open('6.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if parts[0] == 'turn':
            action = parts[1]
            x1, y1 = map(int, parts[2].split(','))
            x2, y2 = map(int, parts[4].split(','))
            if action == 'on':
                turn_on2(x1, y1, x2, y2)
            elif action == 'off':
                turn_off2(x1, y1, x2, y2)
        elif parts[0] == 'toggle':
            x1, y1 = map(int, parts[1].split(','))
            x2, y2 = map(int, parts[3].split(','))
            toggle2(x1, y1, x2, y2)

total_brightness = sum(sum(row) for row in lights)

print(f"{total_brightness}")

