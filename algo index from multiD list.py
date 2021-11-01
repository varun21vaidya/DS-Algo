'''write a program to find index of a number from a multidimensional list

'''
def find_index(list1, item):
    index_list=[]
    for i in range(len(list1)):
        if list1[i]==item:     
            index_list.append([i])
        elif isinstance(list1[i], list):
            for index in find_index(list1[i], item):
                index_list.append(index+[i])
    return index_list

print(find_index([[[1,2,3],2,[1,3]],[1,2,3]], 2))
