class Sort():

    @staticmethod
    def bubble_sort(arr):
        arr=list(arr)
        if len(arr)<=1:
            return arr
        for i in range(1,len(arr)):
            for j in range(len(arr)-i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
        
    @staticmethod
    def quick_sort(arr):
        arr=list(arr)
        if len(arr)<=1:
            return arr
        arr_l = []
        arr_r = []
        arr_m = []
        key = arr[0]
        for i in arr:
            if i<key:
                arr_l.append(i)
            elif i>key:
                arr_r.append(i)
            else:
                arr_m.append(i)
        arr_l = Sort.quick_sort(arr_l)
        arr_r = Sort.quick_sort(arr_r)
        return arr_l + arr_m + arr_r
