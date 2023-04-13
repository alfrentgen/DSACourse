from partial_sums import find_sum_in_sorted3
from random import seed
from common_utils import generate_random_int_array

def generate_all_sums(arr):
    win_size = len(arr)
    while win_size > 1:
        for i in range(0, len(arr) - win_size + 1):
            yield sum(arr[i : i + win_size]), i, i + win_size
        win_size -= 1

def random_test(arr_len, expectation):
    arr = generate_random_int_array(arr_len)
    arr.sort()
    seed(a=17)
    for target, li, ri in generate_all_sums(arr):
        ret = find_sum_in_sorted3(arr, target)
        if ret != expectation:
            print(arr)
            assert(ret == expectation),\
                f'{ret} != {expectation}\n{target} in [{li}, {ri}]'+\
                f'\nsum(arr[li:ri]) = {sum(arr[li:ri])}'+\
                f'\narr[li:ri] = {arr[li:ri]}'
    print(f'Random array test passed for sorted array of {len(arr)} elements.')

for l in range(0, 100):
    random_test(l, False if l < 2 else True)

def negative_random_test(arr_len):
    arr = generate_random_int_array(arr_len)
    arr.sort()
    seed(a=17)
    all_sums = [summ for summ, _, _ in generate_all_sums(arr)]
    all_sums.sort()
    false_sums = [all_sums[0] - 1]
    for i in range(0, len(all_sums) - 1):
        l = all_sums[i]
        r = all_sums[i + 1]
        if r - l > 1:
            false_sums.append(l + 1)
        if r - l > 2:
            false_sums.append((l + r) // 2)
            false_sums.append(r - 1)

    false_sums.append(all_sums[-1] + 1)
    for target in false_sums:
        ret = find_sum_in_sorted3(arr, target)
        if ret != False:
            print(arr)
            assert(ret == False),\
                f'{ret} != {False}\n{target} in [{li}, {ri}]'+\
                f'\nsum(arr[li:ri]) = {sum(arr[li:ri])}'+\
                f'\narr[li:ri] = {arr[li:ri]}'
    print(f'Random array negative test passed for sorted array of {len(arr)} elements.')

for l in range(2, 50):
    negative_random_test(l)

'''def reproduce(arr, target):
    for t, li, ri in generate_all_sums(arr):
        if t == target:
            print(li, ri, sum(arr[li:ri]))

    ret = find_sum_in_sorted3(arr, target)
    assert(ret == True)

arr = [-19743, 10387, 14004, 30310, 43035]
target = -9356
li, ri = [0, 2]
reproduce(arr, target)'''