def build_probabilities(grid, ships):
    width = len(grid)
    height = len(grid[0])
    result = [[0]*width for i in range(height)]
    for ship_length in ships:
        for x in range(len(grid)):
            for y in range(len(grid)):
                # if get(grid, x,y) == 'X':
                #     result[x][y] = 0
                # else: 
                    if check_row(grid, x,y, ship_length):
                        mark_row(result, x, y, ship_length)
                    if check_column(grid, x,y, ship_length):
                        mark_column(result, x, y, ship_length)
            
            
                
    return result

def check_row(grid, x,y, ship_length):
    for i in range(ship_length):
        if get(grid, x + i,y) == 'X':
            return False
    return True
            

def mark_row(result, x, y, ship_length):
    for i in range(ship_length):
        result[x+i][y] += 1


def check_column(grid, x,y, ship_length):
    for i in range(ship_length):
        if get(grid, x,y + i) == 'X':
            return False
    return True
            

def mark_column(result, x, y, ship_length):
    for i in range(ship_length):
        result[x][y+i] += 1
    pass

           
def get(grid, x, y):
    try:
        return grid[x][y]
    except IndexError as e:
        return 'X'


def test_destroyers():
    length = 5
    grid = [[' ']*length for i in range(length)]

    result = build_probabilities(grid, [2])
    
    assert result == [
        [2,3,3,3,2],
        [3,4,4,4,3],
        [3,4,4,4,3],
        [3,4,4,4,3],
        [2,3,3,3,2]
    ]


def test_destroyers_hit_at_0_0():
    length = 5
    grid = [[0]*length for i in range(length)]
    grid[0][0] = "X"
    result = build_probabilities(grid, [2])
    print(result)
    assert result == [
        [0,2,3,3,2],
        [2,4,4,4,3],
        [3,4,4,4,3],
        [3,4,4,4,3],
        [2,3,3,3,2]
    ]


def test_destroyers_hit_at_4_4():
    length = 5
    grid = [[0]*length for i in range(length)]
    grid[4][4] = "X"
    result = build_probabilities(grid, [2])
    print(result)
    assert result == [
        [2,3,3,3,2],
        [3,4,4,4,3],
        [3,4,4,4,3],
        [3,4,4,4,2],
        [2,3,3,2,0]
    ]


def test_2_destroyers():
    length = 5
    grid = [[0]*length for i in range(length)]
    grid[4][4] = "X"
    result = build_probabilities(grid, [2,2])
    print(result)
    assert result == [
        [4,6,6,6,4],
        [6,8,8,8,6],
        [6,8,8,8,6],
        [6,8,8,8,4],
        [4,6,6,4,0]
    ]
