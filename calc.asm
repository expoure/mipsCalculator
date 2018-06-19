#Trabalho de arquitetura de computadores 1 - Dyonatha Kramer e Laerte Pack
#Calculadora MIPS

.data
	a: .word 9
	b: .word 9
	c: .word 8
	d: .word 1

.text
	main:
		lw $s0, a
		lw $s1, b
		add $t0, $s0, $s1
		lw $s0, c
		lw $s1, d
		mul $t1, $s0, $s1
		sub $t0, $t0, $t1
		li $v0, 1
		move $a0, $t0
		syscall