def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    if len(ints) == 1:
        return (ints[0], ints[0])
    
    if len(ints) == 2:
        if ints[0] > ints[1]:
            return (ints[1], ints[0])
        else:
            return (ints[0], ints[1])
        
    mid = len(ints) // 2
    min_left, max_left = get_min_max(ints[:mid])
    min_right, max_right = get_min_max(ints[mid:])
    if min_left > min_right:
        min_all = min_right
    else:
        min_all = min_left
    if max_left > max_right:
        max_all = max_left
    else:
        max_all = max_right
        
    return (min_all, max_all)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print ("Pass" if (None == get_min_max([])) else "Fail")