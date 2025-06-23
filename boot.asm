[org 0x7c00]
    mov si, message
print_loop:
    lodsb
    or al, al
    jz halt
    mov ah, 0x0e
    mov bh, 0x00
    mov bl, 0x07
    int 0x10
    jmp print_loop

halt:
    cli
hang:
    hlt
    jmp hang

message db 'Hello, world!', 0

times 510-($-$$) db 0
dw 0xaa55
