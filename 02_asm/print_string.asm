
; string pointer in ebx
print_string:

; preserve eax
	push eax

; Teletype output
	mov ah, 0Eh

; loop starts here
.loop:
; push ebx as an argument
	push ebx
	
; move al = *ebx
	mov al, [ebx]

; BIOS interrupt, print [al] to screen
	int 0x10

; move one char forward
	inc ebx

; check if char is 0
	cmp [ebx], word 0

;	loop if not 0
	jne .loop

; reset ebx to original value
	pop ebx

	ret
