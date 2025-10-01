from calculadora.Operacao import Operacao

class Subtracao(Operacao):

    def subtrair(num1: float, num2: float) -> float:
        
        try:
            return num1 - num2
        except Exception as e:
            print(f"Erro: {e}")