# quest.1

# def saudação( nome ):
#     return (f"olá, {nome}! Sejá bem-vindo(a) au curso de lógica de programação.")
# print (saudação (input("qual seu nome? ")))

# quest.2

# def número (x):
#     if x % 2 == 0 :
#         return ("esse número é par")
#     else:
#         return ("esse número é impar")
# print (número (int(input("digite um número: "))))

# quest.3

# x= int(input("digite um número: "))
# y= int(input("digite outro número: "))

# if x > y :
#     print (f"{x} é maior que {y}")
# elif x < y :
#     print (f"{x} é menor que {y}")
# else:
#     print ("esses números são iguais")

# quest.4

# nmr= int(input("digite um número inteiro: "))
# for i in range (11):
#     resul= nmr*i
#     print(f"{nmr} x {i} = {resul}")

# quest.5

# cont= 10
# while cont >= 1:
#     print(cont)
#     cont -= 1
# print("Explosão!!!!!!!!!!!")

# quest.6

# def notas (a,b,c,d):
#     media = (a+b+c+d)/2
#     return (f"A média é {media}")
# print(notas(2,4,5,6))

# quest.7

# def fatorial(x):
#     cont=1
#     f= x
#     while f >= 1:
#         cont *= f
#         f -= 1
#     return (f"O fatorial de {x} é {cont}")
# print(fatorial(int(input("Digite um número: "))))

# quest.8

# def palavra(x):
#     vogais=["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     cont=0
#     for c in x:
#         if c in vogais:
#             cont += 1
#     return (f"A palavra {x} tem {cont} vogais")
# print(palavra (input("Diga uma palavra: ")))   

# quest.10

# nmr=int(input("Digite um número: "))
# soma = 0
# for i in range(0,nmr):
#     if i % 2 == 0:
#         soma += i
# print(f"A soma dos número pares é {soma}")

# ques.11

# def soma(x,y):
#     return (x + y)
# print(soma(2,3))

# qust.12

# def eh_primo(numero):
#     if numero < 2:
#         return False
#     if numero == 2:
#         return True
#     if numero % 2 == 0:
#         return False
#     for i in range(3, int(numero**0.5) + 1, 2):
#         if numero % i == 0:
#             return False 
#     return True  
# num = int(input("Digite um número inteiro: "))
# if eh_primo(num):
#     print(f"{num} é um número primo.")
# else:
#     print(f"{num} não é um número primo.")

#questao 13

# def inverter_palavra(palavra):
#   return palavra[::-1]
# palavra_digitada = input("Digite uma palavra para ser invertida: ")
# palavra_invertida = inverter_palavra(palavra_digitada)
# print(f"A palavra invertida é: {palavra_invertida}")

#questao 14

# impar = 0
# par = 0
# for i in range(10):
#     n = int(input(f"digite o {i + 1}º numero: "))
#     if n % 2 == 0:
#         par += 1
#     else:
#         impar += 1
# print(f"a quantidade de numero pares é {par}")
# print(f"a quantidade de numero impares é {impar}")

#questao 15

# def calcular_fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1 
#         for _ in range(2, n + 1):
#             proximo_fib = a + b
#             a = b
#             b = proximo_fib
#         return b 
# numero_usuario = int(input("Por favor, digite um número para encontrar seu termo de Fibonacci: "))
# resultado = calcular_fibonacci(numero_usuario)
# print(f"O termo de Fibonacci para o número {numero_usuario} é: {resultado}")



    
        
 





