# źródło inspiracji: https://stackoverflow.com/questions/69026151/how-to-make-calculator-with-out-if-else

from operator import add, sub, mul, truediv

operations_and_functions= {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
}

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
op = input("Podaj operator: +, -, *, /: ")

w = operations_and_functions[op](a,b)
print(f"{a} {op} {b} = {w}")
