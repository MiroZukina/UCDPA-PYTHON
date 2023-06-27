def sumColumn(m, columnIndex):
    total = 0
    for row in m:
        total += row[columnIndex]
    return total

def test_sum_column():
    matrix = []
    print("Enter a 3-by-4 matrix:")

    for i in range(3):
        row = input("Enter a 3-by-4 matrix row {} : ".format(i)).split()
        row = [float(num) for num in row]
        matrix.append(row)

    for i in range(4):
        column_sum = sumColumn(matrix, i)
        print("Sum of elements at column", i, "is", column_sum)

# Testing the function
test_sum_column()
