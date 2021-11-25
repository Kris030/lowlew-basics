
; declare constants
%assign WORD_SIZE 2

; N in ebx
fibonacci_fast:

; variable b in eax

; argument N / variable i
	push ebx
; variable a
	push ecx
; variable c
	push edx

; don't bother with loop if N < 2
	cmp ebx, 2
	mov eax, ebx
	jl .end

; set up a = fib(0), b = fib(1)
	mov ecx, 0
	mov eax, 1

	.loop:

; c = a + b
	mov edx, ecx
	add edx, eax

; a = b
	mov ecx, eax

; b = c
	mov eax, edx

	dec ebx
	cmp ebx, 1
	jg .loop
	
	.end:
	pop edx
	pop ecx
	pop ebx

	ret
