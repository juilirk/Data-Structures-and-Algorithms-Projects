def sqrt(number=None):

    if number is None:
        return None
    if number < 0:
        return None
    if number == 0 or number == 1:
        return number

    start = 0
    end = number

    while(start < end):
        mid = (start+end)//2
        mid_pow = mid*mid

        if mid_pow == number:
            return mid
        elif mid_pow < number:
            start = mid+1
            result = mid
        else:
            end = mid
    return result


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# test case1
print(sqrt(4))
# should print 2

# test case2
print(sqrt(34))
# should print 5

# Edge case 1
print(sqrt())
# should print None

# Edge Case 2
print(sqrt(-1))
# should print None
