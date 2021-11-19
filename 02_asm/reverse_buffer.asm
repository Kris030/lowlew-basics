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

	mov edx, [ebx]

; mov [ebx], [ecx]
	mov eax, [ecx]
	mov [ebx], eax

	dec ebx
	mov [ecx], edx
	inc ecx

	.loop_end:

	pop edx
	pop ecx
	pop ebx
	pop eax

	ret
