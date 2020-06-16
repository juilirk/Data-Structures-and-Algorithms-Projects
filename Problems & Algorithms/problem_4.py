def sort_012(input_list):
    low = 0
    high = len(input_list)-1
    mid = 0

    while(mid <= high):

        if input_list[mid] == 0:
            temp = input_list[low]
            input_list[low] = input_list[mid]
            input_list[mid] = temp
            low += 1
            mid += 1
            continue
        if input_list[mid] == 1:
            mid += 1
            continue
        if input_list[mid] == 2:
            temp = input_list[high]
            input_list[high] = input_list[mid]
            input_list[mid] = temp
            high -= 1
            continue

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# test case 1
print(sort_012([0, 1, 2, 0, 1, 2]))
# should print [0,0,1,1,2,2]

# Edge case 1
print(sort_012([]))
# should print []

# Edge case 2
print(sort_012([1]))
# should print [1]
