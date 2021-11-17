; boot sector offset
;[org 0x7C00]

; c entry
extern c_main

; declare entry point
global start

; our code
section .text

; ----------------------- START OF CODE -----------------------

; 16 bit code
[bits 16]

start:
	call c_main
end:
	hlt
	jmp end

print_char:
	mov al, [bx]
	int 0x10 ; BIOS interrupt, print [al] to screen
	ret

; ----------------------- END OF CODE -----------------------
	
; padding till end of sector
times 510 - ($-$$) db 0

; boot signature
dw 0xaa55
