from decimal import Decimal
import view
import model
import operations


def simple_calculate(first_number: Decimal):
    result = 0
    model.set_memory(first_number)
    while True:
        oper = view.input_operation()
        model.set_operation(oper)
        if oper == '=':
            view.print_result(result)
            break
        number = view.input_number('Введите число: ')
        model.set_number(number)

        first = model.get_memory()
        oper = model.get_operation()
        second = model.get_number()
        for operation in operations.operations:
            if oper == operation:
                result = operations.operations.get(oper)(first, second)
            elif oper == '/' and second == 0:
                print('На ноль делить нельзя.')
                break

        view.print_result(result)
        model.set_memory(result)
        model.set_result(result)


def string_expression(expression: list):
    if '(' in expression:

        result = string_calculate(check_parentheses(expression))
    else:
        result = string_calculate(expression)
    model.set_result(result)


def string_calculate(expression: list):
    new_expression = []
    for item in expression:
        if isinstance(item, Decimal):
            new_expression.append(Decimal(item))
        else:
            new_expression.append(item)
    # i = 0
    while len(new_expression) > 1:
        i = 0
        while (('*' in new_expression) or ('/' in new_expression)) and i < len(new_expression):
            if new_expression[i] in ['*', '/']:
                result = operations.operations.get(new_expression[i])(Decimal(new_expression[i - 1]),
                                                                      Decimal(new_expression[i + 1]))
                new_expression[i - 1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            i += 1
        while (('+' in new_expression) or ('-' in new_expression)) and i < len(new_expression):
            if new_expression[i] in ['+', '-']:
                result = operations.operations.get(new_expression[i])(Decimal(new_expression[i - 1]),
                                                                      Decimal(new_expression[i + 1]))
                new_expression[i - 1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            i += 1

    return new_expression[0]


def check_parentheses(expression):
    while '(' in expression:
        open_index, close_index = 0, 0
        for i in range(len(expression)):
            if expression[i] == '(':
                open_index = i
            if expression[i] == ')':
                close_index = i
                break
        else:
            break
        first_expression = expression[0:open_index]
        part_expression = expression[open_index + 1:close_index]
        last_expression = expression[close_index + 1:]
        expression = first_expression + [string_calculate(part_expression)] + last_expression
    return expression


def validator_expression(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.insert(0, char)
        if char == ')':
            if len(stack) > 0:
                stack.pop(0)
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True


def first_input():
    while True:
        number = view.first_input()
        number = number.strip().replace(' ', '').replace('+', ' + ').replace('-', ' - '). \
            replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
        if number[0] == '-':
            number[0] = number[0] + number[1]
            number.pop(1)
        if len(number) < 2:
            number = float(number[0])
            number = str(number)
            number = Decimal(number)
            simple_calculate(number)
        else:
            if validator_expression(number):
                string_expression(number)
            else:
                print('Введено некорректное выражение')
        result = model.get_result()
        view.print_result(result)
        retry = input('Посчитать еще одно выражение? (y/n): ')
        if retry == 'n':
            break
