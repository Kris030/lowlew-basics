
; ----------------------- ASSEMBLER DIRECTIVES -----------------------
zzz
; [???]
[org 0x7C00]
; [???]
[bits 16]

; declare entry point
global _start

; code section
section .text

; ----------------------- CODE -----------------------

_start:


; ----------------------- DATA -----------------------

; ----------------------- PADDING -----------------------

; [???]
times 512 - 2 - ($-$$) db 0

; [???]
dw 0xaa55
