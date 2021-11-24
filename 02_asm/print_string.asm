
; string pointer in ebx
print_string:

; preserve eax and ebx
	push eax
	push ebx

; Teletype output
	mov ah, 0Eh

; loop starts here
	.loop:
	
; move al = *ebx
	mov al, byte [ebx]

; BIOS interrupt, print [al] to screen
	int 0x10

; move one char forward
	inc ebx

; check if char is 0
	cmp [ebx], byte 0

;	loop if not 0
	jne .loop

; reset eax and ebx to original value
	pop ebx
	pop eax

	ret
