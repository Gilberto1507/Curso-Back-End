Agenda = {}

X = int(input("Digite o Nº de Pessoas que Gostaria de Adicionar independente da Categoria: "))
for i in range(X):
    N = str(input("Digite o Nome do Contato: ")).strip()
    T = int(input("Digite o Telefone do Contato: "))
    C = str(input("DIgite a Categoria do Contato: ")).strip().lower()

    Contato = (N,T,C)

    if C not in Agenda:
        Agenda[C] = []

    Agenda[C].append(Contato)

def Buscar_Categoria(categoria, agenda):
    categoria = categoria.strip().lower()

    if categoria in agenda:
        return sorted(agenda[categoria])
    else:
        return []

Buscando = str(input("Digite uma Categoria para Buscar: ")).strip().lower()
Encontrado = Buscar_Categoria(Buscando, Agenda)

if Encontrado:
    print(f"Contatos da Categoria '{Buscando}' Ordenados por Nome")
    for nome, tel, cat in Encontrado:
        print(f"Nome: {nome} | Telefone: {tel}")
else:
    print("O Contato não foi encontrado")