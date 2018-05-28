import re


presentation = "Trabalho de arquitetura de computadores 1 - Dyonatha Kramer e Laerte Pack\n#Calculadora MIPS\n"
print ("\n" + presentation)
print ("Instruções:")
print ("A calculadora realiza SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO, RAIZ QUADRADA, POTENCIA, FATORIAL E FIBONACCI de "
       "operadores do tipo INTEIRO")

priority = []
dataArray = []
savedTemporary = ["$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7"]
temporary = ["$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7"]

def dataWrite():     #essa funcao ira escrever no arquivo
    file = open("calc.asm", "a+")
    file.write("\n.data\n")
    for i in range(0, len(operands)):
        file.write("\t" + az[0][i] + ": .word " + str(operands[i]) + "\n")  #pega a letra do alfabeto de acordo com a necessidade e refere ao operando
        dataArray.append(az[0][i])
    file.write("\n.text\n\tmain:\n")    #adiciona a parte .text e main:

    for i in range(0, len(operands)):
        file.write("\t\tlw " + str(savedTemporary[i]) + ", " + str(dataArray.pop(0)) + "\n")    #faz load word e atribui o dado a um registrador

    #preciso arrumar a estrutura para que as operacoes sejam feitas de forma correta

        if operators[i] == "*":
            file.write("\t\tmult " + str(temporary[i]) + ", " + str(savedTemporary.pop(0) + ", " + str(savedTemporary.pop(0))) + "\n")

        if operators[i] == "/":
            file.write("\t\tdiv " + str(temporary[i]) + ", " + str(savedTemporary.pop(0) + ", " + str(savedTemporary.pop(0))) + "\n")


    for i in range(0, len(operators) -1):
        if operators[i] == "+":
            file.write("\t\tadd " + str(temporary[i]) + ", " + str(savedTemporary.pop(0) + ", " + str(savedTemporary.pop(0))) + "\n")

        if operators[i] == "-":
            file.write("\t\tadd " + str(temporary[i]) + ", " + str(savedTemporary.pop(0) + ", " + str(savedTemporary.pop(0))) + "\n")
    file.close()


file = open("calc.asm", "w+")
file.write("#" + presentation)
file.close()

operators = []  #lista dinamica dos operadores
operators_index = []    #lista dinamica do indice dos operadores
operandsFromString = []     #lista dinamica dos operandos
az = ["abcdefghijklmnopqrstuvwxyz"]

expression = input("Entre com o calculo a ser realizado: ")


for i in range(0, len(expression)):     #aqui ele 'escaneia' a string em busca de operadores
    if not ((expression[i].isnumeric()) or (expression[i].isspace())):
        operators.append(expression[i])     #adiciona operadores na lista
        operators_index.append(i)       #adiciona o indice dos operadores na lista
operandsFromString.append(re.findall('\d+', expression))     #faz uma lista com operandos
operands = operandsFromString.pop()     #pega sub vetor e passa para vetor normal

#agora que tenho prioridade de expressao devo implementar codigo para que faca operacoes de forma correta em assembly
#para mais de duas operacoes. Tambem preciso implementar em assembly as expressoes fora dos parenteses e seja o que Deus quiser gente bouaaaa
priority = (re.findall(r'\((.*?)\)', expression))
print(priority)

