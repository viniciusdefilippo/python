"""
Para melhor ilustrar as estruturas condicionais, será proposto
um clássico problema para identificar triângulos. Além das condicionais,
também são apresentados no mesmo problema, alguns dos operadores lógicos
mais utilizados como operador and e o operador or.

Apenas para relembrar,

Para ser considerado como um triângulo, o comprimento de cada um dos
lados de um triângulo deve ser menor que a soma dos comprimentos
dos outros dois lados. Sendo assim:

- O triângulo equilátero possui os comprimentos dos três lados iguais;
- O triângulo isósceles possui os comprimentos de dois lados iguais;
- O triângulo escaleno possui os comprimentos de seus três lados diferentes.

"""

ladoA = float(input('Digite o primeiro lado: '))
ladoB = float(input('Digite o segundo lado: '))
ladoC = float(input('Digite o terceiro lado: '))
if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):
    if (ladoA == ladoB) and (ladoA == ladoC):
        print('Equilátero')
    elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não é triângulo!')
