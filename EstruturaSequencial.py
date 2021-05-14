'''

#Quetao 1
print("Alo mundo")

'''
import math

'''
#Questao2

Numero = int(input("digite um numero: "))
print("O numero digitado foi ",Numero)

'''
'''
#Questao3

PrimeiroNumero = int(input("Digite o primeiro numero:"))
SegundoNumero = int(input("Digite o segundo numero: "))
Soma = PrimeiroNumero + SegundoNumero
print("A soma dos dois numeros e: ",Soma)

'''
'''
#Questao4
lista = []
i = 0
while (i<4):
    a = int(input("digite o valor da nota ",))
    lista.append(a)
    i+=1

soma = sum(lista)
media = soma/4
print("A media deste aluno e: ",media)

'''
'''
#Questao 5

Metros = float(input("Informe o valor em metros a ser convertido: "))
Transforma = Metros*100
print("O valor em centimetro e: ",Transforma,'cm')

'''
'''
#Questao 6

RaioDoCirculo = float(input("informe o raio do circulo: "))
Area = 2*3.14*RaioDoCirculo

print("O valor do raio do circulo e: ", Area)

'''
'''
#Questao 7

LadoDoQuadrado = float(input("informe o lado do quadrado: "))
AreaDoQuadrado = LadoDoQuadrado*LadoDoQuadrado
DobloDaArea = AreaDoQuadrado*2
print("A area do quadrado e: ", AreaDoQuadrado)
print("O doblo desta area e: ", DobloDaArea)

'''
'''
#Questao 8

GanhoHora= float(input("informe o seu ganho por hr em reais"))
HorasTrabalhadas = float(input("informe as horas trabalhadas no mes"))
Salario = GanhoHora*HorasTrabalhadas
print("Seu salario mensal e: ", Salario)

'''
'''
#Questao 9

TempFahre = float(input("Informe a temperatura em F: "))
Conversao = 5((TempFahre-32)/9)
print("O valor da temperatura em Celcios e :", Conversao)

'''
'''
#Questao 10

TempCel = float(input("Informe a temperatura em C: "))
Conversao = (TempCel *9/5)+32
print("O valor da temperatura em Fahrenheit e :", Conversao)

'''
'''
#Questao 11

NumeroInt1 = int(input("informe o primeiro numero inteiro: "))
NumeroInt2 = int(input("informe o segundo numero inteiro: "))
NumeroReal = float(input("Informe o numero real: "))
LetraA = (NumeroInt1*2)*(NumeroInt2/2)
LetraB = (NumeroInt1*3)+NumeroReal
LetraC = math.pow(NumeroReal,3)
print("Letra (A): ", LetraA)
print("Letra (B)", LetraB)
print("Letra (C)", LetraC)

'''
'''
#Questao 12

AlturaDaPessoa = float(input("informe a altura da pessoa em metros: "))
PesoIdeal =(72.7*AlturaDaPessoa)-58
print("O peso ideial desta pessoa e: ",PesoIdeal)

'''
'''
#Questao 13

AlturaDaPessoa = float(input("informe a altura da pessoa em metros: "))
PesoIdealH =(72.7*AlturaDaPessoa)-58
PesoIdealM =(62.1*AlturaDaPessoa)-44.7
print("O peso ideial desta pessoa e: ")
print(PesoIdealH, "Para Homens")
print(PesoIdealM, "Para Mulheres")

'''
'''
#Quetao 14

PesoDoPeixe = float(input("Informe o peso do peixe: "))
if (PesoDoPeixe > 50):
    Sobra = PesoDoPeixe - 50
    Multa = Sobra * 4
    print("O peixe excedeu o limite do peso a multa e de: ",Multa)
else:
    print("esse peso nao gera multa")

'''
'''
#Questao 15

GanhoHora = float(input("INforme o ganho por hora em reais: "))
HorasMes =float(input("HOras trabalhadas no mes: "))
SalarioBruto = GanhoHora*HorasMes
INSS = (SalarioBruto*8)/100
Sind = (SalarioBruto*5)/100
ImpostoRenda = (SalarioBruto*11)/100
SalarioLiquido = SalarioBruto-(INSS+Sind+ImpostoRenda)
print("Letra (a) ",SalarioBruto)
print("Letra (b)", INSS)
print("letra (c)",Sind)
print("letra (d)", SalarioLiquido)

'''
'''
#Quetao 16
AreaPintada = float(input("informe a area em metros quadrados "))
Latas = AreaPintada/18
Preço = Latas*80
print("o numero de latas para utilizar e: ", Latas)
print("o valor pago e ", Preço)

'''
'''
#Questao 17
pass

'''
'''
#Questao 18
Arquivo = float(input("informe o tamanho do arquivo para dowload "))
Velocidade = float(input("informe a velociadade da internet em mbs/s "))

Dowload = Arquivo/Velocidade
print("o tempo estimado dop dowload e de: ", Dowload)
'''