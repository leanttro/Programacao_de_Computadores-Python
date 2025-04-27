idade = [85,90,15,18,34,53] # lista de idades
print(idade[0]) # mostra o primeiro item
print(idade[5]) # mostra o sexto item

meuDici = {"nome": "João", "idade": 25, "email":"joão@gmail"} # dicionário
meuDici.pop("email") # remove o email

print(meuDici) # mostra o dicionário

nomes = ["Ana", "Fernanda", "Maria"] # lista de nomes
nomes.append("Lucas") # adiciona Lucas
print(nomes) # mostra os nomes

animais = ["Cachorro", "Gato", "Homens"] # lista de animais
animais.append("Rato") # adiciona Rato
animais.append("Jacaré") # adiciona Jacaré

animais2 = [] # nova lista

for i in range(3): # repete 3x
    animais2.append(animais[i+1]) # adiciona animal da frente

print(animais2) # mostra nova lista

nomes = ["Ana", "Fernanda", "Maria"] # lista de nomes
nomes.pop() # remove o último
print(nomes) # mostra nomes

frutas = ["Limão","Banana","Morango"] # lista de frutas
frutas.append("Abacaxi") # adiciona Abacaxi
frutas.append("Abacate") # adiciona Abacate

frutas2=[] # nova lista
for i in range(2): # repete 2x
    frutas.pop() # remove o último
    frutas2.append(frutas[i]) # adiciona frutas

print(frutas2) # mostra nova lista

frutas = ["Limão","Banana","Morango"] # lista de frutas
frutas.append("Abacaxi") # adiciona Abacaxi
for i in range (2): # repete 2x
    frutas.pop() # remove o último

print(frutas) # mostra frutas
