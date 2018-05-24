import re


presentation = "Trabalho de arquitetura de computadores 1 - Dyonatha Kramer e Laerte Pack\n#Calculadora MIPS\n"
print ("\n" + presentation)
print ("Instruções:")
print ("A calculadora realiza SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO, RAIZ QUADRADA, POTENCIA, FATORIAL E FIBONACCI de "
       "operadores do tipo INTEIRO")




def dataWrite(): #essa funcao ira escrever na parte da estrutura referente aos operandos. .data:
    file = open("calc.asm", "a+")
    file.write(".data\n")
    for i in range(0, len(operands[0])):
        file.write("  " + az[0][i] + ": .word " + str(operands[0][i]) + "\n") #pega a letra do alfabeto de acordo com a necessidade e refere ao operando
    file.close()


file = open("calc.asm", "w+")
file.write("#" + presentation)
file.close()

operators = [] #lista dinamica dos operadores
operators_index = [] #lista dinamica do indice dos operadores
operands = [] #lista dinamica dos operandos
az = ["abcdefghijklmnopqrstuvwxyz"]

expression = input("Entre com o calculo a ser realizado: ")
for i in range(0, len(expression)): #aqui ele 'escaneia' a string em busca de operadores
    if not ((expression[i].isnumeric()) or (expression[i].isspace())):
        operators.append(expression[i])  #adiciona operadores na lista
        operators_index.append(i)   #adiciona o indice dos operadores na lista
operands.append(re.findall('\d+', expression)) #faz uma lista com
dataWrite()



print (len(operands[0]))
print (az)
print (operators)
print (operators_index)
print (operands[0][1])
