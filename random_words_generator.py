import random

def initialiseGrid():
    grid = {}
    grid['Hello'] = 'Здрасти'
    grid['Alex'] = 'Алекс'
    grid['Nora'] = 'Нора'
    grid['Claudia'] = 'Клаудия'
    grid['Tinka'] = 'Тинка'
    return grid

def shuffleKeys(grid):
    keysRow = {}
    i = 1
    for key, value in grid.items():
        keysRow[i] = key
        i = i +1
    keys =  list(keysRow.keys())
    random.shuffle(keys)
    d_shuffled = {}
    for key in keys:
     d_shuffled[key] = keysRow[key]
    print(d_shuffled)
    return d_shuffled

def shuffleValues(grid):
    keysValues = {}
    i = 1
    for key, value in grid.items():
        keysValues[i] = value
        i = i+ 1
    keys =  list(keysValues.keys())
    random.shuffle(keys)
    d_shuffled = {}
    for key in keys:
     d_shuffled[key] = keysValues[key]
    print(d_shuffled)
    return d_shuffled