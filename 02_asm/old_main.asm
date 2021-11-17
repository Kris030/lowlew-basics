; boot sector offset
[org 0x7C00]

; declare entry point
global _start
global print_string

; our code
section .text

; ----------------------- START OF CODE -----------------------

; 16 bit code
[bits 16]

_start:
	mov bx, str
	call print_string
end:
	hlt
	jmp end

; char in al
print_char:
	int 0x10 ; BIOS interrupt, print [al] to screen
	ret

; string pointer in bx
print_string:
	mov ah, 0xE
; loop starts here
loop_label:
	mov al, [bx]
	int 0x10 ; BIOS interrupt, print [al] to screen

; move one char forward
	inc bl

; check if char is 0
	mov cx, [bx]
	test cx, cx
;	loop if not
	jnz loop_label

	ret

; ----------------------- END OF CODE -----------------------

str:
db "Sus.", 0

; padding till end of sector
times 510 - ($-$$) db 0

; boot signature
dw 0xaa55