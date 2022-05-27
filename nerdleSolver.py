from solvingHelpers import isSensible, isCorrect, isValidWithPositionalConditions, produceVariations

func = "xxxxx=x3"
#Example [3,6,5,'+']
cantUse = [9,7,3,1,6]
#Example [(0, '9'), (7, '5')]
positionalConditions = [
    (),#1
    (),#2
    (),#3
    (),#4
    (),#5
    (),#6
    (),#7
    (),#8
]

variations = produceVariations(positionalConditions, cantUse, func)
print(len(variations), "variations")
#print(variations[0:100])       

sensibleEquations = list(filter(isSensible, variations))
print(len(sensibleEquations), "sensible equations")
#print(sensibleEquations[0:100])

correctEquations = list(filter(isCorrect, sensibleEquations))
print(len(correctEquations), "correct equations")
for e in correctEquations:
    print(e)