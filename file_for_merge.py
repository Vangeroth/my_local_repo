lista = [1,2,3,4,5,6]

a = lambda x: '+'.join([str(item) for item in x])
print a(lista)
