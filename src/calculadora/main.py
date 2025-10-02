from calculadora.Soma import Soma
from calculadora.Subtracao import Subtracao
from calculadora.Multiplicacao import Multiplicacao
from calculadora.Divisao import Divisao
from calculadora.Calculadora import Calculadora

def main():

    try:
        somar = Calculadora(Soma())
        print(f"✅ Resultado da soma: {somar.calcular(5, 3)}")
    except ValueError as e:
        print(f"❌ Erro ao calcular soma: {e}")
    
    try:
        somar = Calculadora(Soma())
        print(f"✅ Resultado da soma: {somar.calcular(5, "3")}")
    except ValueError as e:
        print(f"❌ Erro ao calcular soma: {e}")

    try:
        subtrair = Calculadora(Subtracao())
        print(f"✅ Resultado da subtração: {subtrair.calcular(5, 3)}")
    except ValueError as e:
        print(f"❌ Erro ao calcular subtração: {e}")

    try:
        subtrair = Calculadora(Subtracao())
        print(f"✅ Resultado da subtração: {subtrair.calcular("5", 3)}")
    except ValueError as e:
        print(f"❌ Erro ao calcular subtração: {e}")
    
    try:
        multiplicar = Calculadora(Multiplicacao())
        print(f"✅ Resultado da multiplicação: {multiplicar.calcular(5, 3)}")
    except ValueError as e:
        print(f"❌ Erro ao calcular multiplicação: {e}")

    try:
        multiplicar = Calculadora(Multiplicacao())
        print(f"✅ Resultado da multiplicação: {multiplicar.calcular(5, "3")}")
    except ValueError as e:
        print(f"❌ Erro ao calcular multiplicação: {e}")
    
    try:
        dividir = Calculadora(Divisao())
        print(f"✅ Resultado da divisão: {dividir.calcular(9, 3)}")
    except ValueError as e:
        print(f"❌ Erro ao calcular divisão: {e}")

    try:
        dividir = Calculadora(Divisao())
        print(f"✅ Resultado da divisão: {dividir.calcular("9", 3)}")
    except ValueError as e:
        print(f"❌ Erro ao calcular divisão: {e}")

    try:
        dividir = Calculadora(Divisao())
        print(f"✅ Resultado da divisão: {dividir.calcular(9, 0)}")
    except ValueError as e:
        print(f"❌ Erro ao calcular divisão: {e}")

if __name__ == "__main__":
    main()