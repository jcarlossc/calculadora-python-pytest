from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def executar(num1: float, num2: float) -> float:
        pass