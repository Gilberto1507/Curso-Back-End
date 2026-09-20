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
    
def mostrar_menu(lista_de_itens):
    print("=== Catálogo da Biblioteca ===")

    print()
    print("--- Livros ---")
    for numero, item in enumerate(lista_de_itens, start = 1):
        if isinstance(item, Livros):
            print(f"{numero} - {item.descricao()}")

    print()
    print("--- Revistas ---")
    for numero, item in enumerate(lista_de_itens, start = 1):
        if isinstance(item, Revistas):
            print(f"{numero} - {item.descricao()}")


livro1 = Livros("Harry Potter e a Pedra Filosofal", "J.K. Rowling")
livro2 = Livros("1984", "George Orwell")
livro3 = Livros("O Iluminado", "Stephen King")
livro4 = Livros("Memórias Póstumas de Brás Cubas", "Machado de Assis")

revista1 = Revistas("Superinteressante", "Edição 400")
revista2 = Revistas("Quatro Rodas", "Edição 750")
revista3 = Revistas("Mundo Estranho", "Edição 185")
revista4 = Revistas("VEJA", "Edição 3000")

estante = [livro1, livro2, livro3, livro4, revista1, revista2, revista3, revista4]

mostrar_menu(estante)
print()

escolha = int(input("Digite o Nº do item que gostaria de Alugar: "))
print()

item_escolhido = estante[escolha - 1]
item_escolhido.emprestar()