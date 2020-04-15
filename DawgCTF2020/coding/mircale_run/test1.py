import math
from pwn import *
conn = remote ('ctf.umbccd.io', 5300)
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
i=0
while True :

        n=str(conn.recvline()[1:-1])
        if 'pace' in n:
            
            index = n.find("ran")
            index_2 = n.find("in")
            index_3 = n.find("What")
            miles = float(n[index+4:index_2])
            times = n[index_2+3:index_3]
            
            hr= int(times[0])
            min= int(times[2:4])
            second= int(times[5:7])

            total_second = hr*3600+ min*60+second
            answer_second_miles = total_second/(miles)
            answer_min=int(total_second / (miles)//60)
            answer_sec= int(answer_second_miles % 60)
            formated_ans = str(answer_min)+":"+str(answer_sec)
        
            conn.sendline(formated_ans)
        else:
            print(n)
