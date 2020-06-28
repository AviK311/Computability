program ="""
IF X1 != 0 GOTO A1
Z1 <- Z1 + 1
IF Z1 != 0 GOTO A2
[A1]X1 <- X1 - 1
Y <- Y + 1
IF X1 != 0 GOTO A1"""


from main import *

code = encode(program)

i=0
input1 = 3
while not stp(input1, y=code, t=i):
    current = snap(input1, y=code, i=i)
    if incr(current, code):
        print(f"inst {i} is incr")
    if decr(current, code):
        print(f"inst {i} is decr")
    if branch(current, code):
        print(f"inst {i} is branch")
    if skip(current, code):
        print(f"inst {i} is skip")
    i+=1

print(f"The output of the program with input {input1} is", output(input1, y=code, i=i))
