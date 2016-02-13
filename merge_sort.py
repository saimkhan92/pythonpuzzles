# Python program to implement merge sort

def merge_sort(a):
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0
        
        while(i<len(left) and j<len(right)):
            if left[i]<right[j]:
                a[k]=left[i]
                i=i+1
            else:
                a[k]=right[j]
                j=j+1
            k=k+1

        while(i<len(left)):
            a[k]=left[i]
            k=k+1
            i=i+1
        while(j<len(right)):
            a[k]=right[j]
            k=k+1
            j=j+1


a=[2,3,4,6,1,2,8,3,5,7,3,5]
merge_sort(a)
print("The sorted list is {}".format(a))
            
        


    
    
