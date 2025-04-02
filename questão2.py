def km_para_milhas(km):
    return km * 0.621371

def metros_para_centimetros(metros):
    return metros * 100

def litros_para_mililitros(litros):
    return litros * 1000

def conversor():
    km = float(input("Digite a distância em quilômetros: "))
    metros = float(input("Digite a distância em metros: "))
    litros = float(input("Digite a quantidade em litros: "))
    
    print(f"{km} km em milhas: {km_para_milhas(km)}")
    print(f"{metros} metros em centímetros: {metros_para_centimetros(metros)}")
    print(f"{litros} litros em mililitros: {litros_para_mililitros(litros)}")
