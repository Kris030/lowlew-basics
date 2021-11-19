
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
	; mov ebx, 5
	; call fibonacci
	
	; mov ebx, str
	; call print_string

	mov ebx, 12345
	mov ecx, to_string_result
	call num_to_string

	mov ebx, to_string_result
	call print_string

.end:
	hlt
	jmp .end

%include "num_to_string.asm"
%include "print_string.asm"
%include "fibonacci.asm"

; ----------------------- DATA -----------------------

str: db `done.\r\n`, 0
to_string_result: times 10 db 0

; ----------------------- PADDING -----------------------

; padding till end of sector
times 512 - 2 - ($-$$) db 0

; boot signature
dw 0xaa55