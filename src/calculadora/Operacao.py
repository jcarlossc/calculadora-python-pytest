from abc import ABC, abstractmethod

class Operacao(ABC):
    """
        Classe abstrata que define a interface para operações matemáticas.

        Todas as operações concretas (Soma, Subtrai, Multiplica, Divide) 
        devem herdar desta classe e implementar o método `executar`.
    """
    @abstractmethod
    def executar(num1: float, num2: float) -> float:
        """
            Executa a operação matemática entre dois números.

            Args:
                num1 (float): Primeiro número.
                num2 (float): Segundo número.

            Retorna:
                float: Resultado da operação.
        """
        pass