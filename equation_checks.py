def func_has_equal_sign(func: str) -> bool:
    idx = func.find('=')
    return idx != -1

def rhs_is_num(func: str) -> bool:
    idx = func.find('=')
    result = func[idx+1:len(func)]
    try:
        result = int(result)
        return True
    except ValueError:
        return False

def lhs_has_operation(func: str) -> bool:
    idx = func.find('=')
    equation = func[0:idx]
    try:
        int(equation)
        return False
    except ValueError:
        return True

def operations_are_surrounded_by_nums(func: str) -> bool:
    for operation in ["+","-","*","/","="]:
        idx = func.find(operation)
        if idx in [0, len(func)]:
            return False
        if idx != -1:
            try:
                int(func[idx-1])
                int(func[idx+1])
            except ValueError:
                return False
    return True

def contains_divide_by_zeros(func: str) -> bool:
    return func.find("/0") != -1

def contains_leading_zeros(func: str):
    for idx, value in enumerate(func):
        if value == '0':
            follows_operation = (idx == 0 or func[idx-1] in ["+","-","*","/","="])
            precedes_operation = (idx != len(func)-1 and func[idx+1] not in ["+","-","*","/","="])
            if follows_operation and precedes_operation:
                return True
    return False
