; number in bx, buffer in cx
num_to_string:

	push ax
	push bx
	push dx

	.loop:
	; DIVIDE
	mov ax, bx
	mov bx, 10
	xor dx, dx

	div bx
	; DIVIDE END

	add dx, '0'
	mov byte [cx], dl
	inc cx

	cmp ax, 0
	jg .loop

	pop dx
	pop bx
	pop ax

	ret
