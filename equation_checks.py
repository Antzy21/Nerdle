def funcHasEqualSign(func: str) -> bool:
    eqSignIdx = func.find('=')
    return eqSignIdx != -1
    
def rhsIsNum(func: str) -> bool:
    eqSignIdx = func.find('=')
    result = func[eqSignIdx+1:len(func)]
    try:
        result = int(result)
        return True
    except ValueError:
        return False
    
def lhsHasOperation(func: str) -> bool:
    eqSignIdx = func.find('=')
    equation = func[0:eqSignIdx]
    try:
        int(equation)
        return False
    except ValueError:
        return True
    
def operationsAreSurroundedByNums(func: str) -> bool:
    for o in ["+","-","*","/","="]:
        oPos = func.find(o)
        if oPos in [0, len(func)]:
            return False
        if oPos != -1:
            try:
                int(func[oPos-1])
                int(func[oPos+1])
            except ValueError:
                return False
    return True
  
def containsDivideByZeros(func: str) -> bool:
    return func.find("/0") != -1

def containsLeadingZeros(func: str):
    for idx, x in enumerate(func):
        if x == '0':
            if (idx == 0 or func[idx-1] in ["+","-","*","/","="]) and (idx != len(func)-1 and func[idx+1] not in ["+","-","*","/","="]):
                return True
    return False