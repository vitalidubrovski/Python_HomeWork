from decimal import Decimal

first_number = 0
operation = ''
second_number = 0
result = 0


def get_memory():
    global first_number
    return first_number


def set_memory(value: Decimal):
    global first_number
    first_number = value


def get_result():
    global result
    return result


def set_result(value: Decimal):
    global result
    result = value


def get_operation():
    global operation
    return operation


def set_operation(value: str):
    global operation
    operation = value


def get_number():
    global second_number
    return second_number


def set_number(value: Decimal):
    global second_number
    second_number = value
