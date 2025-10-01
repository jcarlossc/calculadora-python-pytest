from calculadora.Operacao import Operacao

class Multiplicacao(Operacao):
    """
        Classe que implementa a operação de multiplicação.
    """
    def executar(self, num1: float, num2: float) -> float:
        """
            Retorna a multiplicação entre dois números.
            Args:
                num1 (float): Primeiro número.
                num2 (float): Segundo número.    

            Retorna:
                float: Resultado da operação.
        """
        try:
            return num1 * num2
        except Exception as e:
            print(f"Erro: {e}")