hora = float(input("quantas horas foram trabalhadas?"))
extra = float(input("quantas horas extras foram trabalhadas?"))


hora_extra = extra*15

horas = hora*10

horas_totais = horas+hora_extra

desconto = (horas_totais/100)*10
salario = horas_totais+desconto

print(f"seu salario é {salario} reais")
