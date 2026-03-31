# 🐍 Python Fundamentals: Variáveis e Tipos de Dados

Este repositório faz parte dos meus estudos de Python, focando na base sólida da linguagem: como nomear, declarar e manipular dados de forma eficiente.

---

## 📝 Convenções de Nomenclatura (Naming Style)

Em Python, seguimos a convenção **snake_case** (palavras em minúsculo separadas por underline). 

| Status | Exemplos Válidos | Exemplos Inválidos |
| :--- | :--- | :--- |
| **Padrão** | `first_name`, `last_name` | `first-name` (hífen não permitido) |
| **Numérico** | `year_2026`, `num1` | `1num` (não pode começar com número) |
| **Especial** | `_if` (uso de palavras reservadas) | `first@name` (caracteres especiais) |

---

## 🚀 Conceitos Chave

### 1. Atribuição e Variáveis
O sinal `=` é um **operador de atribuição**, utilizado para armazenar dados na memória.
* **Declaração Simples:** `age = 21`
* **Atribuição Múltipla:** `nome, idade, pais = "Dev", 21, "Brasil"`

### 2. Funções Integradas (Built-in)
As ferramentas essenciais para manipulação inicial:
* `print()`: Exibe dados no console (aceita múltiplos argumentos).
* `len()`: Retorna o comprimento de uma string ou coleção.
* `input()`: Captura dados inseridos pelo usuário.
* `type()`: Identifica o tipo de dado de uma variável.

---

## 📊 Tipos de Dados (Data Types)

| Tipo | Descrição | Exemplo |
| :--- | :--- | :--- |
| **str** | Strings (Cadeias de caracteres) | `'Python'`, `"Data"` |
| **int** | Números inteiros | `10`, `-5` |
| **float** | Números decimais | `9.81`, `3.14` |
| **bool** | Valores lógicos | `True`, `False` |
| **list** | Coleção ordenada e mutável | `[1, 2, 3]` |
| **dict** | Dicionário (Chave-Valor) | `{'id': 1}` |

---

## 🔄 Casting (Conversão de Tipos)

O **Casting** é o processo de converter um tipo de dado em outro. É fundamental para garantir que operações matemáticas ou concatenações funcionem corretamente.

```python
# String para Float e depois para Int
num_str = '10.6'
num_float = float(num_str)  # Resultado: 10.6
num_int = int(num_float)    # Resultado: 10 (trunca o valor)

# Int para String (Útil para concatenar textos)
idade = 21
mensagem = "Eu tenho " + str(idade) + " anos."