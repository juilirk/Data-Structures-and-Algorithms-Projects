
def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is
    maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return None
    if len(input_list) == 1:
        return "There is only one  number in the list"

    l = mergesort(input_list)
    firstNumber = ""
    secondNumber = ""
    for i in range(len(l)):
        if i % 2 == 1:
            firstNumber += str(l.pop())
        else:
            secondNumber += str(l.pop())
    return [int(firstNumber), int(secondNumber)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Default
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


# test case 1
print(rearrange_digits([1, 1, 1, 1, 1]))
# should print [11,111]

# Edge case 1
print(rearrange_digits([9, 1, 8, 2, 7, 3, 9]))
# should print [972,9831]


# Edge Case 2
print(rearrange_digits([]))
# should print None

# Edge Case 2
print(rearrange_digits([10]))
# should print None
