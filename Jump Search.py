import math

def jumpSearch(arr,x,n):
    step = math.floor(math.sqrt(len(arr)))

    prev = 0
    while arr[int(min(step,n)-1)] < x :
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1


    while arr[int(prev)] < x:
        prev += 1

        if prev == min(step,n):
            return -1

    if arr [int (prev)] == x:
        return prev

    return -1


arr = [5,6,11,14,15,25,63]
x = 63
n = len(arr)

index = jumpSearch(arr, x, n)

print("Number", x, "is at index", "%.0f" % index)



