

# Main Idea
This task is to reserve engineering missyelliott file. It is a ELF file.

# Code
1. first run `ltrace ./missyelliott`
2. input `AAAAAAAAAAAAAAAAAAAAAAAAAAAAA`
3. find out it decoded as `{{{{{{{{{{{{{{{{{{{{{{{{`
4. do `ltrace` again
5. input `{{{{{{{{{{{{{{{{{{{{{{{{` 
6. decoded as `AAAAAAAAAAAAA`
7. confirmed that it is a two way encoder-decoder.
8. hex string = `A\365Q\321Ma\325\351i\211\031\335\t\021\211\313\235\311i\361m\321}\211\331\265Y\221Y\2611Ym\321\213!\235\325=\031\021y\335`
(it is found out when doing ltrace, input sth to it and will display this string)
9. run `echo -e "A\365Q\321Ma\325\351i\211\031\335\t\021\211\313\235\311i\361m\321}\211\331\265Y\221Y\2611Ym\321\213!\235\325=\031\021y\335"| ltrace -s 50 ./missyelliott`
10. flag get

# Reminder

-e blackslash enable

-s specific string size

flag: DawgCTF{.tIesreveRdnAtIpilF,nwoDgnihTyMtuP}