idade = [85,90,15,18,34,53]
print(idade[0])
print(idade[5])

meuDici = {"nome": "João", "idade": 25, "email":"joão@gmail"}
meuDici.pop("email")

print(meuDici)

nomes = ["Ana", "Fernanda", "Maria"]
nomes.append("Lucas")
print(nomes)

animais = ["Cachorro", "Gato", "Homens"]
animais.append("Rato")
animais.append("Jacaré")

animais2 = []

for i in range(3):
    animais2.append(animais[i+1])

print(animais2)

nomes = ["Ana", "Fernanda", "Maria"]
nomes.pop()
print(nomes)

frutas = ["Limão","Banana","Morango"]
frutas.append("Abacaxi")
frutas.append("Abacate")

frutas2=[]
for i in range(2):
    frutas.pop()
    frutas2.append(frutas[i])

print(frutas2)

frutas = ["Limão","Banana","Morango"]
frutas.append("Abacaxi")
for i in range (2):
    frutas.pop()
print(frutas)

