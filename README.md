# 📌 Calculadora com Padrão Strategy em Python.

Este projeto implementa uma **calculadora em Python** aplicando o **padrão de projeto Strategy**, com testes automatizados utilizando **pytest** e gerenciamento de dependências com **Poetry**.

---

## 📌 Objetivos do Projeto
- Demonstrar o uso do **padrão Strategy** para encapsular operações matemáticas.
- Organizar o projeto de forma **modular e profissional**.
- Aplicar boas práticas de desenvolvimento com **testes unitários, de integração e funcionais**.
- Utilizar **Poetry** como ferramenta de gerenciamento de dependências e ambiente virtual.

---

## 📌 O que é o Padrão Strategy?

O **padrão Strategy** é um **Design Pattern comportamental** que permite **definir uma família de algoritmos**, encapsulá-los em classes separadas e torná-los **intercambiáveis**.  

📌 Na prática, isso significa que cada operação matemática (Soma, Subtração, Multiplicação, Divisão) é representada por uma **estratégia** diferente, mas todas compartilham a mesma interface.  

Assim, a **Calculadora** pode executar diferentes operações sem precisar saber os detalhes de implementação, apenas recebendo a estratégia apropriada.

📌 Vantagens do Strategy:
- Código mais organizado e extensível.
- Fácil adicionar novas operações sem modificar a lógica existente (**OCP – Open/Closed Principle**).
- Reuso de código e maior clareza arquitetural.

---

## 📌 Estrutura do Projeto

```
calculadora/
├── src
|    └── calculadora/       # Código fonte
│          ├── init.py
│          ├── Calculadora.py
│          ├── Divisão.py
│          ├── main.py
│          ├── Multiplicacao.py
│          ├── Operacao.py
│          ├── Soma.py
│          └── Subtracao.py
├── tests/                  # Testes automatizados com pytest
│     ├── test_unitario.py
│     ├── test_integracao.py
│     └── test_funcional.py
├── poetry.lock             # Arquivo de dependências
├── pyproject.toml          # Configuração do Poetry
└── README.md               # Documentação
```

---

## 📌 Instalação e Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/jcarlossc/calculadora-python-pytest.git
cd calculadora-python-pytest
```
### 2. Instalar dependências com Poetry
```
poetry install
```
### 3. Executar projeto
```
poetry run calc
```

---

## 📌 Testes com Pytest
Tipos de testes implementados:

* Unitário → Testa cada operação isoladamente.
* Integração → Testa a interação da Calculadora com diferentes estratégias.
* Funcional → Simula o uso real, com diferentes entradas e operações.

Rodar os testes:
```
poetry run pytest -v 
```

---

## 📌 Tecnologias Utilizadas

* Python 3.13+
* Poetry → gerenciamento de dependências e empacotamento
* Pytest → testes automatizados
* Padrão de Projeto Strategy

---

## 📌 Conclusão

Este projeto demonstra como aplicar o padrão Strategy em Python de forma prática, integrando boas práticas como testes automatizados com pytest e gerenciamento de dependências com Poetry.

É uma base simples, mas poderosa, para expandir com:
Novas operações matemáticas,
Interface gráfica (Tkinter/PyQt),
API com Flask/FastAPI,
Histórico de operações usando Command Pattern.

---

## 📌 Contribuições
Se quiser contribuir:
1. Faça um fork deste repositório
2. Crie uma branch para sua feature ou correção (git checkout -b minha-feature)
3. Faça commits descritos claramente
4. Submeta um Pull Request

---

## 📌 Licença
Este projeto está licenciado sob a MIT License.

---

## 📌 Contatos
📌Autor: Carlos da Costa<br>
📌Recife, PE - Brasil<br>
📌Telefone: +55 81 99712 9140<br>
📌Telegram: @jcarlossc<br>
📌Blogger linguagem R: [https://informaticus77-r.blogspot.com/](https://informaticus77-r.blogspot.com/)<br>
📌Blogger linguagem Python: [https://informaticus77-python.blogspot.com/](https://informaticus77-python.blogspot.com/)<br>
📌Email: jcarlossc1977@gmail.com<br>
📌Portfólio em construção: https://portfolio-carlos-costa.netlify.app/<br>
📌LinkedIn: https://www.linkedin.com/in/carlos-da-costa-669252149/<br>
📌GitHub: https://github.com/jcarlossc<br>
📌Kaggle: https://www.kaggle.com/jcarlossc/  
📌Twitter/X: https://x.com/jcarlossc1977
