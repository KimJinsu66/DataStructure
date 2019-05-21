def bubble_sort(array,n):
    for i in range(1,n-1):
        temp = array[i] 
        for j in range(1, n-i+1):
            if(array[j-1] > array[j]):
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
                
    return array

array = [6,5,3,1,8,7,2,4]
array = bubble_sort(array,len(array))
print(array)