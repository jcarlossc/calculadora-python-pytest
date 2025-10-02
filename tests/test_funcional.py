import pytest
from calculadora.Soma import Soma
from calculadora.Subtracao import Subtracao
from calculadora.Multiplicacao import Multiplicacao
from calculadora.Divisao import Divisao
from calculadora.Calculadora import Calculadora 

@pytest.mark.parametrize("op,a,b,esperado", [
    (Soma(), 2, 3, 5),
    (Subtracao(), 15, 5, 10),
    (Multiplicacao(), 7, 6, 42),
    (Divisao(), 20, 4, 5),
])
def test_fluxo_funcional(op, a, b, esperado):
    calcular = Calculadora(op)
    assert calcular.calcular(a, b) == esperado
