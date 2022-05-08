from solvingHelpers import isSensible, isCorrect, produceVariations

func = "xxxxxx"
#Example [3,6,5,'+']
mustUse = []
cantUse = []
#Example [(0, '9'), (7, '5')]
positionalConditions = [
]

variations = produceVariations(mustUse, cantUse, func)
print(len(variations), "variations")
#print(variations[0:100])       

sensibleEquations = list(filter(isSensible, variations))
print(len(sensibleEquations), "sensible equations")
#print(sensibleEquations[0:100])       

correctEquations = list(filter(isCorrect, sensibleEquations))
print(len(correctEquations), "correct equations")
print(correctEquations)        