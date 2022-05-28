from solvingHelpers import isSensible, isCorrect, produceVariations
import sys

if len(sys.argv) == 2:
    triedEquation = sys.argv[1]
else:
    triedEquation = "9*8-7=65"

func = len(triedEquation)*"x"
cantUse = []
positionalConditions = [[] for _ in triedEquation]

def getResults(triedEquation, func, cantUse, positionalConditions):
    print(f"\nEnter results for equation: {triedEquation}")
    print("--- Not used : 0 --- Used : 1 --- Used in place : 2 ---")
    for i, value in enumerate(triedEquation):
        state = input(f"\nResult for {value}: ")
        if state == "0":
            cantUse.append(value)
        elif state == "1":
            positionalConditions[i].append(value)
        elif state == "2":
            func = func[:i] + value + func[i+1:]
        print("func: ", func)
        print("cantUse: ", cantUse)
        print("posConds: ", positionalConditions)
    return func, cantUse, positionalConditions

def calculate(func, cantUse, positionalConditions):    
    variations = produceVariations(positionalConditions, cantUse, func)
    print(len(variations), "variations")     
    sensibleEquations = list(filter(isSensible, variations))
    print(len(sensibleEquations), "sensible equations")
    correctEquations = list(filter(isCorrect, sensibleEquations))
    print(len(correctEquations), "correct equations")
    return correctEquations
    
while triedEquation != "":
    func, cantUse, positionalConditions = getResults(triedEquation, func, cantUse, positionalConditions)
    print("\nCalculating...\n")
    possibleAnswers = calculate(func, cantUse, positionalConditions)
    print(possibleAnswers)
    if len(possibleAnswers) < 10:
        break
    triedEquation = input("\nNext tried equation: ")
    