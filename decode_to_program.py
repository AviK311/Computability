import coding
label_order = "ABCDE"

def decode_instruction(tup):
    instruction = ""
    tag_num, inst_type, var_num = tup
    if tag_num != 0:
        instruction = f"[{get_tag(tag_num)}]"
    if var_num == 0:
        var = "Y"
    elif var_num%2==0:
        var = "Z{0}".format(int(var_num/2))
    else:
        var = "X{0}".format(int((var_num+1)/2))
    if inst_type == 0:
        instruction += f"{var} <- {var}"
    elif inst_type == 1:
        instruction += f"{var} <- {var} + 1"
    elif inst_type == 2:
        instruction += f"{var} <- {var} - 1"
    else:
        instruction += f"IF {var} != 0 GOTO {get_tag(inst_type-2)}"
    return instruction + "\n"


def get_tag(num):
    return label_order[num%5 - 1] + str(int((num+4)/5))
def decode(program):
    if isinstance(program, int):
        return decode_from_num(program)
    elif isinstance(program, list):
        return decode_from_list(*program)
    

def decode_from_num(program_code):
    instructions = coding.list_decode(program_code+1)
    print("Program Code:", program_code, sep = "\n")
    return decode_from_list(*instructions) 

def decode_from_list(*program_list):
    instructions = [(coding.l(num), coding.r(num)) for num in program_list]
    instructions = [(left, coding.l(right), coding.r(right)) for left, right in instructions]
    instructions = [decode_instruction(tup) for tup in instructions]
    Program = ''.join(instructions)
    print("Program:", Program, sep = "\n")
    return Program



