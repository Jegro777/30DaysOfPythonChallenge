# ==========================================
# FUNDAMENTOS DE PYTHON: VARIÁVEIS E TIPOS
# ==========================================

# 1. DECLARAÇÃO DE VARIÁVEIS (SNAKE_CASE)
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# 2. ATRIBUÍÇÃO MÚLTIPLA EM UMA LINHA
name, job, is_student = 'Dev', 'Student', True

# 3. EXIBIÇÃO E MANIPULAÇÃO (PRINT & LEN)
print('--- Informações Básicas ---')
print('Nome:', first_name, '| Comprimento:', len(first_name))
print('País:', country)
print('Skills:', skills)
print('Dicionário completo:', person_info)

# 4. ENTRADA DE USUÁRIO (INPUT)
# Descomente as linhas abaixo para testar a entrada de dados:
# user_name = input('Qual o seu nome: ')
# user_age = input('Qual a sua idade: ')

# 5. VERIFICAÇÃO DE TIPOS (TYPE)
print('\n--- Verificação de Tipos ---')
print(type('Asabeneh'))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3]))           # list
print(type({'key': 'value'}))    # dict
print(type((1, 2)))              # tuple

# 6. CONVERSÃO DE TIPOS (CASTING)
print('\n--- Exemplos de Casting ---')

# String para Float e Int
num_str = '10.6'
num_float = float(num_str)       # 10.6
num_int = int(num_float)         # 10 (converte removendo os decimais)
print(f'String: {num_str} | Float: {num_float} | Int: {num_int}')

# Int para String
gravity = 10
gravity_str = str(gravity)       # '10'

# String para Lista
word = 'Python'
word_list = list(word)           # ['P', 'y', 't', 'h', 'o', 'n']
print(f'Palavra: {word} | Lista: {word_list}')

# ==========================================
# FIM DO SCRIPT
# ==========================================