
print_char:
	
; preserve ax
	push ax

; Teletype output
	mov ah, 0Eh

; move al = *bx
	mov al, [bx]

; BIOS interrupt, print [al] to screen
	int 0x10
