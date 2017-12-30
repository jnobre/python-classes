a = 10
b = 15
c = 25

def f(a):
	print("Dentro: a=", a) 
	b = 100 + a
	d=2*a 
	print("Dentro: b=", b) 
	print("Dentro: c=", c) 
	print("Dentro: d=", d) 
	return b + 10

print("Init:", "a: " + str(a), "b: " + str(b), "c: " + str(c))
c = f(b)
print("Fora: a = ", a)
print("Fora: b = ", b)
print("Fora: c = ", c)
print("Fora: d = ", d)
