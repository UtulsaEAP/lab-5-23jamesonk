# Kai Jameson
# Thursday @ 2pm

def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   rearrange = str(user_val2) + ' ' + str(user_val1) + ' ' + str(user_val4) + ' ' + str(user_val3)
   return rearrange

if __name__ == '__main__':   
   user_val1 = int(input())
   user_val2 = int(input())
   user_val3 = int(input())
   user_val4 = int(input())

   print(swap_values(user_val1, user_val2, user_val3, user_val4))
   #store output for every input here
   #print those output

 