# Maze Solver

A terminal-based maze solver that finds the path from Start (`S`) to End (`E`) using DFS or BFS algorithms, with visual output.

## Features

- Default pre-loaded maze
- Custom maze input (define rows with `S`, `E`, `0` for path, `1` for wall)
- Two solving algorithms: DFS (Depth-First Search) and BFS (Breadth-First Search)
- Visual maze display with path highlighted using `*`
- Step count for the found path

## Requirements

- Python 3.x

No external dependencies required.

## How to Run

```bash
python maze_solver.py
```

## Example Output

```
==================================================
         MAZE SOLVER (DFS/BFS)
==================================================

--- Choose Maze ---
1. Default maze
2. Enter custom maze
Choose: 1

Legend: S=Start, E=End, #=Wall, .=Path

Maze:
S . . # .
# . # # .
. . . # .
. # . . .
. # . # .
. . . . E

Start: (0, 0), End: (5, 4)

Choose algorithm: (1) DFS or (2) BFS: 2

Using BFS...

Maze:
* * * # .
# * # # .
. * * # .
. # * * *
. # . # *
. . . . *

Path found! Steps: 11
```