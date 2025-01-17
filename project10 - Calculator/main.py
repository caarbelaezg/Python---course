def add (a: int, b: int) -> int:
    return a + b

def subs (a: int, b: int) -> int:
    return a - b

def mult (a: int, b: int) -> int:
    return a * b

def divide (a: int, b: int) -> int:
    if b != 0:
        return a // b
    else:
        print("you can't divide by 0")

operations = {
    "+": add,
    "-": subs,
    "*": mult,
    "/": divide
}

def calculator():
    action = 'n'
    result = 0
    while True:
        fn = int(input("What's the first number: ")) if action == 'n' else result
        op = input("Pick an operation + - * /: ").strip()
        sn = int(input("What's the second number: "))

        result = operations[op](fn, sn)

        print(f"{fn} {op} {sn} = {result}")

        action = input(f"""
            Type 'y' if you want to continue calculating with {result}, 
            n to start a new calculation or f to finish: """).strip()

        if action == 'f':
            break

if __name__ == '__main__':
    calculator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
