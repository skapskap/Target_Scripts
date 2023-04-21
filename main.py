"""Questão 1"""

index = 13
sum = 0
k = 0

while k < index:
    k += 1
    sum += k

print(sum) # Valor 91

"""Questão 2"""

def fibonacci(num):
    a = 0
    b = 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False


numero = int(input("Qual o número para checar se está na Fibonacci?"))
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

"""Questão 3"""

# a) Sequência de números ímpares
# b) Sequência de números elevados ao quadrado, onde o resultado anterior é elevado ao quadrado em seguida.
# c) Sequência de números inteiros elevados ao quadrado.
# d) Sequência de números pares elevados ao quadrado.
# e) Sequência de Fibonacci.
# f) Sequência de números que começam com a letra "D", então o próximo número seria 200.

"""Questão 4"""

distancia = 100
carro_speed = 110
caminhao_speed = 80
pedagio = 5

x = (carro_speed / (carro_speed + caminhao_speed) * distancia)
print(x)

y = distancia - x
print(y)

tempo_caminhao = (y / caminhao_speed) + ((pedagio/60) * 2)

tempo_carro = x / carro_speed

if tempo_carro < tempo_caminhao:
    print("O carro vai estar mais perto de Ribeirão Preto quando se cruzarem")
else:
    print("O caminhão vai estar mais perto de Ribeirão Preto quando se cruzarem")

# Utilizei média ponderada de velocidades para calcular a distância percorrida pelo carro
# até encontrar o caminhão e a partir daí foi fácil definir a distância percorrida pelo caminhão
# e o tempo que os dois veículos levariam a distância x e y (Ribeirão Preto - Franca e Franca - Ribeirão Preto).

"""Questão 5"""

def string_invertida(inp_string):
    nova_string = []
    indice = len(inp_string)
    while indice:
        indice -= 1
        nova_string.append(inp_string[indice])
    return "".join(nova_string)

nova_string = string_invertida(input("Qual você quer que seja a string pra inverter?"))
print(nova_string)