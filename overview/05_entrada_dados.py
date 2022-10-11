# entrada de texto
nome = input("Qual é o seu nome? ")
print(f"Hello {nome}")

# entrada de número inteiro
numero = int(input("Digite um número: "))
print(f"O dobro do número informado foi {2 * numero}")

# Cálculo da média de três valores
# necessário conversão de String para float
# ou seja, converter texto para decimal
a = float(input("Entre com o primeiro número: "))
b = float(input("Entre com o segundo número: "))
c = float(input("Entre com o terceiro número: "))
media = (a + b + c)/3
print(f"A média é: {media}")

# nesse exemplo é possivel digitar uma expressão
# matemática como por exemplo 2 * 5 + 4
# a expressão será avaliada e o resultado
# será exibido no console
exp = input("Entre com um a expressão matemática: ")
print("O resultado é:", eval(exp))
