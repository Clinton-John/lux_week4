## Creating a bigram. 
# 
# A bigram is a sequence of two adjacent elements from a string or list of tokens. For example, if we have the , "

def create_bigrams(user_input):
    # Clean the input string by removing leading/trailing spaces
    user_input_string = user_input.strip()
    
    # Create a list of bigrams
    bigrams = [user_input_string[i:i+2] for i in range(len(user_input_string) - 1)]
    
    return bigrams


def main():
    trials_string = input("Enter a string: ")
    bigrams_list = create_bigrams(trials_string)
    print(bigrams_list)

if __name__ == '__main__':
    main()

# # Example 
# Enter a string: consistency
# ['co', 'on', 'ns', 'si', 'is', 'st', 'te', 'en', 'nc', 'cy']





