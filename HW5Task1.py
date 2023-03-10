# Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна
# запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

def calc_sum(x, y):
    z = x + y
    return z


def calc_subsraction(x, y):
    z = x - y
    return z


def calc_multiplication(x, y):
    z = x * y
    return z


def calc_division(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y can't be a zero"


def is_correct_operator(operator):
    return operator == '0' or operator == '+' or operator == '-' or operator == '*' or operator == '/'


def calculator(m, n, oper):
    if oper == "+":
        res = calc_sum(m, n)
        print(f'{m}+{n}={res}')
    elif oper == "-":
        res = calc_subsraction(m, n)
        print(f'{m}-{n}={res}')
    elif oper == "*":
        res = calc_multiplication(m, n)
        print(f'{m}*{n}={res}')
    elif oper == "/":
        res = calc_division(m, n)
        print(f'{m}/{n}={res}')


def run_calc():
    oper = input("Enter + - * / or 0 for end program ")
    if not is_correct_operator(oper):
        print('Wrong operator')
        run_calc()
    if oper == "0":
        return
    else:
        m = int(input("Enter x = "))
        n = int(input("Enter y = "))
        calculator(m, n, oper)
        run_calc()


run_calc()
