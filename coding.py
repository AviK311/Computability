from Primes import prime
from functools import reduce


def pair_encode(x,y):
    return 2**x * (2*y + 1) - 1




def pair_decode(z):
    num = z + 1
    x = 0
    y = 0
    while num%2 == 0:
        num/=2
        x+=1
    y = int((num-1)/2)
    return x, y

def r(z):
    return pair_decode(z)[1]
def l(z):
    return pair_decode(z)[0]

from Prime_Factors import *

def list_encode(*List):
    result = reduce(lambda x,y: x*y, [prime(i+1)**val for i,val in enumerate(List)])
    save_result(result, list(List))
    return result

def list_decode(x):
    remainder_x, ret_list = check_saved_factors(x)
    remainder_x_list = list()
    i = 1
    while remainder_x>1:
        remainder_x_list+=[0]
        p = prime(i)
        while remainder_x%p == 0:
            remainder_x/=p
            remainder_x_list[i-1]+=1  
        i+=1
    save_result(remainder_x, remainder_x_list)
    ret_list = add_and_extend_list(ret_list, remainder_x_list)
    save_result(x, ret_list)
    return ret_list

def ith(x,i):
    if isinstance(x, list):
        return x[i-1]
    decoded_x = list_decode(x)
    if len(decoded_x) < i:
        return 0
    return decoded_x[i-1]

def lt(x):
    if isinstance(x, list):
        return len(x)
    return len(list_decode(x))
       


def get_a_b_c(z):
    return l(z), l(r(z)), r(r(z))

def encode_a_b_c(a,b,c):
    return pair_encode(a, pair_encode(b,c))
    
