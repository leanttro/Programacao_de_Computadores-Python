# OPERADORES LÓGICOS 
a = 6
b = 28

c = a + b # soma
d = a * b # multiplicação
e = a / b # divisão
f = a % 2 # módulo (resto)

print("O valor de c é ", c)
print("O valor de d é ", d)
print("O valor de e é ", e)
print("O valor de d f ", f)
#Imprime o texto entre aspas e a variável definida após a vírgula sem aspas

# OPERADORES COMPARATIVOS 
x = 11
y = 18
z = 11

x > y # false = > maior que
y < x # false = < menor que

x >= y # false
y >= x # true

x == z # true
x == y # false

x != z # false

# IF / ELSE

idade = int(input("Insira a sua idade: ")) #Solicita uma variável para o usuário
if idade >= 18: #SE a idade for maior ou igual a 18
    print("Você é maior de idade. ")
else: #SENÃO
    print("Você é menor de idade. ")

# AND - Adiciona uma condição a uma IF 

idade = int(input("Digite a sua idade: "))
if idade >= 18 and idade <= 30:
    print("A sua idade está entre 18 e 30 anos.")

else: 
   print("A sua idade não está entre 18 e 30 anos")
   print ("Fim")

# OR - Restringe uma condição a uma IF 

idade = int(input("Digite a sua idade: "))
if idade < 18 or idade > 60:
    print("Você ganhou um brinde. :) ")
else:
    print("Você não ganhou um brinde :( )")
    print("Fim")