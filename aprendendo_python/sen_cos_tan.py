import math 
an = float(input("Digite o valor do angulo"))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print("O angulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}".format(an, seno, cos, tan))
