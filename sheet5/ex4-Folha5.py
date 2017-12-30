def calculaOrdenado(base, irs=0.30, ss=0.10, outros=0,verificaDesconto=True):
      """ Calcula o ordenado liquido (apos descontos)
      Calcula o ordenado liquido dados o valor do ordenado bruto
      (base) e duas taxas de descontos, a do irs (irs), a da seguranca
      social (ss), e ainda o montante de outros descontos (outros)
      Requires: base é float, base > 0, 0<=irs<=1, 0<=ss<=1
      Ensures: um float com o valor do ordenado liquido
      """
      if verificaDesconto == True:
      	descontos = base * irs + base * ss + outros
      else:
      	descontos = 0
      return base - descontos



print(calculaOrdenado(1000.0))
print(calculaOrdenado(1000.0, 0, 0, 200))
print(calculaOrdenado(1000.0, outros = 200))
print(calculaOrdenado(1000.0, 0.20, outros = 100))
print(calculaOrdenado(1000.0, ss=0.20, outros = 100))
#print(calculaOrdenado(1000.0, irs=0.20, 100)) #Error
 
