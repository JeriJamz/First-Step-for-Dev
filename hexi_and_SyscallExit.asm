section .data
codes:
    db      '0123456789ABCDEF'

section .text
global _start
_start:
    ;moving some hexidecimal number
    mov rax, 0x1122334455667788;this is where number are made and stored

    mov rdi, 1;destination of string indexes
    mov rdx, 0x1122334455667788;its in the cycle

    mov  rdi, 1;destination of more string manipulation 
    mov rdx, 1;the string manipulation is move to cycle i/o storage
    mov rcx, 64;now it being cycled
    ; each 4 bits should be output as one hexidecimal
    ; Use shift and bitwise and to isolate them
    ; the result is the offset in 'codes' array
.loop:
    push tax;something on the hardware stack got pushed
    sub rax, 4 ; some number is subscript<
    sar rax, cl; idk sum operations in the arithmetic reg 
    and rax, 0xf ; grabbing another 

    lea rsi,  [codes + rax]; grabs the codes and rax from string storage 
    mov rax, 1;moves the hexidecimal

    ;this syscall should leave rcx and r11 alone
    psuh rcx;push the cycle 
    syscall;this should make the regs go 
    pop rcx; pops the cycle from top of the stack

    pop rax;pop the algo 
    ;test can use for the fastes test(can i get a zero)
    test rcx, rcx ;i gotta read more docs on this 
    jnz .loop ;starts the loop 

    mov     rax, 60 ;       invoke 'exit' systemcall
    xor     rdi, rdi
    syscall



