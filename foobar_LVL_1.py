def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
   
def solution(data, n): 
    dict= {}
    for datapoint in data:
        if datapoint in dict:
            dict[datapoint]+=1
        else:
            dict[datapoint]=1
    for key in dict:
        if (dict.get(key) > n):
            remove_values_from_list(data,key)
            data[:] = [x for x in data if x != key]
            print(key,':', data)
    
solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)