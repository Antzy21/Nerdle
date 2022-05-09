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
        options = list(filter(lambda x: x not in cantUse, range(1,10)))
    
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
            
allOptions = list(range(1,10))
operations = ["+","-","*","/","="]
allOptions.extend(operations)

def optionMustBeNum(func: str):
    x = func.find('x')
    if x == 0 or x == len(func):
        return True
    if '=' in func and func.find('=') < x:
        return True
    try:
        int(func[x-1])
        return False
    except:
        return True

def getOptions(mustUse: list[int], cantUse: list[int], numSlots, func: str) -> list:
    if '=' not in func and func.find('x') == len(func)-2:
        return ['=']
    options = allOptions
    if numSlots == len(mustUse):
        options = mustUse
    if optionMustBeNum(func):
        options = list(filter(lambda x: x in range(1,10), options))
    options = list(filter(lambda x: x not in cantUse, options))
    return options    

def produceVariations(mustUse: list[int], cantUse: list[int], func: str) -> list[str]:

    numSlots = len(list(filter(lambda c: c == 'x', func)))
    if numSlots == 0:
        return [func]
    
    options = getOptions(mustUse, cantUse, numSlots, func)
    
    variations = []
    for n in options:
        x = func.find('x')
        newFunc = f"{func[0:x]}{n}{func[x+1:len(func)]}"
        
        newMustUse = mustUse[:]
        if n in newMustUse:
            newMustUse.remove(n)
            
        variations.extend(produceVariations(newMustUse, cantUse, newFunc))
    
    return variations
    
def funcHasEqualSign(func: str) -> bool:
    eqSignIdx = func.find('=')
    return eqSignIdx != -1
    
def rhsIsNum(func: str) -> bool:
    eqSignIdx = func.find('=')
    result = func[eqSignIdx+1:len(func)]
    try:
        result = int(result)
        return True
    except:
        return False
    
def lhsHasOperation(func: str) -> bool:
    eqSignIdx = func.find('=')
    equation = func[0:eqSignIdx]
    try:
        int(equation)
        return False
    except:
        return True
    
def operationsAreSurroundedByNums(func: str) -> bool:
    for o in operations:
        oPos = func.find(o)
        if oPos in [0, len(func)]:
            return False
        if oPos != -1:
            try:
                int(func[oPos-1])
                int(func[oPos+1])
            except:
                return False
    return True
    
def isSensible(func: str) -> bool:
    if not funcHasEqualSign(func):
        return False
    elif not rhsIsNum(func):
        return False
    elif not operationsAreSurroundedByNums(func):
        return False
    elif not lhsHasOperation(func):
        return False
    else:
        return True
    
def isValidWithPositionalConditions(func: str, positionalConditions: list[tuple]) -> bool:
    for positionalCond in positionalConditions:
        index = positionalCond[0]
        if func[index] == positionalCond[1]:
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