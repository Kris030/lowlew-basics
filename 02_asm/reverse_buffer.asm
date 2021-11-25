; buff pointer in ebx, buff end in ecx
reverse_buffer:

; variable tmp1
	push eax
; variable p1
	push ebx
; variable p2
	push ecx
; variable tmp2
	push edx

; --- LOOP START ---
; while (p1 < p2)
	.loop:
	cmp ebx, ecx
	jge .loop_end

; tmp2 = *p2
	mov dl, byte [ecx]

; *p1 = *p2
	mov al, byte [ebx]
	mov byte [ecx], al

; p2--
	dec ecx

; *p1 = tmp2
	mov byte [ebx], dl

; p1++
	inc ebx
	jmp .loop
; --- LOOP END ---

	.loop_end:
; clean up variables
	pop edx
	pop ecx
	pop ebx
	pop eax

	ret
