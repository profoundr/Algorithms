def moveZero(arr,n):
    count = 0

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1


arr = [1,2,3,0,0,5,4,3,0,5,5,0,0]
n=len(arr)
moveZero(arr,n)
for i in range(n):
    print(arr[i])

nn
