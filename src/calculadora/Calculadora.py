from calculadora.Operacao import Operacao

class Calculadora:
    """
        Classe que representa a calculadora, responsável por 
        aplicar uma estratégia de operação matemática.

        A estratégia é passada no momento da criação da instância.

        Exemplo:
            >>> calc = Calculadora(Soma())
            >>> calc.calcular(5, 3)
            8
    """
    def __init__(self, estrategia: Operacao) -> None:
        """
            Inicializa a calculadora com uma estratégia.

            Args:
                estrategia (Operacao): A operação a ser utilizada.
        """
        self.estrategia = estrategia

    def calcular(self, num1: float, num2: float) -> float:
        """
            Executa o cálculo usando a estratégia definida.

            Args:
                num1 (float): Primeiro número.
                num2 (float): Segundo número.

            Retorna:
                float: Resultado do cálculo.
        """
        return self.estrategia.executar(num1, num2)