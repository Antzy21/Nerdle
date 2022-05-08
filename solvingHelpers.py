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
            
def isSlot(c):
    return c == 'x'
            
def produceVariations(mustUse: list[int], cantUse: list[int], func: str) -> list[str]:
    numSlots = len(list(filter(isSlot, func)))
    if numSlots == 0:
        return [func]
    elif numSlots == len(mustUse):
        options = mustUse
    else:
        options = list(filter(lambda x: x not in cantUse, range(1,10)))
    
    variations = []
    for n in options:
        i = func.find('x')
        newFunc = f"{func[0:i]}{n}{func[i+1:len(func)]}"
        
        newMustUse = mustUse[:]
        if n in newMustUse:
            newMustUse.remove(n)
            
        variations.extend(produceVariations(newMustUse, cantUse, newFunc))
    
    return variations
    
def isValidVariation(func: str, positionalConditions: list[tuple]) -> bool:
    eqSignIdx = func.find('=')
    if eqSignIdx == -1:
        print("Error: no equal sign found")
        return False
    
    for positionalCond in positionalConditions:
            index = positionalCond[0]
            if func[index] == positionalCond[1]:
                return False
    
    equation, result = func[0:eqSignIdx], func[eqSignIdx+1:len(func)]
    result = int(result)
    
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
    
    if len(equationList) % 2 == 0:
        print("Error: left hand side of equation incorrect.")
        return False
    
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