
import random
import logging


def simpleAddition(limit1=20, limit2=20):

    one = random.randint(1,limit1)
    two = random.randint(1,limit2)
    result = one + two
    question = ("{} + {} = ".format(one, two))
    #print(question)
    return (question, result)

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

def simpleDivision(limit1=12, limit2=12):
    one = random.randint(1,limit1)
    two = random.randint(1,limit2)
    result = one * two
    question = ("{} / {} = ".format(result, one))
    print(question)
    return two

def thousandsAddition(limit1, limit2):
    result = 0
    while result == 0 or result > 1000000:
        one = random.randint(1,limit1) * 1000
        two = random.randint(1,limit2) * 1000
        result = one + two

    print("{} + {} = ".format(one, two))
    return result

def thousandsSubstraction(limit1, limit2):
    one = random.randint(1,limit1) * 1000
    two = random.randint(1,limit2) * 1000
    result = max(one,two) - min(one,two)

    print("{} - {} = ".format(max(one,two), min(one,two)))
    return result

def simpleAdditionsExercice(questionsNumber=20):
    #logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    #logging.debug('This is a low-level debug message.')
    questions = []
    for i in range(questionsNumber):
        questions.append(simpleAddition())
    return questions
