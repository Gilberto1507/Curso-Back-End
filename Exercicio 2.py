while True:
    X = str(input("Digite um Nome: "))
    if X != "":
        print("Nome Registrado")
        print()
        break
    print("Erro. O Nome não pode ser Vazio, preencha novamente por favor.")

while True:
    try:
        Z = int(input("Digite sua Idade: "))
        if Z >= 0 and Z <= 120:
            print("Idade Registrada")
            print()
            break
        print("Erro. A Idade deve estar entre 0 e 120, preencha novamente por favor.")
    except:
        print("Erro. DIgite Nº validos, preencha por favor.")
while True:
    Y = str(input("Digite o Seu Email: "))
    if "@" in Y:
        posicao_at = Y.find("@")
        if "." in Y[posicao_at:]:
            print("E-mail Registrado")
            print()
            break
    print("Erro. O E-mail deve conter '@' seguido de pelo menos um '.', preencha novamente por favor.")

print("Seu Cadastro esta completo.")
print(f"Nome: {X} | Idade: {Z} | E-mail: {Y}")