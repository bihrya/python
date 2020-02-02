import os
import sys
import math_exercices as m

# Test parameters **********************************************
simpleAdditions=5                                              #
simpleSubstractions=0
simpleMultiplications=0
simpleDivisions=0
thousandsAdditions=0
thousandsSubstractions=0
# **************************************************************

def menuchoice():
    while True:
        try:
            exNumber = str(input('What is it going to be? '))
        except ValueError:
            print("Sorry, I did not understand... Again please.")
            continue
        else:
            break

    return exNumber.split(',')

def askQuestion(question, result):
    while True:
        try:
            exNumber = int(input(question))
        except ValueError:
            print("Sorry, I did not understand... Again please.")
            continue
        else:
            break
    if exNumber == result:
        return True
    else:
        return False

def displayMenu():
    print('Here are the activities you can do. You can choose multiple activities by typing each number after a comma (1,5,6)')
    print('{:^10}'.format('1') + ' Simple additions')
    print('{:^10}'.format('2') + ' Simple substractions')
    print()
    print('{:^10}'.format('3') + ' Additions without regrouping')
    print('{:^10}'.format('4') + ' Substraction without regrouping')
    print()
    print('{:^10}'.format('5') + ' Additions with regrouping')
    print('{:^10}'.format('6') + ' Substraction with regrouping')
    print()
    print('{:^10}'.format('7') + ' Time tables up to 12')
    print('{:^10}'.format('8') + ' Time table of your choice')

    print()

os.system('clear')
print('*' * 50)
print('*{:^48}*'.format('Let\'s do some maths'))
print('*' * 50)
print()
print('But first, what is your name?')
name = str(input("My name is "))
print()
print('Nice to see you {}'.format(name))
displayMenu()
choice = menuchoice()


for i in choice:
    print(i)

if '1' in choice:
    list = m.simpleAdditionsExercice(simpleAdditions)
    for question, result in list:
        if askQuestion(question, result):
            print('Good')

if '2' in choice:
    print(2)
if '3' in choice:
    print(3)
if '4' in choice:
    print(4)
if '5' in choice:
    print(5)
if '6' in choice:
    print(6)
if '7' in choice:
    print(6)
if '8' in choice:
    print(6)

print('Well done {}'.format(name))
displayMenu()
