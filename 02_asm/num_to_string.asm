
; number in ebx, buffer in ecx, returns result's length
num_to_string:

; count the length in esi
	push esi
	mov esi, 0

; argument N
	push ebx
; save ecx, edx
	push ecx
	push edx

	.loop:
; count++
	inc esi

; --- DIVIDE ---
; divide eax, result in eax
	mov eax, ebx
; by 10
	mov ebx, 10
; remainder in edx
	mov edx, 0
; run division
	div ebx
; --- DIVIDE END ---

; add '0' to remainder to get current digit
	add edx, '0'
; move it to buffer
	mov [ecx], edx
; advance buffer
	inc ecx

; restore N into ebx
	mov ebx, eax

; while (N > 0)
	cmp eax, 0
	jg .loop

	mov [ecx], word 0

; return length
	mov eax, esi

; restore registers
	pop edx
	pop ecx
	pop ebx

; setup reverse buffer call
	mov ebx, ecx
	add ecx, esi
	dec ecx
; save return value
	push eax
	call reverse_buffer

; restore esi and return value
	pop eax
	pop esi

	ret

%include "reverse_buffer.asm"

