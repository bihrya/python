import os
import sys
import math_exercices as m

print("Start test")

def ask(question, result):
    while True:
        try:
            user_input = int(input(question[0]))
        except ValueError:
            print("Sorry, I did not understand... Again please.")
            continue
        else:
            break

        if user_input==result:
            print("Correct")
        else:
            print("The correct answer is {}".format(question[1]))


for i in range(10):
    res = m.simpleAddition(10,10)
    res = m.simpleSubstraction(10,10)


for i in range(5):
    res = m.simpleAddition(50,50)
    res = m.simpleSubstraction(50,50)
