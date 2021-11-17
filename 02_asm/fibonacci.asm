
; N in bx
fibonacci:

; check if greater than zero
	cmp bx, 0
	jg .fib_1
; return 0
	mov ax, 0
	jmp .end

; check if == 1
.fib_1:
	cmp bx, 1
	jne .fib_N
; return 1
	mov ax, 1
	jmp .end

; rest of the cases
.fib_N:

; call with N - 1
	push bx
	sub bx, 1
	call fibonacci

; call with N - 2
	pop bx
	push bx

	sub bx, 2
; new local variable cx = fib(n - 1)
	push cx
	mov cx, ax
	call fibonacci

; return = fib(n - 2) + cx
	add ax, cx

; pop cx variable
	pop cx
; pop N
	pop bx

.end:
	ret
