import random
def quicksort(left,right,a):
    if(left>right):
        return
    i = left
    j = right
    tmp = a[left]
    while(i!=j):
        while (i < j and a[j] >= tmp):
            j -= 1
        while (i < j and a[i] <= tmp):
            i += 1
        if(i<j):
            a[i],a[j] = a[j],a[i]
    a[left] = a[i]
    a[i] = tmp
    quicksort(left, i - 1, a)
    quicksort(i+1, right, a)



a = []
for i in range(20):
    a.append(int(200*random.random()))
print(a)
print(len(a))
quicksort(0,len(a)-1,a)
print(a)
