def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
    	return [-1, -1]

    sorted_list = sort(input_list)
    number1 = ""
    number2 = ""
    
    for i in range(len(sorted_list)):
        if i % 2 == 0:
            number1 += str(sorted_list[i])
        else:
            number2 += str(sorted_list[i])
            
    return [int(number1), int(number2)]
            

def sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    arr1 = sort(arr[:mid])
    arr2 = sort(arr[mid:])
    return merge(arr1, arr2)

def merge(arr1, arr2):
    merged = []
    index_1 = 0
    index_2 = 0
    while index_1 < len(arr1) or index_2 < len(arr2):
        
        if index_1 == len(arr1):
            for i in arr2[index_2:]:
                merged.append(i)
            break
            
        if index_2 == len(arr2):
            for i in arr1[index_1:]:
                merged.append(i)
            break
                
        if arr1[index_1] > arr2[index_2]:
            merged.append(arr1[index_1])
            index_1 += 1
        else:
            merged.append(arr2[index_2])
            index_2 +=1
        
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0], [0, 0]])
test_function([[0], [-1, -1]])