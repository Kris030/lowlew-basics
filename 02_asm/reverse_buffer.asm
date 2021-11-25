; buff pointer in ebx, buff end in ecx
reverse_buffer:

	push eax
	push ebx
	push ecx
	
; tmp
	push edx

	.loop:
	cmp ebx, ecx
	jge .loop_end

	mov dl, byte [ecx]

	mov al, byte [ebx]
	mov byte [ecx], al

	dec ecx

	mov byte [ebx], dl

	inc ebx

	jmp .loop

	.loop_end:
	pop edx
	pop ecx
	pop ebx
	pop eax

	ret
