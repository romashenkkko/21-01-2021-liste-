lista1=[1, -2, 3, -8, 8, 5]
print('lista 1 este', lista1)
lista2=sorted(lista1)
print('lista 2 sortata este', lista2)
lista2.sort(reverse=True)
print('lista 3 sortata in ordine descrescator este', lista2)
print('lungimea listei', len(lista1))
print('elementul cel mai mare din lista este', max(lista1))
print('elementul cel mai mic din lista este', min(lista1))
lista4=lista1+([-111])
print('lista 4 noua formata', lista4)
lista5=lista1
lista5[2]=-222
print('lista 5 nou formata', lista5)
