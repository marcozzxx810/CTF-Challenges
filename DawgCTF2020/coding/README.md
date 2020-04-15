# Main Idea
This task is to netcat the server and enter the correct miles per minutes

There are over 100 enter and the calculation is not that easy so I tried out to make a simple python to automatically send the calculated miles per minutes to it.

# Code
1. formate the received text into `miles` `hr` `minutes` `second`
1. Since I the last answer is in minutes per miles, I tried to calculate second per miles first and convert back
1. **Rounding Issue may arised** So I used `%` to calculate the second part first and then use it to calculate minutes part

# Overall
It is an easy coding task, but rmb to print out the flag at last 