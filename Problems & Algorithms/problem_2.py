def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        return -1
    return recursive_search(input_list, number, 0, len(input_list)-1)


def recursive_search(input_list, target, start, end):
    if(start > end):
        return -1
    mid_index = (start+end)//2
    mid_element = input_list[mid_index]

    if mid_element == target:
        return mid_index

    if mid_element >= input_list[start]:
        if target < mid_element and input_list[start] <= target:
            return recursive_search(input_list, target, start, mid_index-1)
        return recursive_search(input_list, target, mid_index+1, end)

    if target > mid_element and target <= input_list[end]:
        return recursive_search(input_list, target, mid_index+1, end)
    return recursive_search(input_list, target, start, mid_index-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# test case 1
print(rotated_array_search([4, 5, 6, 2, 3], 10))
# should print -1

# test case 2
print(rotated_array_search([4, 5, 6, 1, 2, 3], 3))
# should print 5

# Edge Case 1
print(rotated_array_search([], 10))
# should print -1

# edge case 2
print(rotated_array_search([], 1))
# should print -1
