'''
A Python program that checks if a given string is a palindrome
A Palindrome string is one that can be read from both sides and still be the same. For example "madam" can be read from both sides.
A stack data structure is a linear data structure that follows the concept of Last In First Out order. The first element to be added to the data structure will be the last element to be brough out. This program will check if a user input  is a palindrome using stack data structure and give the output to the user.
'''

# Takes user input, checks if palindrome using a stack and returns the output to the user
def check_if_palindrome(user_input):

    #convert the string to all lower case
    user_input = user_input.lower()
    stack = []

    # using a list to construct the stack
    for charachter in user_input:
        stack.append(charachter)

    #getting the strings from the list to form a reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    if user_input == reversed_string:
        print(f"{user_input} is a Palindrome")
    else:
        print(f"{user_input} is not a Palindrome")

    

## The main function
def main():
    user_input = input("Please enter a string: ")
    check_if_palindrome(user_input)

if __name__ == '__main__':
    main()



