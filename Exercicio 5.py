class Usuario:
    def __init__ (self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha

    @ senha.setter
    def senha(self, valor):
        if len(valor) >= 8:
            self.__senha = valor
        else:
            print("Erro: A Sua senha precida de pelo menos 8 Digitos")
            self.__senha = ""

    def verificar_senha(self, tentativa):
        if self.__senha == tentativa:
            return True
        else:
            return False

X = str(input("Digite o Nome de Usuario: "))
Y = str(input("Digite o seu Email: "))
Z = int(input("Digite sua Nova Senha: "))

usuario1 = Usuario(X, Y, Z)

S = int(input("Digite a sua Senha: "))

if usuario1.verificar_senha(S):
    print("Acesso Liberado")
else:
    print("Senha Incorreta. Acesso Negado")