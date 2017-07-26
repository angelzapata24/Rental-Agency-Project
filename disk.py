import core

def keep_history(tent_size, amount):
    message = '\n{}, ${:.2f}'.format(tent_size, amount)
    with open('history.txt', 'a') as file:
        file.write(message)

def in_history():
    left = []
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1].strip().replace('$', ''))])
    return left
