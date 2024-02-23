def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def find_final_floor(directions):
    current_floor = 0
    for char in directions:
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1
    return current_floor


def find_basement_position(directions):
    current_floor = 0
    for idx, char in enumerate(directions, start=1):
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1
        if current_floor == -1:
            return idx
    return None


inputs = file_read('1.txt')

print(find_final_floor(inputs))
print(find_basement_position(inputs))
