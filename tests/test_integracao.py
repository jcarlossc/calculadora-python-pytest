from calculadora.Soma import Soma
from calculadora.Subtracao import Subtracao
from calculadora.Multiplicacao import Multiplicacao
from calculadora.Divisao import Divisao
from calculadora.Calculadora import Calculadora 

def test_calculadora_soma():
    calcular = Calculadora(Soma())
    assert calcular.calcular(2, 3) == 5

def test_calculadora_subtrai():
    calcular = Calculadora(Subtracao())
    assert calcular.calcular(10, 7) == 3

def test_calculadora_multiplica():
    calcular = Calculadora(Multiplicacao())
    assert calcular.calcular(4, 5) == 20

def test_calculadora_divide():
    calcular = Calculadora(Divisao())
    assert calcular.calcular(9, 3) == 3
