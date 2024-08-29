'''
 list comprehension allows for creating a new list in a simple way , based on items that are already available in a single list, or randomly generated.
 It takes the element from the specified range and does some mathematical calculations or expressions with it to make it work
'''
#EXAMPLE 1
list1 = [23,76,43,87,98,54,32]
double_numbers = [value*2 for value in list1]
print(double_numbers)

#EXAXMPLE 2 -- adding all the nnumbers divisible by 3 in a list
divisible_numbers = [x for x in range(1, 100) if x % 3 == 0]
print(divisible_numbers)

# to show the number of elements in the list we use the len()
print(len(divisible_numbers))


# EXAMPLE 3 -- Creating a list of tuples that has numbers and their squares
numbers_tuple = [(num, num**2) for num in range(1,10)]
print(numbers_tuple)

