; number in ebx, buffer in ecx
num_to_string:

; count the length in esi
	push esi
	xor esi, esi

	push ebx
	push ecx
	push edx

	.loop:
; count++
	inc esi

	; DIVIDE
	mov eax, ebx
	mov ebx, 10
	xor edx, edx

	div ebx
	; DIVIDE END

	add edx, '0'
	mov [ecx], edx
	inc ecx

	mov ebx, eax

	cmp eax, 0
	jg .loop

	mov [ecx], word 0

; return length
	mov eax, esi

; setup reverse buffer call
; ----
	dec ecx
	mov ebx, ecx
	sub ebx, esi

	;call reverse_buffer
; ----
	pop edx
	pop ecx
	pop ebx

	pop esi

	ret

%include "reverse_buffer.asm"
