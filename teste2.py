import math
vet=[]
for i in range(10):
    if i%2==0:
        calc=3**i+7*math.factorial(i)
        vet.append(calc)
    else:
        calc = 2**i+4*math.log(i)
        vet.append(round(calc,2))
print("A média dos elementos da lista é: ",round(sum(vet)/10,2))
print("A posição do maior elemento é: ",vet.index(max(vet))+1)
    