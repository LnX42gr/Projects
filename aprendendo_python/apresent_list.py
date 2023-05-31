import random 
n = input("Primeiro aluno: ")
n1 = input("Segundo aluno: ")
n2 = input("Terceiro aluno: ")
n3 = input("Quarto aluno: ")
lista = [n, n1, n2, n3]
random.shuffle(lista)
print("A ordem será {}".format(lista))
