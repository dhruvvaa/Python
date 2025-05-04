def binary(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,3,5,7,9]
target=7
result=binary(arr,target)
if(result!=-1):
    print(f"Target element found at index {result}")
else:
    print("Target element not found")