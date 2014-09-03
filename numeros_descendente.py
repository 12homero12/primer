lista=[]
for i in range(20):
	n=input()
	lista1=[n]
	lista=lista+lista1
	lista.sort(reverse=True)
print(lista)