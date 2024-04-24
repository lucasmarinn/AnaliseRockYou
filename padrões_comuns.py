import re

# Função para verificar se uma senha parece ser uma tag HTML ou div
def is_html_tag(password):
    html_chars = {'<', '>', '/', '='}  # Caracteres comuns em tags HTML
    return any(char in html_chars for char in password)

# Abra o arquivo ROCKYOU!
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
    passwords = file.readlines()

# Remova espaços em branco e caracteres de nova linha
passwords = [password.strip() for password in passwords]

# Verifique cada senha para padrões comuns, excluindo possíveis tags HTML ou divs
common_patterns = []
for password in passwords:
    if not is_html_tag(password):  # Filtrar senhas que parecem ser HTML ou divs
        if re.search(r'(.)\1{2,}', password) or re.search(r'\d{4,}', password):
            common_patterns.append(password)

# Imprima os resultados
if common_patterns:
    print("Padrões comuns encontrados nas senhas:")
    for pattern in common_patterns[:10]:  # Imprimir os primeiros 10 padrões encontrados
        print(pattern)
else:
    print("Nenhum padrão comum encontrado nas senhas.")


