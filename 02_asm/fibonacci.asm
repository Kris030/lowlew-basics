
; N in ebx
fibonacci:

; check if greater than zero
	cmp ebx, 0
	jg .fib_1
; return 0
	mov eax, 0
	jmp .end

; check if == 1
	.fib_1:
	cmp ebx, 1
	jne .fib_N
; return 1
	mov eax, 1
	jmp .end

; rest of the cases
	.fib_N:

; call with N - 1
	push ebx
	sub ebx, 1
	call fibonacci

; call with N - 2
	pop ebx
	push ebx

	sub ebx, 2
; new local variable ecx = fib(n - 1)
	push ecx
	mov ecx, eax
	call fibonacci

; return = fib(n - 2) + ecx
	add eax, ecx

; pop ecx variable and parameter N
	pop ecx
	pop ebx

	.end:
	ret
