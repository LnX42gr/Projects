from math import pow, sqrt

n = float(input("Digite o valor do cateto adjacente: "))
n2 = float(input("Digite o valor do cateto oposto: "))
ch= pow(n, 2) + pow(n2, 2)
hp=sqrt(ch)
print("Se o valor do cateto adjacente é {} e o valor do cateto oposto é {}, então a hipotenusa vale {:.2}".format(n, n2, hp))
