from calculadora.Soma import Soma
from calculadora.Subtracao import Subtracao
from calculadora.Multiplicacao import Multiplicacao
from calculadora.Divisao import Divisao

def main():
    somar = Soma()
    print(f"O resultado da soma é: {somar.executar(5, 3)}")

    subtrair = Subtracao()
    print(f"O resultado da subtração é: {subtrair.executar(5, 3)}")

    multiplicar = Multiplicacao()
    print(f"O resultado da multiplicação é: {multiplicar.executar(5, 3)}")

    dividir = Divisao()
    print(f"O resultado da divisão é: {dividir.executar(6, 0)}")
    
    dividir = Divisao()
    print(f"O resultado da divisão é: {dividir.executar(6, 2)}")

if __name__ == "__main__":
    main()