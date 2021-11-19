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

	mov edx, [ecx]

	mov eax, [ebx]
	mov [ecx], eax

	dec ecx

	mov [ebx], edx

	inc ebx

	jmp .loop
	.loop_end:

	pop edx
	pop ecx
	pop ebx
	pop eax

	ret
