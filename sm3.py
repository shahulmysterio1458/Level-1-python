def sort_rows(matrix):
    for row in matrix:
        row_sum = sum(row)
        row.insert(0, row_sum)

    matrix.sort()
    for row in matrix:
        row.pop(0)

    return matrix

def display_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


matrix = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter the element at position ({i},{j}): "))
        row.append(element)
    matrix.append(row)


sorted_matrix = sort_rows(matrix)
display_matrix(sorted_matrix)
