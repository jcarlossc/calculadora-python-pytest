import pytest
from calculadora.Soma import Soma
from calculadora.Subtracao import Subtracao
from calculadora.Multiplicacao import Multiplicacao
from calculadora.Divisao import Divisao

def test_soma():
    operacao = Soma()
    assert operacao.executar(5, 3) == 8

def test_soma_não_numeral():
    operacao = Soma()
    with pytest.raises(ValueError, match="Parâmetros inválidos para soma."):
        operacao.executar(10, "3")    

def test_subtrai():
    operacao = Subtracao()
    assert operacao.executar(10, 4) == 6

def test_subtrair_não_numeral():
    operacao = Subtracao()
    with pytest.raises(ValueError, match="Parâmetros inválidos para subtração."):
        operacao.executar(10, "3")     

def test_multiplica():
    operacao = Multiplicacao()
    assert operacao.executar(6, 7) == 42

def test_multiplica_não_numeral():
    operacao = Multiplicacao()
    with pytest.raises(ValueError, match="Parâmetros inválidos para multiplicação."):
        operacao.executar(10, "3")     

def test_divide():
    operacao = Divisao()
    assert operacao.executar(8, 2) == 4

def test_divide_não_numeral():
    operacao = Divisao()
    with pytest.raises(ValueError, match="Parâmetros inválidos para divisão."):
        operacao.executar(10, "3")     

def test_divisao_por_zero():
    operacao = Divisao()
    with pytest.raises(ValueError, match="Divisão por zero não permitida."):
        operacao.executar(10, 0)
