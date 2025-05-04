def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
num=[8,2,5,1,7,9,3]
print("Before sorting:",num)
bubble(num)
print("After sorting:",num)