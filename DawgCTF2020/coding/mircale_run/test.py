from pwn import *
conn = remote ('ctf.umbccd.io', 5300)
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())

n=conn.recvline())

conn.sendline('7:53')
print(conn.recvline())

conn.sendline('9:06')
print(conn.recvline())

conn.sendline('6:44')
print(conn.recvline())

conn.sendline('9:12')
print(conn.recvline())

conn.sendline('8:24')
print(conn.recvline())

conn.sendline('10:05')
print(conn.recvline())

conn.sendline('8:24')
print(conn.recvline())

conn.sendline('8:45')
print(conn.recvline())

conn.sendline('9:35')
print(conn.recvline())

conn.sendline('6:55')
print(conn.recvline())

conn.sendline('8:48')
print(conn.recvline())

conn.sendline('8:47')
print(conn.recvline())

conn.interactive()