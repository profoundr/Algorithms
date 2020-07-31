def interpolationSearch(arr,x,n):
    l = 0
    h = n - 1
    while arr[l] <= x and arr[h] >= x and l < h:

        if l == h:
            if arr[l] == x:
                return l
            return -1

        pos = l + int(((float(h - l) / ( arr[h] - arr[l])) * ( x - arr[l])))


        if arr[pos] < x:
            return pos + 1

        if arr[pos] == x:
            return pos

        else:
            h = pos - 1
    return -1




arr = [5,6,11,14,15,25,63]
x = 25
n = len(arr)

index = interpolationSearch(arr, x, n)

print("Number", x, "is at index", "%.0f" % index)
