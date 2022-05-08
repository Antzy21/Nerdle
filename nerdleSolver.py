from solvingHelpers import isSensible, isCorrect, produceVariations

func = "xxxxx"
mustUse = []
cantUse = []
positionalConditions = [
]

variations = produceVariations(mustUse, cantUse, func)
print(len(variations), "variations")
       
sensibleEquations = list(filter(isSensible, variations))
print(len(sensibleEquations), "sensible equations")

correctEquations = list(filter(isCorrect, sensibleEquations))
print(len(correctEquations), "correct equations")

print(correctEquations)        