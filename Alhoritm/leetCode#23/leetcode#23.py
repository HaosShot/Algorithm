lists = [[777,123123123,41245],[6001230,123123,555555],[54432,1235152,64123512521]]
arr = []

def new_arr(arr):
    for i in range(len(lists)):
        arr = arr + lists[i]
    return arr

def sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i -1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

result=new_arr(arr)
print(sort(result))

input("Нажмите любую клавишу,чтобы закрыть программу")
