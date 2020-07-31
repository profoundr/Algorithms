def arrange(arr,ind,n):
    temp = ([0] *n)

    for i in range(n):
        temp[ind[i]] = arr[i]

    for i in range(n):
        arr[i] = temp[i]
        ind[i] = i



arr   = [10, 11, 12]
index = [1, 0, 2]
n=len(arr)

arrange(arr,index,n)

for i in range(n):
    print(arr[i])

for i in range(n):
    print(index[i])
