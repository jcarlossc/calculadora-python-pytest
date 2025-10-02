from calculadora.Operacao import Operacao

class Divisao(Operacao):
    """
        Classe que implementa a operação de divisão.
    """
    def executar(self, num1: float, num2: float) -> float:
        """
            Retorna a divisão entre dois números.
            Args:
                num1 (float): Primeiro número.
                num2 (float): Segundo número.    

            Retorna:
                float: Resultado da operação.

            Raises:
                ValueError: Divisão por zero não permitida.   
        """
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Parâmetros inválidos para divisão.")
        elif num2 == 0:
            raise ValueError("Divisão por zero não permitida.")
        return num1 / num2