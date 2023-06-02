


def add_two(list_):
    empty=[]
    for x in list_:
        empty_sub=[]
        for y in x:
           empty_sub.append(y+2)
        empty.append(empty_sub)    
    return empty


print(add_two([[1,2,3],[4,5,6]]))