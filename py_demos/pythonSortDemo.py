_list1 = [67,45,2,13,1,998]
_list2 = [89,23,33,45,10,12,45,45,45]

def sortList(list):
    count1=0
    count2=1

    while count1<len(list):
        while count2<len(list):
            if list[count1]>list[count2]:
                #the first is larger then the second swap
                temp=list[count2]
                list[count2]=list[count1]
                list[count1]=temp
            count2 +=1
        count1+=1
        count2 =count1+1
sortList(_list1)
sortList(_list2)

print _list1
print""
print _list2

