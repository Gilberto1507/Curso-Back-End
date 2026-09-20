def Classificação_de_Idade(X):
    if X >= 0 and X <= 12:
        print("Sua Idade é correspondente a de uma Criança")
    elif X >= 13 and X <= 17:
        print("Sua Idade é correspondente a de um Adolescente")
    elif X >= 18 and X <= 59:
        print("Sua Idade é correspondente a de um Adulto")
    else:
        print("Sua Idade é correspondente a de um Idoso")

X = int(input("Digite a sua Idade: "))

Classificação_de_Idade(X)