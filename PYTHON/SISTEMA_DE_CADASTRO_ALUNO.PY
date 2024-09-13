class Aluno:
    def __init__(self, nome, nota01, nota02):
        self.__nome = nome
        self.__nota01 = nota01
        self.__nota02 = nota02
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
   
    def set_nota01(self, nota01):
        self.__nota01 = nota01
    
    def get_nota01(self):
        return self.__nota01
    
    def set_nota02(self, nota02):
        self.__nota02 = nota02
    
    def get_nota02(self):
        return self.__nota02
    
    def calcular_media(self):
        return (self.__nota01 + self.__nota02) / 2

if __name__ == "__main__":
    aluno = Aluno("Tristan Gabriel Nobrega Cezar", 9.0, 10.0)
    print("Nome do aluno:", aluno.get_nome())
    print("Nota 1:", aluno.get_nota01())
    print("Nota 2:", aluno.get_nota02())
    print("Media:", aluno.calcular_media())

   