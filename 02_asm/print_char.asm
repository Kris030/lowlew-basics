; char in ebx
print_char:
	
; preserve eax
	push eax

; Teletype output
	mov ah, 0Eh

; move al = *ebx
	mov al, [ebx]

; BIOS interrupt, print [al] to screen
	int 0x10

; restore eax
	pop eax

	ret
