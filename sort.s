section .text
global sort_array

sort_array:
    push rbp
    mov rbp, rsp
    
    push rbx
    push r12
    push r13
    
    cmp esi, 1
    jle .no_changes
    
    mov r12, rdi
    mov r13d, esi
    xor r10d, r10d
    
    mov ecx, r13d
    dec ecx
    
.outer_loop:
    xor ebx, ebx
    mov edx, r13d
    sub edx, ecx
    dec edx
    
.inner_loop:
    mov eax, [r12 + rbx*4]
    mov r8d, [r12 + rbx*4 + 4]
    
    cmp eax, r8d
    jle .no_swap
    
    mov [r12 + rbx*4], r8d
    mov [r12 + rbx*4 + 4], eax
    inc r10d
    
.no_swap:
    inc ebx
    cmp ebx, edx
    jl .inner_loop
    
    dec ecx
    jnz .outer_loop
    
    mov eax, r10d
    jmp .done
    
.no_changes:
    xor eax, eax
    
.done:
    pop r13
    pop r12
    pop rbx
    pop rbp
    ret
