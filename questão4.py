def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def verificar_aprovacao():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media = calcular_media(nota1, nota2, nota3)
    print(f"Média: {media}")
    
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
