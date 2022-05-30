from functools import *
from equationChecks import *
from numpy import number

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
            
def findSolutions(mustUse, cantUse, strFunc, func, resultLength=1, *args):
    
    # Error handling:
    for numList in [mustUse, cantUse]:
        for n in numList:
            if not 0<n<10:
                print("Error: number lists invalid")
                return
    
    lenFuncParams = len(func.__code__.co_varnames)
    if lenFuncParams+resultLength == len(mustUse)+len(*args):
        options = mustUse
    else:
        options = list(filter(lambda x: x not in cantUse, range(0,10)))
    
    if lenFuncParams == len(*args):
        result = func(*args[0])
        for i in createResult(options, resultLength):
            if result == i:
                print(strFunc(i,*args[0]))
    else:
        for i in options:
            newArgs = addToArgs(args, i)            
            
            newMustUse = mustUse[:]
            if i in newMustUse:
                newMustUse.remove(i)
            
            findSolutions(newMustUse, cantUse, strFunc, func, resultLength, newArgs)
            
allOptions = []
numberOptions = list(range(0,10))
allOptions.extend(numberOptions)
strNumberOptions = [str(i) for i in numberOptions]
allOptions.extend(strNumberOptions)
operations = ["+","-","*","/","="]
allOptions.extend(operations)

def optionMustBeOperation(func: str):
    idx = func.find('x')
    try:
        precedingValue = int(func[idx-1])
        # If previous value was 0, must be an operation to avoid leading zero
        if precedingValue == 0:
            return True
    except:
        pass
    return False

def optionMustBeNum(func: str):
    idx = func.find('x')
    # Nums must be at start and end of equation
    if idx == 0 or idx == len(func):
        return True
    # If equals sign present, rhs must be a value made of numbers
    if '=' in func and func.find('=') < idx:
        return True
    try:
        # Number must preced a zero so it doesn't become a leading zero
        if int(func[idx+1]) == 0:
            return True
    except:
        pass
    return False
    
def getMustUse(positionalConditions: list[tuple], func: str) -> list[int]:
    def reduceFunc(a, b):
        a.extend(list(b))
        return a
    mustUseNums = reduce(reduceFunc, positionalConditions, [])
    return list(set(filter(lambda x: str(x) not in func, mustUseNums)))

def getCantUse(cantUse, cantUseInThisPosition):
    allCantUse = []
    for x in cantUse:
        try:
            num = int(x)
            allCantUse.append(num)
        except:
            pass
        allCantUse.append(x)
    allCantUse.extend(cantUseInThisPosition)
    return allCantUse

def getOptions(positionalConditions: list[tuple], cantUse: list[int], numSlots, func: str) -> list:
    xPos = func.find('x')
    cantUseInThisPosition = positionalConditions[xPos]
    if '=' not in func and xPos == len(func)-2:
        return ['=']
    options = allOptions
    mustUse = getMustUse(positionalConditions, func)
    if numSlots == len(mustUse):
        options = mustUse
    if optionMustBeNum(func):
        options = list(filter(lambda x: x in numberOptions or x in strNumberOptions, options))
    elif optionMustBeOperation(func):
        options = list(filter(lambda x: x in operations, options))
    options = list(filter(lambda x: x not in getCantUse(cantUse, cantUseInThisPosition), options))
    return options

def produceVariations(positionalConditions: list[tuple], cantUse: list[int], func: str) -> list[str]:

    numSlots = len(list(filter(lambda c: c == 'x', func)))
    if numSlots == 0:
        return [func]
    
    options = getOptions(positionalConditions, cantUse, numSlots, func)
    
    variations = []
    for n in options:
        x = func.find('x')
        newFunc = f"{func[0:x]}{n}{func[x+1:len(func)]}"            
        variations.extend(produceVariations(positionalConditions, cantUse, newFunc))
    
    return variations
    
def isSensible(func: str) -> bool:
    return (
        funcHasEqualSign(func) and
        rhsIsNum(func) and
        operationsAreSurroundedByNums(func) and
        lhsHasOperation(func) and
        containsDivideByZeros(func)
    )
    
def isValidWithPositionalConditions(func: str, positionalConditions: list[tuple]) -> bool:
    for positionalCond, x in zip(positionalConditions, func):
        if x in positionalCond:
            return False
    return True    
    
def isCorrect(func: str) -> bool:
    
    eqSignIdx = func.find('=')
    equation, result = func[0:eqSignIdx], int(func[eqSignIdx+1:len(func)])
    
    equationList = [0]
    for c in equation:
        try:
            i = int(c)
            if type(equationList[-1]) is int:
                equationList[-1] = equationList[-1]*10+i
            else:
                equationList.append(i)
        except:
            equationList.append(c)
    
    while len(equationList) != 1:
        for sign in ['*', '/', '+', '-']:
            try:
                idx = equationList.index(sign)
            except:
                idx = -1
            while idx != -1:
                if sign == '*':
                    value = equationList[idx-1] * equationList[idx+1]
                if sign == '/':
                    value = equationList[idx-1] / equationList[idx+1]
                if sign == '+':
                    value = equationList[idx-1] + equationList[idx+1]
                if sign == '-':
                    value = equationList[idx-1] - equationList[idx+1]
                equationList[idx] = value
                equationList.pop(idx-1)
                equationList.pop(idx)
                try:
                    idx = equationList.index(sign)
                except:
                    idx = -1
                
    return (equationList[0] == result)