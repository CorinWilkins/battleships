import pytest
def build_probabilities_destroyers(grid):
    width = len(grid)
    height = len(grid[0])
    result = [[0]*width for i in range(height)]
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] != 'X':
                if get(grid, x + 1,y) != 'X':
                    result[x][y] += 1
                    result[x+1][y] += 1
                if get(grid, x, y + 1) != 'X':
                    result[x][y] += 1
                    result[x][y+1] += 1
            else:
                result[x][y] = 0
    return result
                
def get(grid, x, y):
    try:
        return grid[x][y]
    except IndexError as e:
        return 'X'

def test_destroyers():
    length = 5
    grid = [[' ']*length for i in range(length)]

    result = build_probabilities_destroyers(grid)
    
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
    result = build_probabilities_destroyers(grid)
    print(result)
    assert result == [
        [0,2,3,3,2],
        [2,4,4,4,3],
        [3,4,4,4,3],
        [3,4,4,4,3],
        [2,3,3,3,2]
    ]