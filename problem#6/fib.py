# Kai Jameson
# Thursday @ 2pm

def fibonacci(start_num):
    #write your code here
    secondNum = 1
    firstNum = 0
    nthNum = 0
    if start_num == 1:
        nthNum = firstNum
    elif start_num == 2:
        nthNum = secondNum
    else: 
        for i in range(2, start_num + 1):
            nthNum = secondNum + firstNum
            firstNum = secondNum
            secondNum = nthNum
    return nthNum


if __name__ == '__main__':
    start_num = int(input())
    print('fibonacci(' + str(start_num) + ') is ' + str(fibonacci(start_num)))