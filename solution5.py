"""Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together."""

def pascal(numRows: int):
    triangle = [[1]]

    for i in range(numRows - 1):
        n = [0] + triangle[-1] + [0]
        row = []
        for x in range(len(triangle[-1]) + 1):
            row.append(n[x] + n[x + 1])
        triangle.append(row)
    return triangle


result = pascal(5)
for row in result:
    print(row)
