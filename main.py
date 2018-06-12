import re
import shuntingYardAlgorithm

presentation = "Trabalho de arquitetura de computadores 1 - Dyonatha Kramer e Laerte Pack\n#Calculadora MIPS\n"
print ("\n" + presentation)
print ("Instruções:")
print ("A calculadora realiza SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO, RAIZ QUADRADA, POTENCIA e FATORIAL de "
       "operadores do tipo INTEIRO")

sizeArray = 0
operandsInOrder = []
dataArray = []
savedTemporary = ["$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7"]
savedTemporaryUsed = []
temporary = ["$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7"]
temporaryUsed = []

def dataWrite():     #essa funcao ira escrever no arquivo
    count = 0
    file = open("calc.asm", "a+")
    file.write("\n.data\n")
    for i in range(0, len(operands)):
        file.write("\t" + az[0][i] + ": .word " + str(operandsInOrder[i]) + "\n")  #pega a letra do alfabeto de acordo com a necessidade e refere ao operando
        dataArray.append(az[0][i])
    file.write("\n.text\n\tmain:\n")    #adiciona a parte .text e main:

    #for i in range(0, len(operands)):
    #    file.write("\t\tlw " + str(savedTemporary[i]) + ", " + str(dataArray.pop(0)) + "\n")    #faz load word e atribui o dado a um registrador


    for i in range(0, len(sya)):
        if not sya[i].isnumeric():
            #if sya[i] == "r":

            if sya[i] == "f":
                if len(rpn) != 0:
                    if rpn[0].isnumeric():
                        file.write("\t\tlw " + "$s0" + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\taddi $s1,$zero, 1\n\t\taddi $s2,$zero, 2\n\t\tli $s3, 268500992\n\t\tadd $t2,$zero, $s1\n\t\tlw $t3, a\n\t\tadd $s4, $s0, $s1"
                                   "\n\t\tslt $t0,$s0,$s2\n\t\t\tbeq $t0,$zero,LOOP\n\t\t\tj LSair"
                                   "\nLOOP:\n\t\taddi $t4, $t4, 1\n\t\t\tslt $t0, $t4, $s4\n\t\t\tbeq $t0, $zero, LSair\n\t\tmul $t2, $t2, $t4"
                                   "\n\t\tj LOOP\nLSair:\n\t\tsw $t2, ($s3)\n\t\tli $v0, 1\n\t\tmove $a0, $t2\n\t\tsyscall")
                        exit()

            #if sya[i] == "^":

            if sya[i] == "*":

                if len(rpn) != 0:
                    if rpn[0].isnumeric() and rpn[1].isnumeric():
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tlw " + str(savedTemporary[1]) + ", " + str(dataArray.pop(0)) + "\n")
                        temporaryUsed.append(temporary.pop(0))
                        file.write("\t\tmul " + str(temporaryUsed[count]) + ", " + str(savedTemporary[0]) + ", " + str(
                            savedTemporary[1]) + "\n")
                        try:
                            for j in range(i + 1, 0, -1):
                                rpn.pop(0)
                                print(str(rpn) + '*')
                        except Exception:
                            print('..')



                    else:
                        print(i)
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tmul " + str(temporaryUsed[0]) + ", " + str(temporaryUsed[0]) + ", " + str(
                            savedTemporary[0]) + "\n")
                        sizeArray = len(rpn)
                        for j in range(i, sizeArray, -1):      #for j in range(i, rpn[0], -1):
                            rpn.pop(0)
                            print(str(rpn) + '*')


            if sya[i] == "/":
                if len(rpn) != 0:
                    if rpn[0].isnumeric() and rpn[1].isnumeric():
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tlw " + str(savedTemporary[1]) + ", " + str(dataArray.pop(0)) + "\n")
                        temporaryUsed.append(temporary.pop(0))
                        file.write("\t\tdiv " + str(temporaryUsed[count]) + ", " + str(savedTemporary[0]) + ", " + str(
                            savedTemporary[1]) + "\n")
                        try:
                            for j in range(i + 1, 0, -1):
                                rpn.pop(0)
                                print(str(rpn) + '/')
                        except Exception:
                            print('..')
                        print('saiu')

                    else:
                        print(i)
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tdiv " + str(temporaryUsed[0]) + ", " + str(temporaryUsed[0]) + ", " + str(
                            savedTemporary[0]) + "\n")
                        sizeArray = len(rpn)
                        for j in range(i, sizeArray, -1):      #for j in range(i, rpn[0], -1):
                            rpn.pop(0)
                            print(str(rpn) + '/')

            if sya[i] == "+":
                if len(rpn) > 1:
                    if rpn[0].isnumeric() and rpn[1].isnumeric():
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tlw " + str(savedTemporary[1]) + ", " + str(dataArray.pop(0)) + "\n")
                        temporaryUsed.append(temporary.pop(0))
                        print(temporaryUsed)
                        file.write("\t\tadd " + str(temporaryUsed[count]) + ", " + str(savedTemporary[0]) + ", " + str(
                            savedTemporary[1]) + "\n")
                        try:
                            for j in range(i + 1, 0, -1):
                                rpn.pop(0)
                                print(str(rpn) + '+')
                        except Exception:
                            print('..')

                    else:
                        print(i)
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tadd " + str(temporaryUsed[0]) + ", " + str(temporaryUsed[0]) + ", " + str(
                            savedTemporary[0]) + "\n")
                        sizeArray = len(rpn)
                        for j in range(i, sizeArray, -1):      #for j in range(i, rpn[0], -1):
                            rpn.pop(0)
                if len(temporaryUsed) > 1:
                    file.write("\t\tadd " + str(temporaryUsed[0]) + ", " + str(temporaryUsed.pop(0)) + ", " + str(
                        temporaryUsed.pop(0)) + "\n")

            if sya[i] == "-":
                if len(rpn) > 1:
                    if rpn[0].isnumeric() and rpn[1].isnumeric():
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tlw " + str(savedTemporary[1]) + ", " + str(dataArray.pop(0)) + "\n")
                        temporaryUsed.append(temporary.pop(0))
                        file.write("\t\tsub " + str(temporaryUsed[count]) + ", " + str(savedTemporary[0]) + ", " + str(
                            savedTemporary[1]) + "\n")
                        try:
                            for j in range(i + 1, 0, -1):
                                rpn.pop(0)
                                print(str(rpn) + '-')
                        except Exception:
                            print('..')

                    else:
                        print(i)
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tsub " + str(temporaryUsed[0]) + ", " + str(temporaryUsed[0]) + ", " + str(
                            savedTemporary[0]) + "\n")
                        sizeArray = len(rpn)
                        for j in range(i, sizeArray, -1):      #for j in range(i, rpn[0], -1):
                            print(str(rpn) + '-')
                            rpn.pop(0)
                if len(temporaryUsed) > 1:
                    file.write("\t\tsub " + str(temporaryUsed[0]) + ", " + str(temporaryUsed.pop(0)) + ", " + str(
                        temporaryUsed.pop(0)) + "\n")
            count += 1

    file.write("\t\tli $v0, 1\n\t\tmove $a0, $t0\n\t\tsyscall")
    file.close()


file = open("calc.asm", "w+")
file.write("#" + presentation)
file.close()

operators = []  #lista dinamica dos operadores
operators_index = []    #lista dinamica do indice dos operadores
operandsFromString = []     #lista dinamica dos operandos
az = ["abcdefghijklmnopqrstuvwxyz"]
rpn = []
exp = []
expression = input("Entre com o calculo a ser realizado: ")


for i in range(0, len(expression)):     #aqui ele 'escaneia' a string em busca de operadores
    if not ((expression[i].isnumeric()) or (expression[i].isspace()) or (expression[i] == "(") or (expression[i] == ")")):
        operators.append(expression[i])     #adiciona operadores na lista
        operators_index.append(i)       #adiciona o indice dos operadores na lista
operandsFromString.append(re.findall('\d+', expression))     #faz uma lista com operandos
operands = operandsFromString.pop()     #pega sub vetor e passa para vetor normal


sya = shuntingYardAlgorithm.rpn(expression)

for i in range(0, len(sya)):
    rpn.append(sya[i])

for i in range(0, len(rpn)):
    if rpn[i].isnumeric():
        operandsInOrder.append(rpn[i])
print(rpn)
dataWrite()
