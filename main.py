#https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs # some inspiration from here

#1 Guess The Number

def guessTheNumber():
    import random

    print('Guess a random number between 0 and 20:')

    while (True):
        i = random.randint(0, 20)
        x = int(input())
        if (i == x):
            break
        elif (i < x):
            print('number too high! please guess again')
        elif (i > x):
            print('number too low! please guess again')

    print('Congratulations you did it!')

#2 Rock, Paper, Scissors Game

def rockPaperScissors():
    import random

    while (True):
        print('rock.. paper.. scissors.. shoot!')

        signs = ['rock', 'paper', 'scissors']
        i = random.choice(signs)
        x = input()

        if (i == x):
            break

        print('I\'ve won. we go again!')

    print('Congratulations you did it!')

#3 Generating a sine vs cosine curve

def trigonometry():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(-2 * np.pi, 2 * np.pi, .1)  # start,stop,step
    y = np.sin(x)
    z = np.cos(x)

    # plots sin/cos for two periods with an amplitude of 1

    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()

#4 Function for inverting a string

def invert(s):
    n = len(s)
    r = ''
    for char in s:
        r += s[n-1]
        n -= 1
    print(r)

# 5 password generator

def generatePassword():
    from random import randint, choice, sample

    chars = int(input('Number of characters: '))
    nums = int(input('Number of numbers: '))
    symb = int(input('Number of symbols: '))

    length = chars + nums + symb # password length

    pwd = []

    # character identification based on ascii

    for i in range(chars):
        pwd += chr(choice([randint(65, 90), randint(97, 122)]))  # charUpper/charLower
    for i in range(nums):
        pwd += chr(randint(48, 58)) # numbers 0-9
    for i in range(symb):
        pwd += chr(choice([randint(33, 47), randint(58, 64), randint(91, 96), randint(123, 126)])) # various symbols

    return sample(pwd, len(pwd))

# pwd = ''.join(generatePassword()) # convert list to string
# print(pwd)

# 6 simple list sorting

def mySort(list):
    temp = list.copy() # function is a lot faster without cloning
    sortedList = []

    while True:
        if len(temp) == 0:
            return sortedList

        min = temp[0] # set initial smallest value
        index = 0
        found = False

        for i in temp:
            if i < min:
                min = i
                index = temp.index(i)
                found = True

        if found:
            temp.remove(temp[index])
        else:
            temp.remove(temp[0]) # first element was smallest

        sortedList.append(min)

# import timeit
#
# list = [9, 8, 7, 5, 6, 55, 5, 2, 9, 5, 33]
# print(mySort(list))
#
# list = [9, 8, 7, 5, 6, 55, 5, 2, 9, 5, 33]
# print(sorted(list))
#
# print(timeit.timeit(lambda: mySort(list)))
# print(timeit.timeit(lambda: sorted(list)))

# 7 fibonacci

def fibIterative(n):
    nums = [0, 1]
    for i in range(n-1):
        nums.append(nums[i] + nums[i+1])
    return nums

def fibRecursive(n, nums):
    if n < 1: # abort condition
        return nums
    nums.append(nums[-1] + nums[-2])
    return fibRecursive(n-1, nums)

# print(fibIterative(10))
# print(fibRecursive(10, [0,1]))
#
# import timeit
#
# def timeDif(n):
#     a = timeit.timeit(lambda: fibIterative(n))
#     b = timeit.timeit(lambda: fibRecursive(n, [0, 1]))
#     print(b - a)
#
# timeDif(100) # recursion is slower and the difference gets greater proportional to n

# binary search

from random import randint

def binSearch(n, list): # number between 0 and 100
    index = 0
    if index == 0:
        index = len(list)

    if len(list) < 2:
        return -1

    if list[len(list)//2] == n: # // integer division
        print('found')
        print(index) ################# implement show index
    index -= len(list)//2
    if binSearch(n, list[:len(list)//2]) != - 1:
        return binSearch(n, list[:len(list) // 2])
    else:
        return binSearch(n, list[len(list)//2:])

rnd = []

for i in range(5):
    rnd.append(i)

binSearch(4, rnd)
