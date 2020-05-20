from coding import *


def label(i, y):
    return l(ith(assist(y),i))
def var(i,y):
    return r(r(ith(assist(y),i)))+1
def instr(i,y):
    return l(r(ith(assist(y),i)))
def label_(i,y):
    ret = instr(i,y)
    if ret > 2:
        return ret-2
    else:
        return 0

def term(x,y):
    return l(x)>lt(assist(y))

def skip(x,y):
    instruction = instr(l(x),y)
    if instruction == 0 and not term(x,y):
        return True
    if instruction >= 2 and r(x)%prime(var(l(x),y))!=0:
        return True
    return False

def incr(x,y):
    return instr(l(x),y)==1
def decr(x,y):
    return instr(l(x),y)==2 and r(x)%prime(var(l(x),y))==0
def branch(x,y):
    if instr(l(x),y)<=2:
        return False
    if r(x)%prime(var(l(x),y))!=0:
        return False
    for i in range(lt(assist(y))+1):
        if label(i,y)==label_(l(x),y):
            return True
    return False

def succ(x,y):
    #print(f"x,y in succ: {x},{y}")
    if skip(x,y):
        return pair_encode(l(x)+1, r(x))
    elif incr(x,y):
        return pair_encode(l(x)+1, r(x)*prime(var(l(x),y)))
    elif decr(x,y):
        return pair_encode(l(x)+1, r(x)/prime(var(l(x),y)))
    elif branch(x,y):
        for i in range(lt(assist(y))+1):
            if label(i,y)==label_(l(x),y):
                return pair_encode(i, r(x))
    return pair_encode(lt(assist(y))+1, r(x))


from functools import reduce

def init(*xs, y):
    right = reduce(lambda x,y: x*y, [prime(2*i)**val for i,val in enumerate(xs, start =1)]+[1])
    return pair_encode(1, right)

def snap(*xs, y, i):
    if i == 0:
        return init(*xs, y=y)
    else:
        return succ(snap(*xs, y=y, i=i-1), y)

def stp(*xs, y, t):
    return term(snap(*xs, y=y, i=t), y)

def print_snap(res):
    left = l(res)
    right = list_decode(r(res))
    print(f"<{left},{right}>")

def output(*xs, y, i):
    return ith(r(snap(*xs, y=y, i=i)), 1)

    

def assist(y):
    if isinstance(y, list):
        return y
    return y+1
