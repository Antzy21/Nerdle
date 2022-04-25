from solvingHelpers import produceVariations, isValidVariation

func = "xx/x-x=5"
mustUseNums = [3,6]
cantUseNums = [1,2,7,8,9]

variations = produceVariations(mustUseNums, cantUseNums, func)

validVariations = []
for variation in variations:
    if isValidVariation(variation):
        validVariations.append(variations)
        print(variation)
