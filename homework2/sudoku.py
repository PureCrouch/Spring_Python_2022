import pathlib
import typing as tp
import random


T = tp.TypeVar("T")

def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path('E:\pogr\homework02\puzzle1.txt')
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
    if len(values) % n != 0:
        return None
    return [values[i * n : (i + 1) * n] for i in range(n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    return grid[pos[0]]

def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    col = [''] * len(grid)
    for i in range(len(grid)):
        col[i] = grid[i][pos[1]]
    return col


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int])-> tp.List[str]:
    n = 3
    y = pos[0] // n
    x = pos[1] // n
    res = [''] * len(grid[0])
    for i in range(n):
        for j in range(n):
            res[i * n + j] = grid[y * n + i][x * n + j]
    return res

def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                return i, j


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    return set([str(i) for i in range(1,10)]) - (set(get_block(grid, pos) + get_row(grid, pos) + get_col(grid, pos)) - set(['.']))

from copy import deepcopy as cp

def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    pos = find_empty_positions(grid)
    if not pos:
        if not grid: return None
        return grid
    possible_values = list(find_possible_values(grid, pos))
    possible_values.sort()
    if len(possible_values) == 0: return None
    for i in range(len(possible_values)):
        grid_copy = cp(grid)
        grid_copy[pos[0]][pos[1]] = possible_values[i]
        solution = solve(grid_copy)
        if solution: return solution

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    if not solution: return False
    for i in range(3):
        for j in range(3):
            block = set(get_block(solution, (i*3, j*3)))
            if len(block) != 9 or '.' in block: return False

    for i in range(9):
        row = set(get_row(solution, (i, 0)))
        col = set(get_col(solution, (0, i)))
        if len(row) != 9 or '.' in row: return False
        if len(col) != 9 or '.' in col: return False

    return True