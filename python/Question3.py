# modify this function, and create other functions below as you wish
def binary_search(maxs,scores):
    s_min = min(scores)
    s_max = max(scores)
    arr = [0] * (s_max-s_min + 1)

    for i in scores:
        arr[i - s_min] += 1

    lst = []
    for i,count in enumerate(arr):
        if(count==0):
            continue
        else:
            for j in range(0,count):
                lst.append(i+s_min)
        
    lst.reverse()
    print(lst)
    if(lst[-1] > maxs):
        lst.insert(len(lst),maxs)
        index = len(lst)-1
    else:
        for i,v in enumerate(lst):
                if(v > maxs):
                    continue
                else:
                    if(v == maxs):
                        index = i
                    else:
                        index = i-1
                    break
            
        lst.insert(index,maxs)
        
    rank = 1
    for el in range(1,index+1):
        if(lst[el] == lst[el-1]):
            continue
        else:
            rank +=1
    return rank

           
def question03(scores, alice):
    from collections import Counter    
    if(len(set(alice)) == len(alice)):
        result = binary_search(min(alice),scores)
        #print('Going')
        return result
    else:
        count = Counter(alice)    
        lst  = list(count.most_common(2))
        maxs = 0
        for ls in lst:
            maxs = max(ls[0],maxs)

        result = binary_search(maxs,scores)
        return result
