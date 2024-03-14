'''Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer
entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;'''

frase = str(input('Digite uma frase: ')).strip()

# Fatia a string e mostra os caracteres do início para o final [::-1] pulando de um em um
print('↓↑' * 10)
print(frase[::-1])
print('↓↑' * 10)
print(frase.upper().replace(' ', '')[::-1])