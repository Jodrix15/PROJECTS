import sys

def suma(a, b):
    return a+b

args = sys.argv #nos devuelve una lista de strings

print(args)
print(suma(int(args[1]), int(args[2])))




