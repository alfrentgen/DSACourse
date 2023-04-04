from typing import List

def find_sum_in_sorted(arr: List, lookup_sum: int) -> bool:
    assert(len(arr) > 1)

    i = 0
    summ = arr[i]
    for j in len(1, arr):
        summ += arr[j]
        
        if summ == lookup_sum:
            return True
        
        if summ > lookup_sum:
            while i < j - 1:
                summ -= arr[i]
                i += 1
                if summ == lookup_sum:
                    return True
                if summ < lookup_sum:
                    break

    return False

def find_sum_in_sorted2(arr: List, lookup_sum: int) -> bool:
    assert(len(arr) > 1)

    i = 0
    summ = arr[i]
    for j in len(1, arr):
        summ += arr[j]
        
        if summ == lookup_sum:
            return True
        
        if summ > lookup_sum:
            while i < j - 1:
                summ -= arr[i]
                i += 1
                if summ == lookup_sum:
                    return True
                if summ < lookup_sum:
                    break

    return False

def find_first_non_negative(arr: List):
    for i in range(len(arr)):
        if arr[i] >= 0:
            return i
    
    return None

def check_with_opposites(cur_sum, target_sum, arr, idx):
    negative_target = target_sum < 0
    compare = lambda current, target : (current > target) if negative_target else (current < target)
    check_index = lambda idx : (idx < len(arr)) if negative_target else (-1 < idx)
    while check_index(idx):
        cur_sum += arr[idx]
        if cur_sum == target_sum:
            return True
        if compare(cur_sum, target_sum):
            break
        if negative_target:
            idx += 1
        else:
            idx -= 1
    return False

def check_subsums(cur_sum, target_sum, arr, li, ri):
    negative_target = target_sum < 0
    compare = lambda current, target : (current > target) if negative_target else (current < target)
    while li < ri:
        if cur_sum == target_sum:
            return True
        if compare(cur_sum, target_sum):
            break
        if negative_target:
            cur_sum -= arr[ri]
            ri -= 1
        else:
            cur_sum -= arr[li]
            li += 1
    return False

def find_sum_in_sorted3(arr: List, target_sum: int) -> bool:
    if len(arr) < 2:
        return False

    negative_sum = target_sum < 0
    first_non_neg_idx = find_first_non_negative(arr)
    has_non_negatives = first_non_neg_idx is not None
    has_negatives = bool(first_non_neg_idx and first_non_neg_idx > 0)
    
    if (negative_sum and not has_negatives) or (not negative_sum and not has_non_negatives):
        return False
    
    if (negative_sum and sum(arr[0 : first_non_neg_idx]) > target_sum) or\
        (not negative_sum and sum(arr[first_non_neg_idx : ]) < target_sum):
        return False
        
    has_opposites = has_non_negatives if negative_sum else has_negatives
    li = ri = first_non_neg_idx - 1 if negative_sum else first_non_neg_idx
    summ = arr[li]
	
    first_opp_idx = li + 1 if negative_sum else li - 1
    while True:
        if has_opposites and check_with_opposites(summ, target_sum, arr, first_opp_idx):
           return True

        if negative_sum:
            li -= 1
            if li < 0:
                break
        else:
            ri += 1
            if ri == len(arr):
                break
				
        summ += arr[li] if negative_sum else arr[ri]
        if check_subsums(summ, target_sum, arr, li, ri):
            return True

    return False
