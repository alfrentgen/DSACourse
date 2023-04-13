from random import randint

def generate_random_int_array(length):
    return [randint(-(2**16), 2**16 - 1) for i in range(length)]
