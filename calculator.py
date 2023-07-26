def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
for operation in operations:
    print(operation)
operation_symbol = input("계산 형태를 고르시오: ")
calculation_function = operations[operation_symbol]
result = calculation_function(num1,num2)

print(f" {num1} {operation_symbol} {num2} = {result}")
