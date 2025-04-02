#1 Calculadora Simples
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == "+":
        print(f"Resultado: {soma(num1, num2)}")
    elif operacao == "-":
        print(f"Resultado: {subtracao(num1, num2)}")
    elif operacao == "*":
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif operacao == "/":
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Operação inválida!")
