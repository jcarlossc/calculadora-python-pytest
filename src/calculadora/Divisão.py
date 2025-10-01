from calculadora.Operacao import Operacao

class Divisao(Operacao):

    def executar(self, num1: float, num2: float) -> float:

        try:
            return num1 / num2
        except ZeroDivisionError as e:
            print(f"Erro: {e}")