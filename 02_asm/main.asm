
; ----------------------- ASSEMBLER DIRECTIVES -----------------------

; boot sector offset
[org 0x7C00]
; 16 bit code
[bits 16]

; declare entry point
global _start

; our code
section .text

; ----------------------- CODE -----------------------

_start:
	
	mov edx, 0	

	.loop:

	mov ebx, str_fib_p_0
	call print_string

	mov ebx, edx
	mov ecx, buffer
	call num_to_string
	mov ebx, buffer
	call print_string

	mov ebx, str_fib_p_1
	call print_string
	
	mov ebx, edx
	;call fibonacci
	mov ecx, buffer
	call fibonacci_fast

	mov ebx, eax
	mov ecx, buffer
	call num_to_string

	mov ebx, buffer
	call print_string

	mov ebx, str_newline
	call print_string

	inc edx
	cmp edx, 38
	jl .loop

	mov ebx, str_finish
	call print_string

.end:
	hlt
	jmp .end

%include "fibonacci_fast.asm"
%include "num_to_string.asm"
%include "print_string.asm"
;%include "fibonacci.asm"

; ----------------------- DATA -----------------------

str_fib_p_0: db "fib(", 0
str_fib_p_1: db ") = ", 0
str_finish:  db "done."
str_newline: db `\r\n`, 0
buffer: times 10 db 0

; ----------------------- PADDING -----------------------

; padding till end of sector
times 512 - 2 - ($-$$) db 0

; boot signature
dw 0xaa55
