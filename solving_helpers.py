from functools import reduce
import equation_checks as checks

all_options = []
number_options = [str(i) for i in range(0,10)]
all_options.extend(number_options)
operations = ["+","-","*","/","="]
all_options.extend(operations)

def option_must_be_num(func: str):
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
    except ValueError:
        pass
    try:
        # If preceding value was operation, must follow with a number
        if func[idx-1] in operations:
            return True
    except ValueError:
        pass
    return False

def get_must_use(positional_conditions: list[tuple], func: str) -> list[int]:
    def reduce_func(list_a, list_b):
        list_a.extend(list(list_b))
        return list_a
    must_use_nums = reduce(reduce_func, positional_conditions, [])
    return list(set(filter(lambda x: str(x) not in func, must_use_nums)))

def get_cant_use(cant_use, cant_use_in_this_position):
    all_cant_use = []
    for value in cant_use:
        try:
            num = int(value)
            all_cant_use.append(num)
        except ValueError:
            pass
        all_cant_use.append(value)
    all_cant_use.extend(cant_use_in_this_position)
    return all_cant_use

def get_options(
    positional_conditions: list[tuple],
    cant_use: list[int],
    num_slots, func: str
    ) -> list:

    idx = func.find('x')
    cant_use_in_this_position = positional_conditions[idx]
    if '=' not in func and idx == len(func)-2:
        return ['=']
    options = all_options
    if idx == 0:
        options = list(filter(lambda x: x not in [0, '0'], options))
    must_use = get_must_use(positional_conditions, func)
    if num_slots == len(must_use):
        options = must_use
    if option_must_be_num(func):
        options = list(filter(lambda x: x in number_options, options))
    filter_cant_use = lambda x: x not in get_cant_use(cant_use, cant_use_in_this_position)
    options = list(filter(filter_cant_use, options))
    return options

def produce_variations(
    positional_conditions: list[tuple],
    cant_use: list[int],
    func: str
    ) -> list[str]:

    num_slots = len(list(filter(lambda c: c == 'x', func)))
    if num_slots == 0:
        return [func]

    options = get_options(positional_conditions, cant_use, num_slots, func)

    variations = []
    for option in options:
        unknowns = func.find('x')
        new_func = f"{func[0:unknowns]}{option}{func[unknowns+1:len(func)]}"
        if new_func.count('x') == 6:
            print(new_func)
        variations.extend(produce_variations(positional_conditions, cant_use, new_func))

    return variations

def is_sensible(func: str) -> bool:
    return (
        checks.func_has_equal_sign(func) and
        checks.rhs_is_num(func) and
        checks.operations_are_surrounded_by_nums(func) and
        checks.lhs_has_operation(func) and
        not checks.contains_divide_by_zeros(func) and
        not checks.contains_leading_zeros(func)
    )

def is_valid_with_positional_conditions(func: str, positional_conditions: list[tuple]) -> bool:
    for positional_cond, value in zip(positional_conditions, func):
        if value in positional_cond:
            return False
    return True

def calculate_rhs(equation: str):
    equation_list = [0]
    for value in equation:
        try:
            i = int(value)
            if isinstance(equation_list[-1], int):
                equation_list[-1] = equation_list[-1]*10+i
            else:
                equation_list.append(i)
        except ValueError:
            equation_list.append(value)
    while len(equation_list) != 1:
        for sign in ['*', '/', '+', '-']:
            try:
                idx = equation_list.index(sign)
            except ValueError:
                idx = -1
            while idx != -1:
                if sign == '*':
                    value = equation_list[idx-1] * equation_list[idx+1]
                if sign == '/':
                    value = equation_list[idx-1] / equation_list[idx+1]
                if sign == '+':
                    value = equation_list[idx-1] + equation_list[idx+1]
                if sign == '-':
                    value = equation_list[idx-1] - equation_list[idx+1]
                equation_list[idx] = value
                equation_list.pop(idx-1)
                equation_list.pop(idx)
                try:
                    idx = equation_list.index(sign)
                except ValueError:
                    idx = -1
    return equation_list[0]

def is_correct(func: str) -> bool:
    idx = func.find('=')
    equation, result = func[0:idx], int(func[idx+1:len(func)])
    calculated_result = calculate_rhs(equation)
    return calculated_result == result
