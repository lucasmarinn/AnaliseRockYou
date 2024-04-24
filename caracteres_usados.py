from collections import Counter
import string

# Função para verificar se uma senha parece ser uma tag HTML ou div
def is_html_tag(password):
    html_chars = {'<', '>', '/', '='}  # Caracteres comuns em tags HTML
    return any(char in html_chars for char in password)

# Abra o arquivo ROCKYOU!
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
    passwords = file.readlines()

# Remova espaços em branco e caracteres de nova linha e filtre tags HTML ou divs
passwords = [password.strip() for password in passwords if not is_html_tag(password)]

# Junte todas as senhas em uma única string
all_passwords = ''.join(passwords)

# Calcule a frequência de caracteres
char_frequency = Counter(all_passwords)

# Separe letras, números e caracteres especiais
letters = [char for char in all_passwords if char.isalpha()]
numbers = [char for char in all_passwords if char.isdigit()]
special_chars = [char for char in all_passwords if not char.isalnum()]

# Calcule a frequência de cada categoria de caracteres
letter_frequency = Counter(letters)
number_frequency = Counter(numbers)
special_char_frequency = Counter(special_chars)

# Selecione os três caracteres mais usados de cada categoria
top_letters = letter_frequency.most_common(3)
top_numbers = number_frequency.most_common(3)
top_special_chars = special_char_frequency.most_common(3)

# Imprima os resultados
print("Três letras mais usadas:")
for char, freq in top_letters:
    print(f"Caractere: {char}, Frequência: {freq}")

print("\nTrês números mais usados:")
for char, freq in top_numbers:
    print(f"Caractere: {char}, Frequência: {freq}")

print("\nTrês caracteres especiais mais usados:")
for char, freq in top_special_chars:
    print(f"Caractere: {char}, Frequência: {freq}")
