# N-Queens Solution Counter - Summary

## Overview
A Python implementation that counts all possible solutions to the N-Queens problem for different board sizes and visualizes the results with a graph.

## File
- **n_queens.py** - Solution counter with matplotlib visualization

## Features
1. **Solution Counting** - Counts all valid N-Queens solutions for boards size 1-12
2. **Console Output** - Displays solution count for each board size
3. **Graph Visualization** - Plots solutions vs board size with logarithmic scale
4. **High-Quality Export** - Saves graph as PNG at 300 DPI

## Algorithm

### Backtracking Approach
```
count_n_queens(n):
  - Uses recursive backtracking to count all solutions
  - Board represented as 1D array (board[row] = column)
  - Places queens row by row
  - Backtracks when no safe position exists
```

### Safety Check (is_safe)
A position is safe if:
- No queen in the same column
- No queen on the same diagonal (both directions)

### Time Complexity
O(N!) - explores all possible queen placements

## Results

| Board Size (N) | Solutions |
|----------------|-----------|
| 1              | 1         |
| 2              | 0         |
| 3              | 0         |
| 4              | 2         |
| 5              | 10        |
| 6              | 4         |
| 7              | 40        |
| 8              | 92        |
| 9              | 352       |
| 10             | 724       |
| 11             | 2,680     |
| 12             | 14,200    |

## Visualization
- **Graph Type**: Line plot with markers
- **X-axis**: Board size (N)
- **Y-axis**: Number of solutions (logarithmic scale)
- **Output**: `n_queens_graph.png`
- **Shows**: Exponential growth pattern of solutions

## Technical Details
- **Language**: Python 3
- **Dependencies**: matplotlib
- **Board Representation**: 1D array where index = row, value = column
- **Conflict Detection**: O(N) per placement check

## How to Run
```bash
python n_queens.py
```

## Output
1. Console prints solution count for N=1 to N=12
2. Displays matplotlib graph window
3. Saves graph as `n_queens_graph.png`

## Key Concepts
- Backtracking algorithm
- Constraint satisfaction problem
- Recursive problem solving
- Data visualization
- Logarithmic scaling for exponential data

---
*Created: 2026-04-09*
