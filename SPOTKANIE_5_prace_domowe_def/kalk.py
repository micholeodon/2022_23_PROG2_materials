a = float(input("Podaj a: "))

op = ""
while op not in ["+", "-", "*", "/"]:
    op = input("Podaj operator: +, -, *, /: ")

b = float(input("Podaj b: "))

if op == "+":
    print(f"{a} {op} {b} = {a+b}")
if op == "-":
    print(f"{a} {op} {b} = {a-b}")
if op == "*":
    print(f"{a} {op} {b} = {a*b}")
if op == "/":
    print(f"{a} {op} {b} = {a/b}")
