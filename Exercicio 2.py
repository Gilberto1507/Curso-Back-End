class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar(self, item):
        self.catalogo.append(item)

    def listar_itens(self):
        print("=== Catálogo da Biblioteca ===")

        print()
        print("--- Livros ---")
        for numero, item in enumerate(self.catalogo, start = 1):
            if isinstance(item, Livros):
                print(f"{numero} - {item.descricao()}")

        print()
        print("--- Revistas ---")
        for numero, item in enumerate(self.catalogo, start = 1):
            if isinstance(item, Revistas):
                print(f"{numero} - {item.descricao()}")

    def remover(self):
        self.listar_itens()
        X = int(input("Digite a Posição que gostaria de Remover: "))
        item_removido = self.catalogo.pop(X - 1)
        print(f"O Item {item_removido.titulo} foi removido do Catalogo com Secesso")

    def buscar_titulo(self):
        titulo_buscando = input("\nDigite o Titulo que deseja Buscar: ").strip().lower()

        for item in self.catalogo:
            if item.titulo.lower() == titulo_buscando:
                print(f"Item Encontrado: {item.descricao()}")
                if item.disponivel:
                    print("Status: Disponivel para Aluguel")
                else:
                    print("Status: Indisponivel, esta sendo Alugado")
                return
        print(f"Desculpe, o Titulo {titulo_buscando} não se encontra em nossa Biblioteca")

    def emprestar_item(self):
        self.listar_itens()
        print()

        escolha = int(input("Digite o Nº do item que você deseja Alugar: "))
        item_escolhido = self.catalogo[escolha - 1]
        item_escolhido.emprestar()

    def devolver_item(self):
        self.listar_itens()
        print()

        escolha = int(input("Digite o Nº do item que você deseja Devolver: "))
        item_escolhido = self.catalogo[escolha - 1]
        item_escolhido.devolver()
        
class Itens_Acervo:
    def __init__(self,titulo):
        self.titulo = titulo
        self.__disponivel = True

    @property
    def disponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel == True:
            self.__disponivel = False
            print(f"O Livro {self.titulo} foi Alugado com sucesso!")
        else:
            print(f"O Livro {self.titulo} ja esta sendo Alugado, peço desculpa pelo ocorrido.")

    def devolver(self):
        if self.__disponivel == False:
            self.__disponivel = True
            print(f"O Livro {self.titulo} foi Devolvido com sucesso!")
        else:
            print(f"O Livro {self.titulo} não esta sendo Alugado no momento.")

class Livros(Itens_Acervo):
    def __init__(self, titulo, autor):
        super().__init__(titulo)
        self.autor = autor

    def descricao(self):
        return (f"Livro: {self.titulo} e Autor: {self.autor}")

class Revistas(Itens_Acervo):
    def __init__(self, titulo, edicao):
        super().__init__(titulo)
        self.edicao = edicao

    def descricao(self):
        return (f"Revista: {self.titulo} e Edição: {self.edicao}")
    

livro1 = Livros("Harry Potter e a Pedra Filosofal", "J.K. Rowling")
livro2 = Livros("1984", "George Orwell")
livro3 = Livros("O Iluminado", "Stephen King")
livro4 = Livros("Memórias Póstumas de Brás Cubas", "Machado de Assis")

revista1 = Revistas("Superinteressante", "Edição 400")
revista2 = Revistas("Quatro Rodas", "Edição 750")
revista3 = Revistas("Mundo Estranho", "Edição 185")
revista4 = Revistas("VEJA", "Edição 3000")

minha_biblioteca = Biblioteca()

lista_inicial = [livro1, livro2, livro3, livro4, revista1, revista2, revista3, revista4]
for item in lista_inicial:
    minha_biblioteca.adicionar(item)

while True:
    print("\n" + "="*30)
    print("Sistema da Biblioteca")
    print("="*30)
    print("1 - Listar Catalogo")
    print("2 - Buscar Titulo")
    print("3 - Alugar Item")
    print("4 - Devolver Item")
    print("5 - Remover do Sistema")
    print("0 - Sair")

    opcao = input("Escolha uma Opção: ").strip().replace("\r", "")

    if opcao == "1":
        minha_biblioteca.listar_itens()
    elif opcao == "2":
        minha_biblioteca.buscar_titulo()
    elif opcao == "3":
        minha_biblioteca.emprestar_item()
    elif opcao == "4":
        minha_biblioteca.devolver_item()
    elif opcao == "5":
        minha_biblioteca.remover()
    elif opcao == "0":
        print("FIm do Programa!")
        break
    else:
        print("Número Invalido, Escolha uma opção Possivel.")