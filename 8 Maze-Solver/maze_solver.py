default_maze = [
    ['S', 0, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 'E']
]

maze = None


def create_custom_maze():
    print("\n--- Create Custom Maze ---")
    print("Enter maze dimensions and rows")
    print("Use: S=Start, E=End, 0=Path, 1=Wall")
    print("Example row: S0100E")
    
    try:
        rows = int(input("Enter number of rows: ").strip())
        cols = int(input("Enter number of columns: ").strip())
    except ValueError:
        print("Invalid dimensions")
        return None
    
    grid = []
    for r in range(rows):
        while True:
            row_input = input(f"Row {r+1}: ").strip()
            if len(row_input) == cols:
                break
            print(f"Row must be {cols} characters long")
        
        grid_row = []
        for char in row_input:
            if char == 'S':
                grid_row.append('S')
            elif char == 'E':
                grid_row.append('E')
            elif char in '01':
                grid_row.append(int(char))
            else:
                grid_row.append(0)
        grid.append(grid_row)
    
    start, end = find_start_end(grid)
    if not start or not end:
        print("Error: Maze must have exactly one S and one E")
        return None
    
    return grid


def choose_maze():
    global maze
    print("\n--- Choose Maze ---")
    print("1. Default maze")
    print("2. Enter custom maze")
    
    choice = input("Choose: ").strip()
    
    if choice == "1":
        maze = [row[:] for row in default_maze]
    elif choice == "2":
        maze = create_custom_maze()
    else:
        maze = [row[:] for row in default_maze]


def print_maze(grid, path=None):
    print("\nMaze:")
    for r, row in enumerate(grid):
        line = ""
        for c, cell in enumerate(row):
            if path and (r, c) in path:
                line += "* "
            elif cell == 'S':
                line += "S "
            elif cell == 'E':
                line += "E "
            elif cell == 1:
                line += "# "
            else:
                line += ". "
        print(line)
    print()


def find_start_end(grid):
    rows = len(grid)
    cols = len(grid[0])
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    return start, end


def get_neighbors(pos, rows, cols, grid):
    r, c = pos
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] != 1:
                neighbors.append((nr, nc))

    return neighbors


def dfs(start, end, grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    stack = [start]
    parent = {}

    while stack:
        current = stack.pop()

        if current == end:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current, rows, cols, grid):
            if neighbor not in visited:
                parent[neighbor] = current
                stack.append(neighbor)

    return None


def bfs(start, end, grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    queue = [start]
    parent = {}
    visited.add(start)

    while queue:
        current = queue.pop(0)

        if current == end:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current, rows, cols, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None


def main():
    global maze
    
    print("=" * 50)
    print("         MAZE SOLVER (DFS/BFS)")
    print("=" * 50)
    
    choose_maze()
    
    if not maze:
        print("No maze loaded")
        return
    
    print("\nLegend: S=Start, E=End, #=Wall, .=Path")
    print_maze(maze)

    start, end = find_start_end(maze)
    
    if not start or not end:
        print("Error: Maze must have S (start) and E (end)")
        return
    print(f"Start: {start}, End: {end}")

    choice = input("\nChoose algorithm: (1) DFS or (2) BFS: ").strip()

    if choice == "1":
        print("\nUsing DFS...")
        path = dfs(start, end, maze)
    else:
        print("\nUsing BFS...")
        path = bfs(start, end, maze)

    if path:
        path_set = set(path)
        print_maze(maze, path_set)
        print(f"Path found! Steps: {len(path) - 1}")
    else:
        print("No path exists")


if __name__ == "__main__":
    main()