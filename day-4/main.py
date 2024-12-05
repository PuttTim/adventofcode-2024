content = []

with open("sample.txt", "r") as file:
    for line in file:
        content.append(line.strip())

    print(content)


def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if all(
                    is_valid(r + dr * k, c + dc * k)
                    and grid[r + dr * k][c + dc * k] == word[k]
                    for k in word_length
                ):
                    count += 1

    return count


def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    valid_mas = {"MAS", "SAM"}

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(row, col, direction):
        path = []
        for step in range(3):
            r = row + step * direction[0]
            c = col + step * direction[1]
            if not is_valid(r, c):
                return None
            path.append(grid[r][c])
        return "".join(path)

    def is_xmas(center_row, center_col):
        left_diag = dfs(center_row - 1, center_col - 1, (1, 1))
        right_diag = dfs(center_row - 1, center_col + 1, (1, -1))
        return left_diag in valid_mas and right_diag in valid_mas

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A" and is_xmas(r, c):
                count += 1

    return count


grid = [list(row) for row in content]

result = count_xmas_patterns(grid)
print("Total occurrences of 'X-MAS':", result)

# print("count:", count_word_occurrences(content, "MAS"))
# print("count:", count_xmas_patterns_dfs(content))
