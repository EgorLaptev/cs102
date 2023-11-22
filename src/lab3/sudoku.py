import pathlib
import threading, multiprocessing
import typing as tp
from functools import *
from random import randint, shuffle
import copy

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    matrix = [ [values[j+n*i] for j in range(n) ] for i in range(n)]

    return matrix


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    
    row = grid[pos[0]]

    return row


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """

    col = [ row[pos[1]] for row in grid ]

    return col


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """

    r,c = pos

    col = (c+3)//3-1
    row = (r+3)//3-1

    block = [ grid[i][j] for i in range(row*3, row*3+3) for j in range(col*3, col*3+3) ]

    return block


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    n = len(grid)
    positions = [[i, j] for i in range(n) for j in range(n) if grid[i][j] == '.']

    return tuple(positions[0]) if len(positions) else False


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """

    values = set()

    for n in '123456789':
        in_row = n in get_row(grid, pos)
        in_col = n in get_col(grid, pos)
        in_block = n in get_block(grid, pos)

        if not (in_row or in_col or in_block):
            values.add(n)

    return values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')gr
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    
    current_pos = find_empty_positions(grid)

    if not current_pos:
        return grid

    possible_values = list(find_possible_values(grid, current_pos))
    shuffle(possible_values)    

    for current_value in possible_values:
        row, col = current_pos
        grid[row][col] = current_value
        
        if solve(grid):
            return grid

        grid[row][col] = '.'

    
    return False


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False
    >>> grid = [ \
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'], \
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'], \
            ['1', '9', '8', '2', '4', '2', '5', '6', '7'], \
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'], \
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'], \
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'], \
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'], \
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'], \
            ['3', '4', '5', '2', '8', '6', '1', '7', '9'] \
        ]
    >>> check_solution(grid)
    False
    """

    n = len(solution)
    rows = [ [num for num in row if num != '.'] for row in solution ]
    cols = [ [num for num in get_col(solution, (0, col)) if num != '.'] for col in range(n) ]
    blocks = [ [num for num in get_block(solution, (row, col)) if num != '.'] for row in range(0, n, 3) for col in range(0, n, 3) ]
    
    uniq_rows = all([ len(row) == len(set(row)) for row in rows ])
    uniq_cols = all([ len(col) == len(set(col)) for col in cols ])
    uniq_blocks = all([ len(block) == len(set(block)) for block in blocks ])

    solved = all('.' not in row for row in solution)

    return uniq_rows and uniq_cols and uniq_blocks and solved


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    
    # >>> grid = generate_sudoku(1000)
    # >>> sum(1 for row in grid for e in row if e == '.')
    # 0
    # >>> solution = solve(grid)
    # >>> check_solution(solution)
    # True
    # >>> grid = generate_sudoku(0)
    # >>> sum(1 for row in grid for e in row if e == '.')
    # 81
    # >>> solution = solve(grid)
    # >>> check_solution(solution)
    # True

    N = min(N, 81)

    empty = [ ['.' for _ in range(9)] for row in range(9) ]
    grid = solve(copy.deepcopy(empty))
    nums = sum( row.count('.') for row in grid )

    while 81 - N> nums:
        row = randint(0, 8)
        col = randint(0, 8)
        grid[row][col] = '.'
        nums = sum( row.count('.') for row in grid )

    return grid


def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    solution = solve(grid)
    if not solution:
        print(f"Puzzle {filename} can't be solved")
    else:
        display(solution)
        if check_solution(solution):
            print('Solution is correct')
        else:
            print('Oops')

if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        p = multiprocessing.Process(target=run_solve, args=(filename,))
        p.start()



# if __name__ == "__main__":
#     for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
#         grid = read_sudoku(fname)
#         display(grid)
#         solution = solve(grid)
#         if not solution:
#             print(f"Puzzle {fname} can't be solved")
#         else:
#             display(solution)
#             if check_solution(solution):
#                 print('Solution is correct')
#             else:
#                 print('Oops')