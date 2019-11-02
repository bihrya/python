import os
import sys
import random

def simpleAddition(limit1=20, limit2=20):
    one = random.randint(1,limit1)
    two = random.randint(1,limit2)
    result = one + two
    question = ("{} + {} = ".format(one, two))
    print(question)
    return result

def simpleSubstraction(limit1=20, limit2=20):
    one = random.randint(1,limit1)
    two = random.randint(1,limit2)
    result = max(one,two) - min(one,two)
    question = ("{} - {} = ".format(max(one,two), min(one,two)))
    print(question)
    return result

def simpleMultiplication(limit1=12, limit2=12):
    one = random.randint(1,limit1)
    two = random.randint(1,limit2)
    result = one*two
    question = ("{} x {} = ".format(one, two))
    print(question)
    return result

print(simpleAddition(10,10))
print(simpleSubstraction(20,20))
print(simpleMultiplication())
