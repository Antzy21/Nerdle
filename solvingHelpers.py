alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    't',
    'u',
    'x',
    'y',
    'z',
]

def addToArgs(args : list[int], i : int) -> tuple[int] :
    lst = list(*args)
    lst.append(i)
    return(tuple(lst))

def createResult(
    options : list[int],
    length: int,
    currentValue: int =0
    ) -> list[int]:
    variations = []
    for i in options:
        newValue = currentValue*10+i
        if length == 1:
            variations.append(newValue)
        else:            
            newoptions = options[:]
            newoptions.remove(i)
            variations.extend(createResult(newoptions, length-1, newValue))
    return variations
            
def findSolutions(mustUseNums, cantUseNums, strFunc, func, resultLength=1, *args):
    
    lenFuncParams = len(func.__code__.co_varnames)
    if lenFuncParams+resultLength == len(mustUseNums)+len(*args):
        options = mustUseNums
    else:
        options = list(filter(lambda x: x not in cantUseNums ,range(1,10)))
    
    if lenFuncParams == len(*args):
        result = func(*args[0])
        for i in createResult(options, resultLength):
            if result == i:
                print(strFunc(i,*args[0]))
    else:
        for i in options:
            newArgs = addToArgs(args, i)            
            
            newMustUseNums = mustUseNums[:]
            if i in newMustUseNums:
                newMustUseNums.remove(i)
            
            findSolutions(newMustUseNums, cantUseNums, strFunc, func, resultLength, newArgs)