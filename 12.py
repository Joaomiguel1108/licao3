salario = float(input("digite o valor do seu salario"))

aumento = (salario/100)*15
aumento_total = salario+aumento

desconto = (aumento_total/100)*8
desconto_total = desconto + aumento_total

print(salario)
print(aumento_total)
print(desconto_total)
