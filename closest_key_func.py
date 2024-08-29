'''
Given a dictionary with keys as letters and values as lists of letters, write a function closest_key to find the key with the input value closest to the beginning of the list.

'''

def closest_key(data_dict, target_value):
    closest_key = None
    min_index = float('inf')  # Initialize to infinity to ensure any valid index is smaller
    
    for key, values in data_dict.items():
        if target_value in values:
            index = values.index(target_value)
            if index < min_index:
                min_index = index
                closest_key = key
    
    return closest_key

# Example usage:
def main():
    foods = {
        'fruits': ['apple', 'banana', 'cherry', 'date'],
        'vegetables': ['carrot', 'broccoli', 'apple', 'cabbage'],
        'desserts': ['cake', 'apple', 'pie', 'ice cream']
    }

    result = closest_key(foods, 'apple')
    print(result)


if __name__ == '__main__':
    main()
