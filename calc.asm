#Trabalho de arquitetura de computadores 1 - Dyonatha Kramer e Laerte Pack
#Calculadora MIPS

.data
	a: .word 8

.text
	main:
		lw $s0, a
		addi $s1,$zero, 1
		addi $s2,$zero, 2
		li $s3, 268500992
		add $t2,$zero, $s1
		lw $t3, a
		add $s4, $s0, $s1
		slt $t0,$s0,$s2
			beq $t0,$zero,LOOP
			j LSair
LOOP:
		addi $t4, $t4, 1
			slt $t0, $t4, $s4
			beq $t0, $zero, LSair
		mul $t2, $t2, $t4
		j LOOP
LSair:
		sw $t2, ($s3)
		li $v0, 1
		move $a0, $t2
		syscall