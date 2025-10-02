from calculadora.Operacao import Operacao

class Subtracao(Operacao):
    """
        Classe que implementa a operação de subtração.
    """
    def executar(self, num1: float, num2: float) -> float:
        """
            Retorna a subtração entre dois números.
            Args:
                num1 (float): Primeiro número.
                num2 (float): Segundo número.    

            Retorna:
                float: Resultado da operação.

            Raises:
                ValueError: se os parâmetros não forem numéricos.
        """
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Parâmetros inválidos para subtração.")
        return num1 - num2