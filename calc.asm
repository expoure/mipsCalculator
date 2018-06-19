#Trabalho de arquitetura de computadores 1 - Dyonatha Kramer e Laerte Pack
#Calculadora MIPS

.data
	a: .word 2
	b: .word 4
	c: .word 6

.text
	main:
		lw $s0, b
		lw $s1, c
		mul $t0, $s0, $s1
		lw $s0, a
		add $t0, $t0, $s0
		li $v0, 1
		move $a0, $t0
		syscall