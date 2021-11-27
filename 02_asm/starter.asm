
; ----------------------- ASSEMBLER DIRECTIVES -----------------------

; boot sector offset
[org 0x7C00]
; 16 bit code
[bits 16]

; declare entry point
global _start

; our code
section .text

; ----------------------- CODE -----------------------

_start:


; ----------------------- DATA -----------------------

; ----------------------- PADDING -----------------------

; padding till end of sector
times 512 - 2 - ($-$$) db 0

; boot signature
dw 0xaa55
