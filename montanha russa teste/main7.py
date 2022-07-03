#EXERCICIO DA MONTANHA RUSSA ACRESCENTANDO O VALOR DE UMA FOTO:

print("BEM VINDO A MONTANHA RUSSA FIREWHIP!!")
altura = int(input("Qual a sua altura = " ))
bil = 0
if altura >= 120:
    print("Ok. Você tem altura suficiente para andar.")
    idade = int(input("Qual a sua idade?"))
    if idade < 12:
        bil += 5
        print("O valor do seu bilhete é R$5.00")
    elif idade >= 18:
        bil += 12
        print("O valor do seu bilhete é R$12.00")
    else:
        bil += 7
        print("O valor do seu bilhete é R$7.00")
    foto = input("Você quer uma foto pelo adicional de R$ 3.00? Y ou N? = ")
    if foto == "Y":
        bil += 3
    print(f"Então o valor final do seu bilhete fica R${bil}")

else:
    print("Desculpe, você não tem altura suficiente para poder andar.")
 
