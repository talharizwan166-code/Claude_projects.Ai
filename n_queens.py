import matplotlib.pyplot as plt

def count_n_queens(n):
    """Count all solutions to the N-Queens problem."""
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False

        # Check diagonals
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def solve(board, row):
        if row == n:
            return 1

        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                count += solve(board, row + 1)
                board[row] = -1

        return count

    board = [-1] * n
    return solve(board, 0)


def plot_solutions(n_values, solution_counts):
    """Plot the number of solutions for different N values."""
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, solution_counts, marker='o', linewidth=2, markersize=8)
    plt.xlabel('Board Size (N)', fontsize=12)
    plt.ylabel('Number of Solutions', fontsize=12)
    plt.title('N-Queens Problem: Solutions vs Board Size', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('n_queens_graph.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    print("N-Queens Solution Counter")
    print("-" * 30)

    n_values = []
    solution_counts = []

    for n in range(1, 13):
        solutions = count_n_queens(n)
        print(f"N = {n:2d}: {solutions:6d} solutions")
        n_values.append(n)
        solution_counts.append(solutions)

    print("\nGenerating graph...")
    plot_solutions(n_values, solution_counts)
