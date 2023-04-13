from common_utils import generate_random_int_array

def sort(arr, pi):
    if len(arr) < 2:
        return pi, arr
    
    def swap(ai, bi, arr):
            tmp = arr[ai]
            arr[ai] = arr[bi]
            arr[bi] = tmp

    li = 0
    ri = len(arr) - 1

    if len(arr) == 2 and arr[li] > arr[ri]:
        swap(li, ri, arr)
        return pi, arr
    
    # try swapping without moving the pivot
    pv = arr[pi]
    while li < pi:
        if arr[li] > pv: # seek right swap candidate
            while pi < ri and arr[ri] > pv:
                ri -= 1

            if ri != pi: # swap
                swap(li, ri, arr)

                ri -= 1
                li += 1
                continue

        if ri == pi:
            break

        li += 1

    # continue swapping the rest moving the pivot
    assert(ri == pi or li == pi)
    left_side = li != pi
    idx, step = (li, 1) if left_side else (ri, -1)
    
    while idx != pi:
        need_swap = arr[idx] > pv if left_side else arr[idx] < pv
        if need_swap:
            # swap pivot and its left neighbour
            swap(pi, pi - step, arr)

            pi -= step
            if pi == idx: # adjacent elements were swapped
                break

            # swap current element and the element right behind the pivot
            swap(idx, pi + step, arr)
        
        skip = arr[idx] <= pv if left_side else arr[idx] >= pv
        if skip:
            idx += step

    return pi, arr

def quick_sort(arr):
    stack = [(0, len(arr))]
    while len(stack):
        li, ri = stack.pop()
        pi = (ri - li) // 2
        _pi, arr[li:ri] = sort(arr[li:ri], pi)
        pi = li + _pi
        if(ri - (pi + 1) > 1):
            stack.append((pi + 1, ri))
        if(pi - li > 1):
            stack.append((li, pi))
    return arr

def test():
    for l in range(0, 2**13, 5):
        print(l)
        arr1 = generate_random_int_array(l)
        arr2 = arr1.copy()
        arr1.sort()
        arr2 = quick_sort(arr2)
        assert(arr1 == arr2), f'\n{arr1}\n{arr2}'

test()