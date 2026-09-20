Lista_Atletica = []

N = int(input("Digite o Nº de Integrandes de cada Lista: "))

print("Preencha a Lista da Atletica")
for i in range (N):
    X = str(input(f"Digite o E-mail do {i + 1}º Integrante: "))
    Lista_Atletica.append(X)

print()
print("--- Lista da Atletica ---")
print(Lista_Atletica)

Lista_Sala = []

print()
print("Preencha a Lista da Sala")
for i in range (N):
    X = str(input(f"Digite o E-mail do {i + 1}º Integrante: "))
    Lista_Sala.append(X)

print()
print("--- Lista da Sala ---")
print(Lista_Sala)

set_atleitca = set(Lista_Atletica)
set_sala = set(Lista_Sala)

print()
print("Apenas os Integrantes da Atletica e da Sala:")
print(set_atleitca & set_sala)
print()

print("Apenas os Integrantes da Atletica ou da Sala:")
print(set_atleitca ^ set_sala)
print()

print("Todos os Menbros da Atletica e da Sala:")
print(set_atleitca | set_sala)