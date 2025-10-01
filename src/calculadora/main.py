from calculadora.Soma import Soma
from calculadora.Subtracao import Subtracao

def main():
    somar = Soma()
    print(f"O resultado da soma é: {somar.executar(5, 3)}")

    subtrair = Subtracao()
    print(f"O resultado da subtração é: {subtrair.executar(5, 3)}")




if __name__ == "__main__":
    main()