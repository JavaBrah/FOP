# Write a program that asks the user for a (integer) number of cents, 
# from 0 to 99, and outputs how many of each type of coin would represent
#  that amount with the fewest total number of coins.
#  When you run your program, it should match the following format:

# Please enter an amount in cents less than a dollar.
# 87
# Your change will be:
# Q: 3
# D: 1
# N: 0
# P: 2

# Hint: You may find the mod operator (%) useful.

# You may not use any loops.

demo_input = 21

def findExactChange(input):
    coinDict = {'Q': 25, 'D': 10, 'N': 5, 'P':1}
    changeDict = {'Q': 0, 'D': 0, 'N': 0, 'P':0}
    if input // coinDict["Q"]:
        changeDict['Q'] = input // coinDict['Q']
        input -= changeDict['Q'] * coinDict["Q"]
    if input // coinDict['D']:
        changeDict["D"]  = input // coinDict["D"]
        input -= changeDict['D'] * coinDict['D']
    if input // coinDict['D']:
        changeDict["N"]  = input // coinDict["N"]
        input -= changeDict['N'] * coinDict['N']
    if input // coinDict['P']:
        changeDict["P"]  = input // coinDict["P"]
        input -= changeDict['P'] * coinDict['P']
       

    print(changeDict)

findExactChange(demo_input)