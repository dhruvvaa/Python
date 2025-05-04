def binarySearch(arr, target, low, high):
    if(low>high):
        return -1
    mid=(low+high)//2
    if(arr[mid==target]):
        return mid
    elif(arr[mid]<target):
        return binarySearch(arr, target,mid+1,high)
    else:
        return binarySearch(arr, target, low, mid-1)
arr=[1,4,2,6,9,7]
target=4
result=binarySearch(arr, target,0,len(arr)-1)
if (result != -1):
    print(f"Target elemnt found at index {result}")
else:
    print("Target element not found")