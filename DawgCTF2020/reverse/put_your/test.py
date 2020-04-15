hexstring="41f551d14d61d5e9698919dd091189cb9dc969f16dd17d89d9b5599159b131596dd18b219dd53d191179dd00"

flag_bytes = bytearray(hexstring.decode("hex"))

print(flag_bytes)

flag_bytes.reverse()




# while( j < 43):
#     i=0
#     char = int(0) 
#     while(i<8):
#         if ((1 << (i and 31) and (flag_bytes)[j]) != 0):
#             char = bytes(char | 1 << (7 - i and 31))
 #            print(char)
#         i=i+1
#     flag_bytes[j]=char
#     j=j+1

j=0
for bt in flag_bytes:
    char = int(0)
    i=int(0)
    while(i<8):
        if ( 1<<(i & 31) and bt!=0):
            char = (char| (1>>(7&31)))
        i=i+1
    bt = char
    print(char) 
    j=j+1
print(flag_bytes)