"""Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False."""

def num_within(x, a, b):
    return x in range(a, b+1)

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))
print(num_within(11, 3, 8))
print(num_within(12, 4, 14))


