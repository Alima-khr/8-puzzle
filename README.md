# 8-Puzzle Solver

A Python program that solves the 8-puzzle (3×3 sliding tiles) using the A* algorithm with the Manhattan distance heuristic. Each run generates a new random solvable starting position, and the program finds the shortest sequence of moves to the goal.

## The Problem

The board has tiles numbered 1–8 and one empty space. In one move, the empty space swaps with an adjacent tile. The goal is to reach this arrangement:

```
1 2 3
4 5 6
7 8 _
```

## Example Output

```
Initial state:
1 2 3
4 _ 6
7 5 8

Solution found in 2 moves:

Step 0:
1 2 3
4 _ 6
7 5 8

Step 1:
1 2 3
4 5 6
7 _ 8

Step 2:
1 2 3
4 5 6
7 8 _
```

## How It Works

- **State:** a tuple of 9 numbers, where `0` is the empty space.
- **Random start (`random_start`):** shuffles the tiles and keeps only positions that are solvable.
- **Solvability check (`is_solvable`):** a puzzle is solvable only if the number of inversions is even. Exactly half of all permutations are unsolvable.
- **Neighbors (`neighbors`):** all positions reachable with one move of the empty space.
- **Heuristic (`manhattan`):** the sum of Manhattan distances of all tiles from their goal positions. It is admissible because it never overestimates the real number of moves.
- **Search (`solve`):** A* picks the state with the lowest `f = g + h` from a priority queue, where `g` is the number of moves made and `h` is the heuristic estimate. The solution found has the minimum number of moves.
- **Output (`print_state`):** prints a state as a 3×3 grid.
