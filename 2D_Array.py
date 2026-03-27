def matrix_experiment():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    for row in matrix: 
        print(row)

    print("\nRow Sums:")
    for i in range(len(matrix)):
        print(f"Row {i}: {sum(matrix[i])}")

    print("\nColumn Sums:")
    for col in range(len(matrix[0])):
        c_sum = sum(matrix[row][col] for row in range(len(matrix)))
        print(f"Column {col}: {c_sum}")

    target = 5
    found = False
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == target:
                print(f"\nSearch {target}: Found at ({r}, {c})")
                found = True
    if not found: print(f"\nSearch {target}: Not Found")

    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    print("\nTranspose:")
    for row in transpose: 
        print(row)

if __name__ == "__main__":
    matrix_experiment()