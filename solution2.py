#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(numbers):
    product = 1
    for number in numbers:
        product = product * number
    return product
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7]
list3 = [3, 6, 10, 20]

print(mult_list(list1))
print(mult_list(list2))
print(mult_list(list3))




