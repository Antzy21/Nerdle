from solvingHelpers import findSolutions

def func(a,b,c,d):
    return((10*a+b)-(10*c+d))

def strFunc(result,a,b,c,d):
    return(f"{a}{b}-{c}{d}={result}")

mustUseNums = [3,4,5,6,9]
cantUseNums = [1,2,7,8]
findSolutions(
    mustUseNums, 
    cantUseNums, 
    strFunc, 
    func, 
    2, 
    ())