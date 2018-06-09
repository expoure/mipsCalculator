#Trabalho de arquitetura de computadores 1 - Dyonatha Kramer e Laerte Pack
#Calculadora MIPS

.data
	a: .word 2
	b: .word 4
	c: .word 8
	d: .word 4

.text
	main:
		lw $s0, a
		lw $s1, b
		mul $t0, $s0, $s1
		lw $s0, c
		lw $s1, d
		div $t1, $s0, $s1
		add $t0, $t0, $t1
		li $v0, 1
		move $a0, $t0
		syscall