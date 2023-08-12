#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    if a >= b and a >= c:
        return a 
    elif b >= a and b >= c:
        return b
    else:
        return c 

print(max_num(1, 2, 3))
print(max_num(10, 15, 20))
print(max_num(25, 75, 50))



