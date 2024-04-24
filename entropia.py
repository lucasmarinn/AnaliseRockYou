import math
from collections import Counter
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

# Junte todas as senhas em uma única string, excluindo possíveis tags HTML ou divs
all_passwords = ''.join(password for password in passwords if not is_html_tag(password))

# Calcule a frequência de cada caractere
char_frequency = Counter(all_passwords)

# Calcule a probabilidade de cada caractere
total_chars = len(all_passwords)
char_probabilities = {char: freq / total_chars for char, freq in char_frequency.items()}

# Calcule a entropia das senhas
entropy = -sum(prob * math.log2(prob) for prob in char_probabilities.values())

print(f"A entropia das senhas é: {entropy}")

