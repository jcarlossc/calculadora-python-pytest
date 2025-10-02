import pytest
from calculadora.Soma import Soma
from calculadora.Subtracao import Subtracao
from calculadora.Multiplicacao import Multiplicacao
from calculadora.Divisao import Divisao

def test_soma():
    operacao = Soma()
    assert operacao.executar(5, 3) == 8

def test_subtrai():
    operacao = Subtracao()
    assert operacao.executar(10, 4) == 6

def test_multiplica():
    operacao = Multiplicacao()
    assert operacao.executar(6, 7) == 42

def test_divide():
    operacao = Divisao()
    assert operacao.executar(8, 2) == 4

def test_divisao_por_zero():
    operacao = Divisao()
    with pytest.raises(ValueError, match="Divisão por zero não permitida"):
        operacao.executar(10, 0)
