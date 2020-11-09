a=input().split()
n_list = []
for i in a:
    n_list.append(int(i))
def fmin(l_list):
    mn=l_list[0]
    for i in l_list:
        if i<mn:
            mn=i
    return mn
def selection_sort(array):
    print(' '.join(str(x) for x in array))
    for i in range(len(array)-1):
        mn=fmin(array[i:len(array)])
        mn_i=array.index(mn)
        array[i],array[mn_i]=array[mn_i],array[i]
        print(' '.join(str(x) for x in array))

selection_sort(n_list)
    
    
    
