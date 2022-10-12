def binarysearch(pool, element, lower, higher):
    if higher >= lower:  
        mid = (higher + lower) // 2
        if pool[mid] == element:
            return mid
        elif element < pool[mid]:
            return binarysearch(pool, element, lower, mid - 1)
        elif element > pool[mid]:
            return binarysearch(pool, element, mid + 1, higher) 
    else:
        return -1
        
pool = list(range(0,10,2))
print(pool)
x = binarysearch(pool, 2, 0, len(pool)-1)
if x != -1:
    print(f'gefunden! Bei {x}')
else:
    print('nicht gefunden')