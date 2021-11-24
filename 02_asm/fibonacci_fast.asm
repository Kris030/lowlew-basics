
; declare constants
%assign WORD_SIZE 2

; N in ebx, buff in ecx
fibonacci_fast:

	push ebx
	push ecx

; don't bother with loop if N < 2
	cmp bx, word WORD_SIZE
	mov ax, bx	
	jl .end

; set up fib(0), fib(1)
	mov [ecx], word 0
	add ecx, WORD_SIZE
	mov [ecx], word 1
	add ecx, WORD_SIZE

	.loop:
	add ecx, WORD_SIZE

	mov ax, word [ecx - WORD_SIZE]
	add ax, word [ecx - WORD_SIZE * 2]
	mov [ecx], word ax

	dec bx
	cmp bx, 0
	jg .loop
	
	.end:
	pop ecx
	pop ebx

	ret
