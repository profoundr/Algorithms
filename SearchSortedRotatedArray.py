def PivotBinarySearch(arr,key,n):

    pivot = PivotSearch(arr,0,n)
    if arr[pivot] == key:
        return pivot
    if pivot == -1:
        return binarySearch(arr,0,n-1,key)
    elif arr[0] <= key:
        return binarySearch(arr,0,pivot - 1,key)

    return binarySearch(arr,pivot + 1,n-1,key)



def PivotSearch(arr,low,high):
    if high < low:
        return -1
    if low == high:
        return low
    mid = (low + high) // 2
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return PivotSearch(arr, low, mid-1)
    return PivotSearch(arr, mid + 1, high)


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



arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]

key = 3
n = len(arr)
x = PivotBinarySearch(arr,key,n)
if x == -1:
    print('not found')
else:
    print(f'The Index is at {x}')