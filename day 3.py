def count_houses(inputs):
    visited_houses = set()
    x, y = 0, 0
    visited_houses.add((x, y))

    for direction in inputs:
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1

        visited_houses.add((x, y))

    return len(visited_houses)


def count_houses2(inputs):
    visited_houses = set()
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    visited_houses.add((santa_x, santa_y))

    is_santa_turn = True

    for direction in inputs:
        if is_santa_turn:
            if direction == '^':
                santa_y += 1
            elif direction == 'v':
                santa_y -= 1
            elif direction == '>':
                santa_x += 1
            elif direction == '<':
                santa_x -= 1
            visited_houses.add((santa_x, santa_y))
        else:
            if direction == '^':
                robo_y += 1
            elif direction == 'v':
                robo_y -= 1
            elif direction == '>':
                robo_x += 1
            elif direction == '<':
                robo_x -= 1
            visited_houses.add((robo_x, robo_y))

        is_santa_turn = not is_santa_turn

    return len(visited_houses)


with open('3.txt', 'r') as file:
    inputs = file.read()


print(count_houses(inputs))
print(count_houses2(inputs))

