# Kai Jameson
# Thursday @ 2pm

def int_to_reverse_binary(user_input):
    binary_val = ''
#write your while loop here
    while user_input > 0:
        binary_val = binary_val + str(user_input % 2)
        user_input = user_input // 2
        #write your code

    return binary_val


def string_reverse(binary_val): 
    reverse_input = ''
    for char in binary_val:
        reverse_input = char + reverse_input
   #write your for loop here
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_val = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_val))
    
    print(binary_string)