import sys
from functools import reduce
from solvingHelpers import isSensible, isCorrect, produceVariations

def getConstraints(attempt, func, cantUse, positionalConditions):
    print(f"\nEnter results for equation: {attempt}")
    print("--- Not used : 0 --- Used : 1 --- Used in place : 2 ---")
    for i, value in enumerate(attempt):
        if value != func[i]:
            state = input(f"\nResult for {value}: ")
            if state == "0":
                if value not in cantUse:
                    cantUse.append(value)
            elif state == "1":
                positionalConditions[i].append(value)
            elif state == "2":
                func = func[:i] + value + func[i+1:]
            print("func:", func, "--- cantUse:", cantUse, "--- posConds: ", positionalConditions)
    return func, cantUse, positionalConditions

def calculate(func, cantUse, positionalConditions):    
    variations = produceVariations(positionalConditions, cantUse, func)
    print(len(variations), "variations")     
    sensibleEquations = list(filter(isSensible, variations))
    print(len(sensibleEquations), "sensible equations")
    correctEquations = list(filter(isCorrect, sensibleEquations))
    print(len(correctEquations), "correct equations")
    return correctEquations
    

def initializeConstraints(equations: list):
    if equations == []:
        equations = ["9*8-7=65"]
    func = len(equations[0])*"x"
    cantUse = []
    positionalConditions = [[] for _ in equations[0]]
    defaultConstraints = (func, cantUse, positionalConditions)
    def reducer(constraints, equationB):
        func, cantUse, posConds = constraints
        return getConstraints(equationB, func, cantUse, posConds)
    return reduce(reducer, equations, defaultConstraints)
    
if len(sys.argv) == 1:
    equations = []
else:
    equations = sys.argv[1:]

func, cantUse, positionalConditions = initializeConstraints(equations)
    
possibleAnswers = []
    
while len(possibleAnswers) != 1:
    print("\nCalculating...\n")
    possibleAnswers = calculate(func, cantUse, positionalConditions)
    print(possibleAnswers)
    if len(possibleAnswers) < 10:
        break
    attempt = input("\nNext attempted equation: ")
    if attempt == "":
        break
    func, cantUse, positionalConditions = getConstraints(attempt, func, cantUse, positionalConditions)
    