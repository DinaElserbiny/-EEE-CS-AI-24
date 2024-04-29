import math
class statistics:
    arr= []   

    def get_num():
    
        n = int(input("Enter the number of elements in the array: "))
        arr = []
        print("Enter the elements of the array:")
        for i in range(n):
            num = int(input()) 
            arr.append(num)
        s=statistics

        print("Min is :",s.get_min(arr))

        print("Max is :",s.get_max(arr))

        print("Mean is :",s.get_mean(arr,n))

        print("Mode is :",s.get_mode(arr))

        print("Median is :",s.get_median(arr,n))

        print("Range is :",s.get_range(arr))

        print("Variance is :",s.get_variance (arr,n))

        print("std is :",s.get_std(arr,n))

        print("quartiles is :",s.get_quartiles(arr))

        print("IQR is :",s.get_IQR(arr,n))



    def get_min(arr):
        min = arr[0]
        for num in arr:
            if num < min:
                min = num
        return min
    
    def get_max(arr):
        max=arr[0]
        for num in arr:
            if num > max:
                    max=num
        return max

    def get_mean(arr,n):
            sum=0
            for num in arr:
                sum=sum+num

            mean=sum/n
            return  mean
    
    
    def get_mode(arr):
        count_dict = {}
        
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1 
        s=statistics 
        max_count = s.get_max(list(count_dict.values()))
        #modes = [num for num, count in count_dict.items() if count == max_count]
        modes = [num for num, count in count_dict.items() if count == max_count]
        return modes 
    
    def get_median(arr,n):
        sortnum= sorted(arr)
        m=n//2
        if n%2 ==0:
            median=(sortnum[m]+sortnum[m+1])/2
        else:
            median=int(m)
        return median    
            
    def get_range(arr):
        s=statistics
        minnum=int(s.get_min(arr))
        maxnum=int(s.get_max(arr))
        range1=maxnum-minnum
        return range1

    def get_variance (arr,n) :
        sum=0
        s=statistics
        median=s.get_median(arr,n)
        for num in arr:
            sum=((num-median)*(num-median)) +sum 
        variance =sum // (n-1)
        
        return variance
    
    def get_std(arr,n):
        s=statistics
        variance=s.get_variance(arr,n)
        std=math.sqrt(variance)
        return std
    

   
   
    def get_quartiles(arr):
        s=statistics
        sorted_arr = sorted(arr)
        n = len(arr)
        q2 = s.get_median(arr, n)
        if n % 2 == 0:
            lower_half = sorted_arr[:n//2]
            upper_half = sorted_arr[n//2:]
        else:
            lower_half = sorted_arr[:n//2]
            upper_half = sorted_arr[n//2 + 1:]
        q1 = s.get_median(lower_half, len(lower_half))  # Pass the length of lower_half
        q3 =s.get_median(upper_half, len(upper_half))  # Pass the length of upper_half
        return q1, q2, q3
 

    def get_IQR(arr,n):
        s=statistics
        q1, _, q3 =s.get_quartiles(arr)
        return q3 - q1


obj=statistics
obj.get_num() 


















