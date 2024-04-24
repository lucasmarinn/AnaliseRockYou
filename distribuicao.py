import string
import numpy as np
import pandas as pd

# Função para verificar se uma senha parece ser uma tag HTML ou div
def is_html_tag(password):
    html_chars = {'<', '>', '/', '='}  # Caracteres comuns em tags HTML
    return any(char in html_chars for char in password)

# Abra o arquivo ROCKYOU!
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
    passwords = file.readlines()

# Remova espaços em branco e caracteres de nova linha
passwords = [password.strip() for password in passwords]

# Calcular a distribuição de frequência dos comprimentos das senhas
password_length_freq = {}
for password in passwords:
    if not is_html_tag(password):  # Filtrar senhas que parecem ser HTML ou divs
        length = len(password)
        if length in password_length_freq:
            password_length_freq[length] += 1
        else:
            password_length_freq[length] = 1

# Converter os resultados para um DataFrame do Pandas
df = pd.DataFrame(list(password_length_freq.items()), columns=['Comprimento', 'Frequência'])

# Exportar para um arquivo do Excel
df.to_excel('distribuicao_senhas.xlsx', index=False)










