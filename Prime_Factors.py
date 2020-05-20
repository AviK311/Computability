with open('spf.txt', 'r') as spf:
    lines = [line.split(':') for line in spf.readlines() if line.strip()]
    saved_factors = {int(l[0]):eval(l[1]) for l in lines}



def add_and_extend_list(list1, list2):
    ret_list1 = [val for val in list1]
    ret_list2 = [val for val in list2]
    if len(ret_list1) > len(ret_list2):
        for index, value in enumerate(ret_list2):
            ret_list1[index] += value
        return ret_list1
    else:
        for index, value in enumerate(ret_list1):
            ret_list2[index] += value
        return ret_list2


def check_saved_factors(x):
    ret_list = []
    
    for num, factors in sorted(saved_factors.items(), key = lambda x:x[0], reverse = True):
        while x%num == 0:
            x /= num
            ret_list = add_and_extend_list(ret_list, factors)
    return int(x), ret_list
            
def save_result(x, factors):
    if x not in saved_factors.keys() and x > 1:
        spf = open('spf.txt', 'a')
        spf.write("{0}: {1}\n".format(x, factors))
        spf.close()
        saved_factors[x] = factors


def verify_saved_factors():
    from Primes import prime
    from functools import reduce
    for num, factors in saved_factors.items():
        if num != reduce(lambda x,y: x*y, [prime(i+1)**val for i,val in enumerate(factors)]):
            print(f"{num} is stored badly")
