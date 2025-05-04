def linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[10,20,30,40,50]
target=40
result=linear(arr,target)
if result != -1:
    print("Element found at index:",result)
else:
    print("Element not found")