import heapq
import random

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


# Checks whether a puzzle can be solved at all.
# It counts how many pairs of tiles are in the "wrong order".
# If that number is even, the puzzle is solvable.
def is_solvable(state):
    tiles = [x for x in state if x != 0]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1
    return inversions % 2 == 0


# Estimates how far the puzzle is from the goal.
# For every tile it adds up how many rows and columns it must move
# to reach its correct place. The empty tile is ignored.
def manhattan(state):
    total = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = tile - 1
        total += abs(index // 3 - goal_index // 3) + abs(index % 3 - goal_index % 3)
    return total


# Finds all positions you can reach with one move.
# It looks for the empty tile and swaps it with each neighbor
# (up, down, left, right) that exists on the board.
def neighbors(state):
    result = []
    i = state.index(0)
    row, col = i // 3, i % 3
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            new = list(state)
            new[i], new[j] = new[j], new[i]
            result.append(tuple(new))
    return result


# Solves the puzzle using the A* search algorithm.
# It always explores the most promising position first
# (steps already made + estimated steps left).
# Returns the list of positions from start to goal, or None if unsolvable.
def solve(start):
    if not is_solvable(start):
        return None

    counter = 0
    frontier = [(manhattan(start), counter, 0, start)]
    parent = {start: None}
    best_g = {start: 0}

    while frontier:
        f, _, g, state = heapq.heappop(frontier)
        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]
        if g > best_g[state]:
            continue
        for nxt in neighbors(state):
            new_g = g + 1
            if nxt not in best_g or new_g < best_g[nxt]:
                best_g[nxt] = new_g
                parent[nxt] = state
                counter += 1
                heapq.heappush(frontier, (new_g + manhattan(nxt), counter, new_g, nxt))
    return None


# Prints the puzzle as a 3x3 grid.
# The empty tile is shown as an underscore.
def print_state(state):
    for r in range(3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[r * 3:r * 3 + 3]))
    print()


# Creates a random starting position.
# It shuffles the tiles and keeps trying until the result is solvable
# and is not already the finished puzzle.
def random_start():
    while True:
        tiles = list(range(9))
        random.shuffle(tiles)
        state = tuple(tiles)
        if state != GOAL and is_solvable(state):
            return state


if __name__ == "__main__":
    start = random_start()

    print("Initial state:")
    print_state(start)

    path = solve(start)
    if path is None:
        print("No solution exists.")
    else:
        print(f"Solution found in {len(path) - 1} moves:\n")
        for step, s in enumerate(path):
            print(f"Step {step}:")
            print_state(s)