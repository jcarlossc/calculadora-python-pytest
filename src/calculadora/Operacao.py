from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def executar() -> float:
        pass