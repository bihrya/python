import os
import sys
import math_exercices as m
import time

print("Start test")

wrong_answer = 0
correct_answer = 0
error = ()

# Test parameters **********************************************
simpleAdditions=5                                              #
simpleSubstractions=0
simpleMultiplications=0
simpleDivisions=0
thousandsAdditions=0
thousandsSubstractions=0
# **************************************************************

def ask(question):
    while True:
        try:
            user_input = int(input(question))
        except ValueError:
            print("Sorry, I did not understand... Again please.")
            continue
        else:
            break
    return user_input

os.system('clear')

input("Press enter when you are ready to start")
start_time = time.time()

#Simple additions
for i in range(simpleAdditions):
    s= time.time()
    res = m.simpleAddition(10,10)
    if not ask("The result is ") == res[1]:
        error = error + (res,)
        print("Not correct: {}".format(res[1]))
        wrong_answer=wrong_answer+1
    else:
        #print("good in {} seconds".format(round(time.time()-s,2)))
        correct_answer = correct_answer + 1
duration = time.time() - start_time

input("Press enter when you are ready to continue")
os.system('clear')

# Simple substractions$
for i in range(simpleSubstractions):
    s= time.time()
    res = m.simpleSubstraction(10,10)
    if not ask("The result is ") == res:
        print("Not correct: {}".format(res))
        wrong_answer=wrong_answer+1
    else:
        #print("good in {} seconds".format(round(time.time()-s,2)))
        correct_answer = correct_answer + 1
duration = time.time() - start_time

input("Press enter when you are ready to continue")
os.system('clear')

# Simple Multiplications
for i in range(simpleMultiplications):
    s= time.time()
    res = m.simpleMultiplication(12,12)
    if not ask("The result is ") == res[1]:
        print("Not correct: {}".format(res[1]))
        wrong_answer=wrong_answer+1
    else:
        #print("good in {} seconds".format(round(time.time()-s,2)))
        correct_answer = correct_answer + 1
duration = time.time() - start_time

input("Press enter when you are ready to continue")
os.system('clear')

# Simple divisions
for i in range(simpleDivisions):
    s= time.time()
    res = m.simpleDivision(12,12)
    if not ask("The result is ") == res[1]:
        print("Not correct: {}".format(res[1]))
        wrong_answer=wrong_answer+1
    else:
        #print("good in {} seconds".format(round(time.time()-s,2)))
        correct_answer = correct_answer + 1
duration = time.time() - start_time

input("Press enter when you are ready to continue")
os.system('clear')

# Additions thousands
for i in range(thousandsAdditions):
    s= time.time()
    res = m.thousandsAddition(999,999)
    if not ask("The result is ") == res:
        print("Not correct: {}".format(res))
        wrong_answer=wrong_answer+1
    else:
        #print("good in {} seconds".format(round(time.time()-s,2)))
        correct_answer = correct_answer + 1
duration = time.time() - start_time

# Substraction thousands
for i in range(thousandsSubstractions):
    s= time.time()
    res = m.thousandsSubstraction(1000,100)
    if not ask("The result is ") == res:
        print("Not correct: {}".format(res))
        wrong_answer=wrong_answer+1
    else:
        #print("good in {} seconds".format(round(time.time()-s,2)))
        correct_answer = correct_answer + 1
duration = time.time() - start_time

print("")
print("*******************************************")
print("{} correct answers".format(correct_answer))
print("{} wrong answers".format(wrong_answer))
print("Finished in {} seconds".format(round(duration)))
print("*******************************************")
print("")

for i in range(len(error)):
    print("{}: {}".format(i,error[i]))
