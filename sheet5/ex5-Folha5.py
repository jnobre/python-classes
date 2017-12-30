
def printFuncao():
	global c #global
	b=5 #local
	c=6
	teste = 1
	print("a dentro da funcao: ", a) 
	print("b dentro da funcao: ", b) 
	print("c dentro da funcao: ", c)
a=1
b=2
c=3

print("a fora da funcao: ", a) 
print("b fora da funcao: ", b) 
print("c fora da funcao: ", c) 
printFuncao()
print2()
print("a fora da funcao: ", a)
print("b fora da funcao: ", b)
print("c fora da funcao: ", c)
