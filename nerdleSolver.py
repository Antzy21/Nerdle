from solvingHelpers import produceVariations, isValidVariation

func = "xx-xx=xx"
mustUse = [1,5,7,8,9]
cantUse = [2,6]

variations = produceVariations(mustUse, cantUse, func)

positionalConditions = [
    (0, "9"),
    (0, "7"),
    (1, "9"),
    (4, "7"),
    (4, "8"),
    (7, "5"),
    (7, "1"),
]

validVariations = []
for variation in variations:
    if isValidVariation(variation, positionalConditions):
        validVariations.append(variations)
        print(variation)            
        