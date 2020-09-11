def binarySearch(data,target,low ,high ):
    if low > high :
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binarySearch(data,target,low,mid-1)
        else:
            return binarySearch(data,target,mid+1,high)

w = "ABCDEF"
print([binarySearch(w,i,0,len(w)-1) for i in "ABCDEFGHIJK"])