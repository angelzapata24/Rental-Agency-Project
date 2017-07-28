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
 
def in_inventory():
    left = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([(split_string[0]), (split_string[1])])
    return left

def take_away(tent, size):
    str_l = ['tent, size']
    left = in_inventory()
    for item in left:
        if item == tent:
            if float(amount) > float(item[1]):
                return False
            else:
                item[1] = float(item[1]) - float(amount)
        item[0] = str(item[0])
        item[1] = str(item[1])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file: 
        file.write(message)
    return True