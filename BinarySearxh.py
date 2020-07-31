def binarySearch(arr, low, high, key):
    if high < low:
        return -1

    # low + (high - low)/2;
    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high,
                            key);
    return binarySearch(arr, low, (mid - 1), key);


arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
key = 3
x = binarySearch(arr,0,n,3)
print(f'Index of element is {x}')