import time
import random

class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.saude = 50
        self.energia = 50

    def verificar_estado(self):
        if self.fome <= 0 or self.saude <= 0 or self.energia <= 0:
            print(f"{self.nome} morreu!")
            return False
        elif self.fome <= 20:
            print(f"{self.nome} está com fome :c !")
        elif self.saude <= 20:
            print(f"{self.nome} está doente :c !")
        elif self.energia <= 20:
            print(f"{self.nome} está cansado :c !")
        return True

    def alimentar(self):
        print(f"Alimentando {self.nome}...")
        print(f"٩(ˊᗜˋ*)و ")
        self.fome += random.randint(5, 15)
        self.energia -= random.randint(1, 5)
        self.verificar_estado()

    def curar(self):
        print(f"Cuidando da saúde de {self.nome}...")
        print(f"( ´ ▽ ` )ﾉ")
        self.saude += random.randint(5, 15)
        self.energia -= random.randint(1, 5)
        self.verificar_estado()

    def descansar(self):
        print(f"Dando descanso para {self.nome}...")
        print(f"Descanse também!")
        self.energia += random.randint(5, 15)
        self.fome -= random.randint(1, 5)
        self.verificar_estado()

    def brincar(self):
        print(f"Brincando com {self.nome}...")
        print(f"{self.nome} está feliz por brincar com você!")

        self.energia -= random.randint(5, 15)
        self.saude -= random.randint(1, 5)
        self.verificar_estado()

def main():
    nome = input("Escolha um nome para o seu Tamagotchi! ")
    pet = Tamagotchi(nome)

    while pet.verificar_estado():
        print("\nAções disponíveis:")
        print("1 - Alimentar")
        print("2 - Curar")
        print("3 - Descansar")
        print("4 - Brincar")
        print("5 - Sair")

        escolha = input("Escolha uma ação: ")

        if escolha == '1':
            pet.alimentar()
        elif escolha == '2':
            pet.curar()
        elif escolha == '3':
            pet.descansar()
        elif escolha == '4':
            pet.brincar()
        elif escolha == '5':
            print("Saindo do jogo ヾ(＾ ∇ ＾)...")
            break
        else:
            print("Opção inválida!")

        time.sleep(1)

if __name__ == "__main__":
    main()
