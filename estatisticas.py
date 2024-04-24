import string
import numpy as np

# Função para verificar se uma senha parece ser uma tag HTML ou div
def is_html_tag(password):
    html_chars = {'<', '>', '/', '='}  # Caracteres comuns em tags HTML
    return any(char in html_chars for char in password)

# Abra o arquivo ROCKYOU!
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
    passwords = file.readlines()

# Remova espaços em branco e caracteres de nova linha
passwords = [password.strip() for password in passwords]

# Filtrar senhas que parecem ser HTML ou divs
valid_passwords = []
for password in passwords:
    if not is_html_tag(password):
        valid_passwords.append(password)

# Calculando o comprimento médio das senhas válidas
total_valid_passwords = len(valid_passwords)
total_valid_length = sum(len(password) for password in valid_passwords)
average_valid_length = total_valid_length / total_valid_passwords

# Calculando a mediana do comprimento das senhas válidas
median_valid_length = np.median([len(password) for password in valid_passwords])

# Calculando a variância do comprimento das senhas válidas
variance_valid_length = np.var([len(password) for password in valid_passwords])

# Calculando o desvio padrão do comprimento das senhas válidas
std_dev_valid_length = np.std([len(password) for password in valid_passwords])

print("Comprimento médio das senhas válidas:", average_valid_length)
print("Mediana do comprimento das senhas válidas:", median_valid_length)
print("Variância do comprimento das senhas válidas:", variance_valid_length)
print("Desvio padrão do comprimento das senhas válidas:", std_dev_valid_length)





