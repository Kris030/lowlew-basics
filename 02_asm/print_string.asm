
; string pointer in bx
print_string:

; preserve ax
	push ax

; Teletype output
	mov ah, 0Eh

; loop starts here
.loop:
; push bx as an argument
	push bx
	
; move al = *bx
	mov al, [bx]

; BIOS interrupt, print [al] to screen
	int 0x10

; move one char forward
	inc bx

; check if char is 0
	cmp [bx], word 0

;	loop if not 0
	jne .loop

; reset bx to original value
	pop bx

	ret
