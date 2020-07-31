def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1


# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    rverseArray(arr, 0, d - 1)
    rverseArray(arr, d, n - 1)
    rverseArray(arr, 0, n - 1)


def rightRotate(arr,d):
    if d == 0:
        return
    n= len (arr)
    rverseArray(arr, 0, n - 1)
    rverseArray(arr, 0, d - 1)
    rverseArray(arr, d, n - 1)

# Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])

    # Driver function to test above functions


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2

# in case the rotating factor is
# greater than array length
d = d % n
leftRotate(arr, d)  # Rotate array by 2
printArray(arr)
print('\r')
rightRotate(arr,d)
printArray(arr)