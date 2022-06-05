import sys
from functools import reduce
from solving_helpers import is_sensible, is_correct, produce_variations

def get_constraints(attempt, func, cant_use, positional_conditions):
    print(f"\nEnter results for equation: {attempt}")
    print("--- Not used : 0 --- Used : 1 --- Used in place : 2 ---")
    for i, value in enumerate(attempt):
        if value != func[i]:
            state = input(f"\nResult for {value}: ")
            if state == "0":
                if value not in cant_use:
                    cant_use.append(value)
            elif state == "1":
                positional_conditions[i].append(value)
            elif state == "2":
                func = func[:i] + value + func[i+1:]
            print("func:", func, "--- cant_use:", cant_use, "--- posConds: ", positional_conditions)
    return func, cant_use, positional_conditions

def calculate(func, cant_use, positional_conditions):
    variations = produce_variations(positional_conditions, cant_use, func)
    print(len(variations), "variations")
    sensible_equations = list(filter(is_sensible, variations))
    print(len(sensible_equations), "sensible equations")
    correct_equations = list(filter(is_correct, sensible_equations))
    print(len(correct_equations), "correct equations")
    return correct_equations

def initialize_constraints(equations: list):
    if equations == []:
        equations = ["9*8-7=65"]
    func = len(equations[0])*"x"
    cant_use = []
    positional_conditions = [[] for _ in equations[0]]
    default_constraints = (func, cant_use, positional_conditions)
    def reducer(constraints, next_equation):
        func, cant_use, positional_conditions = constraints
        return get_constraints(next_equation, func, cant_use, positional_conditions)
    return reduce(reducer, equations, default_constraints)

def main():
    if len(sys.argv) == 1:
        equations = []
    else:
        equations = sys.argv[1:]
    func, cant_use, pos_conditions = initialize_constraints(equations)
    possible_answers = []
    while len(possible_answers) != 1:
        print("\nCalculating...\n")
        possible_answers = calculate(func, cant_use, pos_conditions)
        print(possible_answers)
        if len(possible_answers) < 10:
            break
        attempt = input("\nNext attempted equation: ")
        if attempt == "":
            break
        func, cant_use, pos_conditions = get_constraints(attempt, func, cant_use, pos_conditions)

main()
