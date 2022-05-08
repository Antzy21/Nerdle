from solvingHelpers import isSensible, isCorrect, produceVariations

func = "xxxxx"
mustUse = []
cantUse = []

variations = produceVariations(mustUse, cantUse, func)

positionalConditions = [
]
       
sensibleEquations = list(filter(isSensible, variations))
correctEquations = list(filter(isCorrect, sensibleEquations))

print(correctEquations)        