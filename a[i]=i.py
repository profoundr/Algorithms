def fix(arr,n):
    list1 = []
    for i in range(n):
        if arr[i] != -1 and arr[i] == i:
            continue
        if arr[i] != -1 and arr[i] != i:
            x = arr[i]
            while arr[x] != -1 and arr[x] != x:
                y = arr[x]


                arr[x] = x

                x = y


            arr[x] = x

            if(arr[i] != i):
                arr[i] = -1

    for i in list1:
        arr[i] = -1



arr = [0, 6, 7, 8, -1, 4, 1, 2, 3]

n = len(arr)
fix(arr,n)

for i in range(n):
    print(arr[i])