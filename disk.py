import core


def keep_history(tent_size, amount):
    message = '\n{}, ${:.2f}'.format(tent_size, amount)
    with open('history.txt', 'a') as file:
        file.write(message)


def in_history_revenue():
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    left = []
    for line in lines:
        split_string = line.split(', ')
        left.append(
            [split_string[0],
             float(split_string[1].strip().replace('$', ''))])
    return left


def in_inventory():
    left = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([(split_string[0]), (split_string[1]), (split_string[2])])
    return left


def take_away(tent1, amount):
    str_l = ['tent number:, cost:, amount of tents avalaible:']
    left = in_inventory()
    for item in left:
        if item[0] == tent1:
            if int(amount) > int(item[2]):
                return False
            else:
                item[2] = int(item[2]) - int(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file:
        file.write(message)
    return True


def refill(type_tent, how_many):
    str_l = ['tent number:, cost:, amount of tents avalaible:']
    left = in_inventory()
    for item in left:
        if item[0] == type_tent:
            item[2] = int(how_many) + int(item[2])
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file:
        file.write(message)
