def findX(A, x):

    left = 0
    right = len(A)-1

    while left <= right:

        mid = (left + right) // 2

        if x < A[mid]:
            right = mid - 1
        elif x > A[mid]:
            left = mid + 1
        else:
            return mid
    
    return None

print(findX([1,3,6,7,11,12,644,64578],3))