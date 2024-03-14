'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele
calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência 
ou pode ser previamente definido no código;'''

escolha = int(input('Digite um valor: ')) # Entrada de dados

# Sequência de Fibonacci (Lógica)

f1 = 0  # Variável Fibonacci 1 (Digito atual)
f2 = 1  # Variável Fibonacci 2 (Digito seguinte)

antigo_f1 = 0 # Variável temporária (Utilizada no cálculo como dígito anterior ao atual)

pertence = False # Pertence começa como False para se a escolha do usuário pertencer, a var receber True.

# Enquanto o digito atual for menor ou igual a escolha do usuário:
while f1 <= escolha:
    if f1 == escolha: # Se o dígito atual for igual à escolha do user:
        pertence = True # Pertence se torna true e o laço acaba
        break
    
    '''O próximo dígito (f3) da sequência de Fibonacci é a soma do
    dígito atual (f1) com o dígito anterior (antigo_f1)''' 
    print('\033[1;31m',f1, '\033[m', end='\033[1;33m → \033[m')
    
    antigo_f1 = f1 # Essa variável recebe o valor do digito atual para guarda-lá 
    f1 = f2 # f1 recebe o valor do dígito seguinte para somar com o anterior
    f2 = f1 + antigo_f1  

print('\033[1;33m FIM! \033[m')

# Se pertencer:
if pertence:
    print(f'O número {escolha} PERTENCE à sequência de Fibonacci.')
# Senão:
else:
    print(f'O número {escolha} NÃO PERTENCE à sequência de Fibonacci')



