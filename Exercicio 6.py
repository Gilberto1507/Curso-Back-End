class Tarefa:
    def __init__ (self, nome, descricao, data_criacao):
        self.nome = nome
        self.descricao = descricao
        self.concluida = False
        self.data_criacao = data_criacao

    def marcar_concluida(self):
        self.concluida = True
        return self.concluida

    def __str__(self):
        if self.concluida == True:
            return (f"Tarefa: {self.nome} | Descrição: {self.descricao} | Status: Concluida")
        else:
            return (f"Tarefa: {self.nome} | Descrção: {self.descricao} | Status: Pendente")

lista_de_tarefas = []

while True:
    print("\n" + "="*30)
    print("Planejamento das Tarefas")
    print("="*30)
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Marcar Tareda como Concluida")
    print("5 - Sair")

    opcao = input("Escolha uma Opção: ").strip().replace("\r", "")

    if opcao == "1":
        X = str(input("Digite o Nome da Sua Tarefa: "))
        Y = str(input("Digite a Descrição da Sua Tarefa: "))
        Z = input("Digite a Data da Sua Tarefa: ")

        nova_tarefa = Tarefa(X, Y, Z)
        lista_de_tarefas.append(nova_tarefa)
        print()

    elif opcao == "2":
        for numero, item in enumerate(lista_de_tarefas, start = 1):
            print(f"{numero} | {item}")
            print()

    elif opcao == "3":
        for numero, item in enumerate(lista_de_tarefas, start = 1):
            print(f"{numero} | {item}")

        T = int(input("Digite a Posição que gostaria de Remover: "))

        item_removido = lista_de_tarefas.pop(T - 1)
        print(f"A Tarefa {item_removido.nome} foi removido do Catalogo com Secesso")
        print()
            
    elif opcao == "4":
        for numero, item in enumerate(lista_de_tarefas, start = 1):
            print(f"{numero} | {item}")

        B = int(input("Digite a Posição que gostaria de Finalizar: "))

        item_finalizada = lista_de_tarefas[B - 1]
        item_finalizada.marcar_concluida()
        print(f"A Tarefa {item_finalizada.nome} foi Finalizada com Secesso")
        print()

    elif opcao == "5":
        print("FIm do Programa!")
        break

    else:
        print("Número Invalido, Escolha uma opção Possivel.")

    