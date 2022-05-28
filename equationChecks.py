
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
    for o in ["+","-","*","/","="]:
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
  
def containsDivideByZeros(func: str) -> bool:
    return func.find("/0") == -1