'''
#Questao 1
FirstNumber = float(input("Escreva o primeiro numero "))
SecundNumber = float(input("Escreva o segundo numero "))
if(FirstNumber > SecundNumber):
    print("O primeiro numero e maior que o segundo ")
elif(FirstNumber < SecundNumber):
    print("O segundo numero e maior que o primeiro ")

else:
    print("Os dois numeros sao iguais ")

'''
import math

'''
#Questao 2

Valor = float(input("informe um valor "))
if(Valor > 0):
    print("positivo")
elif(Valor < 0):
    print("negativo ")
else:
    print("neutro")

'''
'''
#Questao 3

Letra = str(input("Informe F para feminino e M para masculino "))
Letra =Letra.upper()
if(Letra == 'F'):
    print("Feminino")
elif(Letra == 'M'):
    print("Masculino")
else:
    print("invalido")

'''
'''
#Questao 4

Letra = str(input("informe uma letra "))
Letra = Letra.upper()

if (Letra == 'A' or Letra =='E' or Letra =='I' or Letra == 'O' or Letra == 'U'):
    print("E uma vogal")

else:
    print("E uma consoante ")
'''
'''
#Questao 5
PrimeiraNota = float(input("digite a primeira nota "))
SegundaNota = float(input("digite a segunda nota "))
Media = (PrimeiraNota+SegundaNota)/2

if (7<=Media<10):
    print("Aprovado")
elif(Media < 7):
    print("Reprovado")
elif(Media == 10):
    print("Aprovado com distinçao")
'''
'''
#Questao 6
Primeiro =float(input("digite o primeiro numero "))
Segundo = float(input("digite o segundo numero "))
Terceiro =float(input("digite o terceiro numero "))
if(Primeiro > Segundo and Primeiro >Terceiro):
    print("o maior numero e: ", Primeiro)
elif(Segundo > Primeiro and Segundo > Terceiro):
    print("o maior numero e: ", Segundo)
elif(Terceiro > Primeiro and Terceiro > Segundo):
    print("o maior numero e: ",Terceiro)

'''
'''
#Questao 7
a = float(input("Digite um numero "))
b = float(input("Digite um numero "))
c = float(input("Digite um numero "))
if(a > b and a > c):
    print("o maior numero e: ", a)
    if(b > c ):
        print("O menor numero e: ", c)
    elif(c > b):
        print(("o menor numero e: ", b))

elif(b > a and b > c):
    print("o maior numero e: ", b)
    if(a > c):
        print("O menor numero e: ", c)
    elif(c > a):
        print("O menor numero e: ", a)
elif(c > a and c > b):
    print("o maior numero e: ",c)
    if(a > b):
        print("O menor numero e: ",b)
    elif(b > a):
        print("O menor numero e: ", a)
'''
'''
#Questao 8
Primeiro =float(input("digite o primeiro produto "))
Segundo = float(input("digite o segundo produto "))
Terceiro =float(input("digite o terceiro produto "))
if(Primeiro < Segundo and Primeiro < Terceiro):
    print("o mais barato e: ", Primeiro)
elif(Segundo < Primeiro and Segundo < Terceiro):
    print("o mais barato e: ", Segundo)
elif(Terceiro < Primeiro and Terceiro < Segundo):
    print("o mais barato e: ",Terceiro)

'''
'''
# Questao 9
Primeiro = float(input("Digite um numero "))
Segundo = float(input("Digite um numero "))
Terceiro = float(input("Digite um numero "))

if(Primeiro > Segundo and Primeiro > Terceiro):
    if(Segundo > Terceiro):
        print(" ordem decrescente dos numeros e: ")
        print(Terceiro)
        print(Segundo)
        print(Primeiro)
    elif(Terceiro > Segundo):
        print(" ordem decrescente dos numeros e: ")
        print(Segundo)
        print(Terceiro)
        print(Primeiro)
if(Segundo > Primeiro and Segundo > Terceiro):
    if(Primeiro > Terceiro):
        print(" ordem decrescente dos numeros e: ")
        print(Terceiro)
        print(Primeiro)
        print(Segundo)
    elif(Terceiro > Primeiro):
        print(" ordem decrescente dos numeros e: ")
        print(Primeiro)
        print(Terceiro)
        print(Segundo)
if(Terceiro > Primeiro and Terceiro > Segundo):
    if(Primeiro > Segundo):
        print(" ordem decrescente dos numeros e: ")
        print(Segundo)
        print(Primeiro)
        print(Terceiro)
    elif(Segundo > Primeiro):
        print(" ordem decrescente dos numeros e: ")
        print(Primeiro)
        print(Segundo)
        print(Terceiro)
'''
'''
#Questao 10
print("Informe qual turno voce estuda M-matuino V-vespertino N-noturno: ")
Turno = str(input())
Turno = Turno.upper()
if(Turno == 'M'):
    print("Bom dia")
elif(Turno == 'V'):
    print("Boa tarde")
elif(Turno == 'N'):
    print("Boa noite")
else:
    print("comando invalido ")
'''
'''
#Questao 11
Salario = float(input("informe seu salario atual: "))
Aumento = 0
NovoSalario = 0
if(Salario <= 280):
    Aumento = (Salario *20)/100
    NovoSalario = Salario+Aumento
    print("O salario antigo era R$",Salario)
    print("O seu aumento vai ser de 20%")
    print("O aumento foi de R$", Aumento)
    print("O seu novo salario vai ser R$",NovoSalario)

elif(280 < Salario < 700):
    Aumento = (Salario * 15) / 100
    NovoSalario = Salario + Aumento
    print("O salario antigo era R$", Salario)
    print("O seu aumento vai ser de 15%")
    print("O aumento foi de R$", Aumento)
    print("O seu novo salario vai ser R$", NovoSalario)

elif(700 <= Salario < 1500):
    Aumento = (Salario * 10) / 100
    NovoSalario = Salario + Aumento
    print("O salario antigo era R$", Salario)
    print("O seu aumento vai ser de 10%")
    print("O aumento foi de R$", Aumento)
    print("O seu novo salario vai ser R$", NovoSalario)
elif(Salario >= 1500):
    Aumento = (Salario * 5) / 100
    NovoSalario = Salario + Aumento
    print("O salario antigo era R$", Salario)
    print("O seu aumento vai ser de 5%")
    print("O aumento foi de R$", Aumento)
    print("O seu novo salario vai ser R$", NovoSalario)
'''
'''
#Questao 12
ValorHora = float(input("qual o valor da sua hora: "))
HorasTrabalhadas = float(input("quantas horas trabalhou no mes: "))
SalarioBruto = ValorHora*HorasTrabalhadas
Sind = (SalarioBruto * 3)/100
FGTS = (SalarioBruto * 11)/100
IR =0
if(SalarioBruto <= 900):
    SalarioLiquido = SalarioBruto- Sind

    print("Salario Bruto R$", SalarioBruto)
    print("(-)IR         insento")
    print("(-)Sindicato     R$",Sind)
    print("(-)FGTS           R$",FGTS)
    print("Descontos       R$",Sind)
    print("Salario Liquido   R$",SalarioLiquido)

elif(900 < SalarioBruto <=1500):
    IR = (SalarioBruto * 5) / 100
    SalarioLiquido = SalarioBruto - (Sind+IR)

    print("Salario Bruto R$", SalarioBruto)
    print("(-)IR         R$",IR)
    print("(-)Sindicato     R$", Sind)
    print("(-)FGTS           R$", FGTS)
    print("Descontos       R$", Sind+IR)
    print("Salario Liquido   R$", SalarioLiquido)

elif(1500 < SalarioBruto <=2500):
    IR = (SalarioBruto * 10) / 100
    SalarioLiquido = SalarioBruto - (Sind+IR)

    print("Salario Bruto R$", SalarioBruto)
    print("(-)IR         R$",IR)
    print("(-)Sindicato     R$", Sind)
    print("(-)FGTS           R$", FGTS)
    print("Descontos       R$", Sind+IR)
    print("Salario Liquido   R$", SalarioLiquido)

elif(2500 <= SalarioBruto ):
    IR = (SalarioBruto * 20) / 100
    SalarioLiquido = SalarioBruto - (Sind+IR)

    print("Salario Bruto R$", SalarioBruto)
    print("(-)IR         R$",IR)
    print("(-)Sindicato     R$", Sind)
    print("(-)FGTS           R$", FGTS)
    print("Descontos       R$", Sind+IR)
    print("Salario Liquido   R$", SalarioLiquido)

'''
'''
#Questao 13
Dia = int(input("digite um numero corresponte ao dia da semana: "))
if(Dia == 1):
    print("Domingo")
elif(Dia == 2):
    print("Segunda")
elif(Dia == 3):
    print("Terça")
elif(Dia == 4):
    print("Quarta")
elif(Dia == 5):
    print("Quinta")
elif(Dia == 6):
    print("Sexta")
elif(Dia == 7):
    print("Sabado")
else:
    print("numero invalido")
    
'''
'''
#Questao 14
Nota1 = float(input("Digite a nota do aluno (1): "))
Nota2 = float(input("Digite a nota do aluno (2): "))
Media = (Nota1 + Nota2)/2

if(9<= Media <=10):
    print("Conceito A")
    print("Aprovado")
elif(7.5>= Media <9):
    print("Conceito B")
    print("Aprovado")
elif(6.0<= Media <7.5):
    print("Conceito C")
    print("Aprovado")
elif(4 <= Media <6.0):
    print("Conceito D")
    print("Reprovado")
elif(0<= Media <4):
    print("Conceito E")
    print("Reprovado")
'''
'''
#Questao 15
LadoA = float(input("informe o valor do lado 1 "))
LadoB = float(input("informe o valor do lado 2 "))
LadoC = float(input("informe o valor do lado 3 "))
if((LadoA + LadoB) > LadoC and (LadoA + LadoC) > LadoB and (LadoB + LadoC) > LadoA):
    print("E um triangulo do tipo: ")

    if(LadoA == LadoB and LadoA == LadoC):
        print("equilatero")

    elif(((LadoA == LadoB) and LadoA != LadoC) or ((LadoA == LadoC) and LadoA != LadoB) or ((LadoB == LadoC) and LadoB != LadoA)):
        print("isosceles")

    elif((LadoA != LadoB and LadoB != LadoC)):
        print("escaleno")

else:
    print("nao e um triangulo")

'''
'''
#Questao 16
print("Equação do segundo grau ")
a = float(input("informe o valor de a "))
b = float(input("informe o valor de b "))
c = float(input("informe o valor de c "))

delta = (b*b)-(4*a*c)
if(a == 0):
    print("voce nao informou uma equação do segundo grau")
elif(delta < 0):
    print("A equação nao tem raizes reais ")
elif(delta == 0 ):
    print("A equaçao possui apenas uma raiz: ")
    x = -b/(2*a)
    print(x)
elif(delta > 0):
    print("A equaçao possui duas raizes: ")
    x1 =(-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print(x1)
    print(x2)
'''
'''
#Quetsao 17
Ano = int(input("informe um ano: "))
Cond1 = Ano%400
Cond2 = Ano%4
Cond3 = Ano%100
if(Cond1 == 0):
    print("O ano e bisssexto")
elif(Cond2 == 0 and Cond3 != 0):
    print("Ano Bissexto")
else:
    print("NAO E BISSEXTO")
    
'''
'''
#Questao 18
Dia = int(input("Informe o dia "))
Mes = int(input("Informe o mes "))
Ano = int(input("Informe o ano "))
if((1 <= Dia <=31) and (1 <= Mes <= 12) and (1 <= Ano <= 9999)):
    print(Dia,"/",Mes,"/",Ano)
else:
    print("Fornato incorreto")

'''
'''
#Questao 19
Numero =int(input("informe um numero inteiro ate 999: "))
Cent = Numero // 100
Deze = (Numero % 100)//10
Unid = ((Numero % 100) % 10)
if(Numero <= 999):
    print(Numero," = ",Cent," Centenas ",Deze," Dezenas ", Unid, " Unidades ")
else:
    print("Numero invalido")

'''
'''
#Questao 21
print("Notas disponiveis 1, 5, 10, 50, 100")
Saque = int(input("Informe o valor do saque (MIN 10, MAX 600): "))
Cent = Saque // 100
Cinq = (Saque % 100) // 50
Dez = ((Saque % 100) % 50) // 10
Cinc = (((Saque % 100) % 50)%10) // 5
Um =  (((Saque % 100) % 50)%10) % 5

if(10 <= Saque <=600):
    print(Cent," Notas de cem ",Cinq," Notas de cinquenta ",Dez," Notas de dez ",Cinc," Notas de cinco ",Um," Notas de um")

else:
    print("Valor invalido")

'''
'''
#Questao 22
Numero = int(input("informe um numero "))
Calculo = Numero//2

if(Calculo == 0):

    print(Numero,"= PAR")
else:
    print(Numero,"= IMPAR")

'''
'''
#Questao 23
Numero = float(input("informe um numero: "))
Calculo = Numero % round(Numero)

if(Calculo == 0):
    print(Numero,"= Inteiro")
else:
    print(Numero,"= Decimal")

'''
'''
#Questao 24

def Par_Impar(Resultado):
    Calculo = 0
    Calculo = Resultado % 2

    if(Calculo == 0):
        print("par")
    elif(Calculo != 0):
        print("impar")


def Pos_Neg(Resultado):
    if(Resultado > 0):
        print("positivo")
    elif(Resultado < 0):
        print("negativo")


def Int_Dec(Resultado):
    Calculo = 0
    Calculo = Resultado % round(Resultado)
    if(Calculo == 0):
        print("inteiro")
    else:
        print("decimal")


Num1=float(input("Informe o primeiro numero: "))
Num2 = float(input("informe o segundo numero: "))

Som = Num1 + Num2
Sub = Num1 - Num2
Mult = Num1 * Num2
Divi = Num1 / Num2

print("Qual operaçao deseja realizar:")
print("(a) SOMA")
print("(b) SUBTRAÇAO")
print("(c) MULTIPLICAÇAO")
print(("(d) DIVISAO"))
Letra = str(input("Digite a letras: "))
Letra = Letra.title()

if(Letra == "A"):

    print("Soma = ",Som)
    if(Som > 0):
        Par_Impar(Som)
    else:
        print("Nem par nem impar")

    Pos_Neg(Som)
    Int_Dec(Som)


elif(Letra == "B"):
    print("Subtraçao = ", Sub)
    if (Sub > 0):
        Par_Impar(Sub)
    else:
        print("Nem par nem impar")

    Pos_Neg(Sub)
    Int_Dec(Sub)


elif(Letra == "C"):
    print("Multiplicaçao = ", Mult)
    if (Mult > 0):
        Par_Impar(Mult)
    else:
        print("Nem par nem impar")

    Pos_Neg(Mult)
    Int_Dec(Mult)


elif(Letra == "D"):
    print("Divisao = ", Divi)
    if (Divi > 0):
        Par_Impar(Divi)
    else:
        print("Nem par nem impar")

    Pos_Neg(Divi)
    Int_Dec(Divi)

'''
'''
#Questao 25
A = str(input("telefonou para vitima (s)SIM (n)NAO: ")).upper()
B = str(input("Esteve no local do crime (s)SIM (n)NAO: ")).upper()
C = str(input("Mora perto da vitima (s)SIM (n)NAO: ")).upper()
D = str(input("Devia para vitima (s)SIM (n)NAO: ")).upper()
E = str(input("Ja trabalho para vitima (s)SIM (n)NAO: ")).upper()

Julgamento = 0

if(A == 'S'):
    Julgamento += 1
if(B == 'S'):
    Julgamento +=1
if(C == 'S'):
    Julgamento +=1
if(D == 'S'):
    Julgamento +=1
if(E == 'S'):
    Julgamento +=1

if(Julgamento < 2):
    print("inocente")
if(Julgamento == 2):
    print("suspeita")
if(Julgamento == 3 or Julgamento ==4):
    print("cumplice")
if(Julgamento == 5):
    print("assassino")

'''
'''
#Questao 26
Combustivel = str(input("(A)-alcool / (G)-gasolina: ")).upper()
Preco = 0

if(Combustivel == 'A'):
    Litros = float(input("informe quantos litros deseja: "))
    if(Litros <= 20):
        Preco = Litros*1.9
        Desconto = Preco-((Preco * 3)/100)
        print("O valor total seria: ",Preco)
        print("o valor que vai pagar com desconto e: ", Desconto)
    elif(Litros >20):
        Preco = Litros * 1.9
        Desconto = Preco - ((Preco * 5) / 100)
        print("O valor total seria: ", Preco)
        print("o valor que vai pagar com desconto e: ", Desconto)


if(Combustivel == 'G'):
    Litros = float(input("informe quantos litros deseja: "))
    if(Litros <= 20):
        Preco = Litros*2.5
        Desconto = Preco-((Preco * 4)/100)
        print("O valor total seria: ",Preco)
        print("o valor que vai pagar com desconto e: ", Desconto)
    elif(Litros >20):
        Preco = Litros * 2.5
        Desconto = Preco - ((Preco * 6) / 100)
        print("O valor total seria: ", Preco)
        print("o valor que vai pagar com desconto e: ", Desconto)

'''
'''
#Questao 27
Morango = float(input("Quantos kg de Morango: "))
Maca =  float(input("Quantos kg de Maca: "))
Pmorango = 0
Pmaca = 0
Desconto = 0
Kg = Morango + Maca

if(Morango <= 5 and Maca <= 5):
    Pmorango = Morango*2.50
    Pmaca =  Maca * 2.20
    Total = Pmorango + Pmaca
    if(Kg > 8 or Total > 25 ):
        Desconto = Total -((Total*10)/100)
        print("O cliente paga com desconto :   R$ ",Desconto)
    else:
        print("O cliente paga: R$",Total)

if(Morango <= 5 and Maca > 5):
    Pmorango = Morango*2.50
    Pmaca =  Maca * 1.50
    Total = Pmorango + Pmaca
    if(Kg > 8 or Total > 25 ):
        Desconto = Total -((Total*10)/100)
        print("O cliente paga com desconto :   R$ ",Desconto)
    else:
        print("O cliente paga: R$",Total)

if(Morango > 5 and Maca <= 5):
    Pmorango = Morango*2.20
    Pmaca =  Maca * 2.20
    Total = Pmorango + Pmaca
    if(Kg > 8 or Total > 25 ):
        Desconto = Total -((Total*10)/100)
        print("O cliente paga com desconto :   R$ ",Desconto)
    else:
        print("O cliente paga: R$",Total)
if(Morango > 5 and Maca > 5):
    Pmorango = Morango*2.20
    Pmaca =  Maca * 1.50
    Total = Pmorango + Pmaca
    if(Kg > 8 or Total > 25 ):
        Desconto = Total -((Total*10)/100)
        print("O cliente paga com desconto :   R$ ",Desconto)
    else:
        print("O cliente paga: R$",Total)
'''
#Questao 28
print("File Duplo (1) ")
print("Alcatra (2)")
print("Picanha (3) ")
Carne = int(input("Digite o codigo da carne: "))
Cartao = str(input("Deseja utilizar cartao (s) (n) ")).upper()
Qnt = float(input("Digite a quantidade em kg "))
total = 0
Desconto = 0

if(Carne == 1):
    if(Cartao == 'S'):
        if(Qnt <= 5):
            total = Qnt*4.9
            Desconto = total - ((total*5)/100)
            print("preço total: R$",total)
            print("preço com desconto: R$",Desconto)
            print("tipo de carne: File Duplo")
        elif(Qnt > 5):
            total = Qnt * 5.8
            Desconto = total - ((total * 5) / 100)
            print("preço total: R$", total)
            print("preço com desconto: R$", Desconto)
            print("tipo de carne: File Duplo")
    elif(Cartao =='N'):
        if (Qnt <= 5):
            total = Qnt * 4.9
            print("preço total: R$", total)
            print("tipo de carne: File Duplo")
        elif(Qnt > 5):
            total = Qnt * 5.8
            print("preço total: R$", total)
            print("tipo de carne: File Duplo")

if(Carne == 2):
    if(Cartao == 'S'):
        if(Qnt <= 5):
            total = Qnt*5.9
            Desconto = total - ((total*5)/100)
            print("preço total: R$",total)
            print("preço com desconto: R$",Desconto)
            print("tipo de carne: Alcatra")
        elif(Qnt > 5):
            total = Qnt * 6.8
            Desconto = total - ((total * 5) / 100)
            print("preço total: R$", total)
            print("preço com desconto: R$", Desconto)
            print("tipo de carne: Alcatra")
    elif(Cartao =='N'):
        if (Qnt <= 5):
            total = Qnt * 5.9
            print("preço total: R$", total)
            print("tipo de carne: Alcatra")
        elif(Qnt > 5):
            total = Qnt * 6.8
            print("preço total: R$", total)
            print("tipo de carne: Alcatra")

if(Carne == 3):
    if(Cartao == 'S'):
        if(Qnt <= 5):
            total = Qnt*6.9
            Desconto = total - ((total*5)/100)
            print("preço total: R$",total)
            print("preço com desconto: R$",Desconto)
            print("tipo de carne: Picanha")
        elif(Qnt > 5):
            total = Qnt * 7.8
            Desconto = total - ((total * 5) / 100)
            print("preço total: R$", total)
            print("preço com desconto: R$", Desconto)
            print("tipo de carne: Picanha")
    elif(Cartao =='N'):
        if (Qnt <= 5):
            total = Qnt * 6.9
            print("preço total: R$", total)
            print("tipo de carne: Picanha")
        elif(Qnt > 5):
            total = Qnt * 7.8
            print("preço total: R$", total)
            print("tipo de carne: Picanha")