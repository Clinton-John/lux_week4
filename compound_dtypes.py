'''
Compound data types are the data types in python that are made up of more than one elements. They are mostly used to store elements that are in one group. The most commonly used compound data types are 
1. List - is a collection of different elements that can be of any data type, and it can be manipulated once created.

2. Tuple -  it is the same as a list but the difference is that once it is created it cannot be changed at any point of the program. The elements can also be of different data types


3. Dictionaries - it is a data type that stores its information as key value pairs. The keys within a dictionary cannot be the same, but the values can be same and of different data types. The details of the dictionaries can be changed. To access the values, the key is called.
'''

# List example containing and integer, float, string and another list
client_information = [21, "Single", 20,000.50, [6,13]]
print("List Example")
print(client_information)
client_information.append("Data Engineer")
print("List after Appending new information")
print(client_information)
print(len(client_information)) # number of elements in the list


##  Tuple Example
client_information = (21, "Single", 20,000.50, [6,13])
print("Tuple Example")
print(client_information)
print(client_information[0])
print(len(client_information))


## Dictionary Examples

employee_information = {
    "Name": "John Doe",
    "Age": 21,
    "Occupation": "Software Engineer",
    "Salary": 20000.50,
    "Languages": ['Python', 'Go' 'Java']
}
print("Dictionary Example")
print(employee_information)
print(employee_information["Name"])
