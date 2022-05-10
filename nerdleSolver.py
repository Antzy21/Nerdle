from solvingHelpers import isSensible, isCorrect, isValidWithPositionalConditions, produceVariations

func = "xxxxxxxx"
#Example [3,6,5,'+']
mustUse = [9,'*','-',7,5]
cantUse = [8,6]
#Example [(0, '9'), (7, '5')]
positionalConditions = [
    (0,9),
    (1,'*'),
    (4,'-'),
    (5,7),
    (7,5)
]

variations = produceVariations(mustUse, cantUse, func)
print(len(variations), "variations")
#print(variations[0:100])       

sensibleEquations = list(filter(isSensible, variations))
print(len(sensibleEquations), "sensible equations")
#print(sensibleEquations[0:100])       

def condFilter(func):
    return isValidWithPositionalConditions(func, positionalConditions)
filteredByPositionalConditions = list(filter(condFilter, sensibleEquations))
print(len(filteredByPositionalConditions), "conditionaly filtered equations")

correctEquations = list(filter(isCorrect, filteredByPositionalConditions))
print(len(correctEquations), "correct equations")
for e in correctEquations:
    print(e)