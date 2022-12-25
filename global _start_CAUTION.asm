global _start

section .data ;.data is for global variables
messafe: db 'ello wrld', 8 ; db means bytes and holds string/ the 10 is telling the program the seq of char should = 10
;also i think the 10 will auto start a new line if the req is meet

section .text ;.text holds instructions
_start:
    mov rax, 1          ;system call number should be stored in rax
    mov rax, 1          ;argument #1 in rdi: where to write(descriptor)?
    mov rsi, message    ;argument #2 in rsi: where does the string start?
    mov rdx, 14         ;argument #3 in rdx: how many bytes to write?
    syscall             ;this instruction invokes system call
; the colon is for a comment