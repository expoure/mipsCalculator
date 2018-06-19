import re
import shuntingYardAlgorithm


presentation = "Trabalho de arquitetura de computadores 1 - Dyonatha Kramer e Laerte Pack\n#Calculadora MIPS\n"
print ("\n" + presentation)
print ("Instruções:")
print ("A calculadora realiza SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO, POTENCIA e FATORIAL de "
       "operadores do tipo INTEIRO")

operandsInOrder = []
dataArray = []
savedTemporary = ["$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7"]
savedTemporaryUsed = []
temporary = ["$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7"]
temporaryUsed = []

def dataWrite():     #essa funcao ira escrever no arquivo
    poped = 0 #identa toda vez que um elemento eh retirado do rpn para que seja possivel fazer manipulacao de vetores corretamente
    count = 0
    file = open("calc.asm", "a+")
    file.write("\n.data\n")
    for i in range(0, len(operands)): #vai carregar o word de acordo com os numeros do vetor ordenado
        file.write("\t" + az[0][i] + ": .word " + str(operandsInOrder[i]) + "\n") #utiliza vetor de alfabeto de acordo com necessidade
        dataArray.append(az[0][i]) #letra vai para vetor de variaveis usadas
    file.write("\n.text\n\tmain:\n")    #adiciona a parte .text e main:

    for i in range(0, len(sya)): #vai varrer a lista padrao
        if not sya[i].isnumeric():

            #trecho referente ao fatorial
            if sya[i] == "f":
                if len(rpn) != 0:
                    if rpn[0].isnumeric():
                        file.write("\t\tlw " + "$s0" + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\taddi $s1,$zero, 1\n\t\taddi $s2,$zero, 2\n\t\tli $s3, 268500992\n\t\tadd $t2,$zero, $s1"
                                   "\n\t\tlw $t3, a\n\t\tadd $s4, $s0, $s1\n\t\tslt $t0,$s0,$s2\n\t\t\tbeq $t0,$zero,LOOP\n\t\t\tj LSair"
                                   "\nLOOP:\n\t\taddi $t4, $t4, 1\n\t\t\tslt $t0, $t4, $s4\n\t\t\tbeq $t0, $zero, LSair\n\t\tmul $t2, $t2, $t4"
                                   "\n\t\tj LOOP\nLSair:\n\t\tsw $t2, ($s3)\n\t\tli $v0, 1\n\t\tmove $a0, $t2\n\t\tsyscall")
                        exit()
            #trecho referente a potencia de x e y
            if sya[i] == "^":
                if len(rpn) != 0:
                    if rpn[i-1].isnumeric() and rpn[i-2].isnumeric():
                        file.write("\t\tlw " + "$s0" + ", " + str(dataArray.pop(0)) + "\n\t\tlw $s1, " + str(dataArray.pop(0)))
                        file.write("\n\t\taddi $t0,$s0, 0\n\t\taddi $t1,$zero, 0\n\twhile:\n\t\tblt $s1, 2, exit\n\t\tsubi $s1, $s1, 1"
                                   "\n\t\tmul $t0, $t0, $s0\n\t\tj while\n\texit:\n\t\tli $v0, 1\n\t\tmove $a0, $t0\n\t\tsyscall")
                        exit()
            #trecho referente a multiplicacao
            if sya[i] == "*":
                print(str(rpn) + '*')
                if len(rpn) != 0:
                    if rpn[i - 2 - poped].isnumeric() and rpn[i - 1 - poped].isnumeric(): #verifica argumentos de rpn com base em sya utilizando 'poped'
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(i-2-poped)) + "\n")
                        file.write("\t\tlw " + str(savedTemporary[1]) + ", " + str(dataArray.pop(i-2-poped)) + "\n")
                        temporaryUsed.append(temporary.pop(0))
                        file.write("\t\tmul " + str(temporaryUsed[count]) + ", " + str(savedTemporary[0]) + ", " + str(
                            savedTemporary[1]) + "\n")
                        count += 1
                        try:
                            for j in range(i-poped, i-poped-3, -1):     #elimina operacoes e operandos ja utilizados
                                rpn.pop(j)
                                poped += 1
                                print(str(rpn) + '*')
                        except Exception:
                            print('..')

                    else:
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tmul " + str(temporaryUsed[0]) + ", " + str(temporaryUsed[0]) + ", " + str(
                            savedTemporary[0]) + "\n")
                        for j in range(i - poped, i - poped - 2, -1):  #elimina operacoes e operandos ja utilizados
                            rpn.pop(0)
                            poped += 1
                            print(str(rpn) + '*')

            # trecho referente a divisao
            if sya[i] == "/":
                print(str(rpn) + '/')
                if len(rpn) != 0:
                    if rpn[i - 2 - poped].isnumeric() and rpn[i - 1 - poped].isnumeric():
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(i-2-poped)) + "\n")
                        file.write("\t\tlw " + str(savedTemporary[1]) + ", " + str(dataArray.pop(i-2-poped)) + "\n")
                        temporaryUsed.append(temporary.pop(0))
                        print(count)
                        file.write("\t\tdiv " + str(temporaryUsed[count]) + ", " + str(savedTemporary[0]) + ", " + str(
                            savedTemporary[1]) + "\n")
                        count += 1
                        try:
                            for j in range(i-poped, i-poped-3, -1): #elimina operacoes e operandos ja utilizados
                                rpn.pop(j)
                                poped += 1
                                print(str(rpn) + '/')
                        except Exception:
                            print('..')

                    else:
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tdiv " + str(temporaryUsed[0]) + ", " + str(temporaryUsed[0]) + ", " + str(
                            savedTemporary[0]) + "\n")
                        for j in range(i - poped, i - poped - 2, -1):  #elimina operacoes e operandos ja utilizados
                            rpn.pop(0)
                            poped += 1
                            print(str(rpn) + '/')

            # trecho referente a adicao
            if sya[i] == "+":
                print(str(rpn) + '+')
                if len(rpn) > 1:
                    if rpn[i - 2 - poped].isnumeric() and rpn[i - 1 - poped].isnumeric():
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(i-2-poped)) + "\n")
                        file.write("\t\tlw " + str(savedTemporary[1]) + ", " + str(dataArray.pop(i-2-poped)) + "\n")
                        temporaryUsed.append(temporary.pop(0))
                        file.write("\t\tadd " + str(temporaryUsed[count]) + ", " + str(savedTemporary[0]) + ", " + str(
                            savedTemporary[1]) + "\n")
                        count += 1
                        try:
                            for j in range(i-poped, i-poped-3, -1):  #elimina operacoes e operandos ja utilizados
                                rpn.pop(j)
                                poped += 1
                                print(str(rpn) + '+')
                        except Exception:
                            print('..')

                    else:
                        print(i)
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tadd " + str(temporaryUsed[0]) + ", " + str(temporaryUsed[0]) + ", " + str(
                            savedTemporary[0]) + "\n")
                        for j in range(i-poped, i-poped-2, -1): #elimina operacoes e operandos ja utilizados
                            rpn.pop(0)
                            poped += 1
                if len(temporaryUsed) > 1:
                    file.write("\t\tadd " + str(temporaryUsed[0]) + ", " + str(temporaryUsed.pop(0)) + ", " + str(
                        temporaryUsed.pop(0)) + "\n")

            # trecho referente a subtracao
            if sya[i] == "-":
                print(str(rpn) + '-')
                if len(rpn) > 1:
                    if rpn[i - 2 - poped].isnumeric() and rpn[i - 1 - poped].isnumeric():
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(i-2-poped)) + "\n")
                        file.write("\t\tlw " + str(savedTemporary[1]) + ", " + str(dataArray.pop(i-2-poped)) + "\n")
                        temporaryUsed.append(temporary.pop(0))
                        file.write("\t\tsub " + str(temporaryUsed[count]) + ", " + str(savedTemporary[0]) + ", " + str(
                            savedTemporary[1]) + "\n")
                        count += 1
                        try:
                            for j in range(i-poped, i-poped-3, -1):  #elimina operacoes e operandos ja utilizados
                                rpn.pop(j)
                                poped += 1
                                print(str(rpn) + '-')
                        except Exception:
                            print('..')

                    else:
                        print(i)
                        file.write("\t\tlw " + str(savedTemporary[0]) + ", " + str(dataArray.pop(0)) + "\n")
                        file.write("\t\tsub " + str(temporaryUsed[0]) + ", " + str(temporaryUsed[0]) + ", " + str(
                            savedTemporary[0]) + "\n")
                        for j in range(i - poped, i - poped - 2, -1):  #elimina operacoes e operandos ja utilizados
                            print(str(rpn) + '-')
                            rpn.pop(0)
                            poped += 1
                if len(temporaryUsed) > 1:
                    file.write("\t\tsub " + str(temporaryUsed[0]) + ", " + str(temporaryUsed.pop(0)) + ", " + str(
                        temporaryUsed.pop(0)) + "\n")

    file.write("\t\tli $v0, 1\n\t\tmove $a0, $t0\n\t\tsyscall")
    file.close()




file = open("calc.asm", "w+")
file.write("#" + presentation)
file.close()

operandsFromString = []     #lista dinamica dos operandos
az = ["abcdefghijklmnopqrstuvwxyz"]
rpn = []
expression = input("Entre com o calculo a ser realizado: ")

operandsFromString.append(re.findall('\d+', expression))     #faz uma lista com operandos
operands = operandsFromString.pop()     #pega sub vetor e passa para vetor normal

sya = shuntingYardAlgorithm.rpn(expression)

for i in range(0, len(sya)):
    rpn.append(sya[i])

for i in range(0, len(rpn)):
    if rpn[i].isnumeric():
        operandsInOrder.append(rpn[i]) #coloca os operadores em outra lista e em ordem para serem usados no data
print(rpn)
dataWrite()
