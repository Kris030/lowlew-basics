
; ----------------------- ASSEMBLER DIRECTIVES -----------------------

; [???]
[org 0x7C00]
; [???]
[bits 16]

; code section
section .text

; ----------------------- CODE -----------------------



; ----------------------- DATA -----------------------

; ----------------------- PADDING -----------------------

; [???]
times 512 - 2 - ($-$$) db 0

; [???]
dw 0xaa55
