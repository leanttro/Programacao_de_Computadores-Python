valor = 0
for i in range(3):
    valor = float(input("Digite um número: "))
    print(valor)
    print("Fim")

sexo = ""
idade = 0
quantMulheres = 0
quantHomens = 0

for i in range(0,5):
    sexo = input("Digite o sexo (M) ou (H)")
    idade = int(input("Digite a idade: "))

    if(sexo=="M" or sexo=="m"):
         quantMulheres+=1
    elif(sexo=="H" or sexo=="h"):
         quantHomens+=1
    
print("A quantidade de mulheres é", quantMulheres)
print("A quantidade de homens é", quantHomens)

maiornota = 0
contador = 0
nota = 0
somanotas = 0

while contador < 3:
     nota = float(input("Digita a nota: "))
     somanotas = somanotas + nota

     contador+=1

     if(contador==1):
            maiornota = nota
     else:
          if(nota>maiornota):
            maiornota = nota
    
media = somanotas / contador
     
print("A maior nota é ",maiornota)
print("A média de notas é",media)
print("Fim")

sexo = ""
idade = 0
quantMulheres = 0
valoridade = 0

for i in range(0,5):
    sexo = input("Digite o sexo (M) ou (H)")
    idade = int(input("Digite a idade: "))

    if(sexo =="M" or sexo =="m"):
        quantMulheres+=1
    
    valoridade+= idade

mediaidade = valoridade/quantMulheres

print("A quantidade de mulheres é ", quantMulheres)
print("A média de idade é", mediaidade)




     
