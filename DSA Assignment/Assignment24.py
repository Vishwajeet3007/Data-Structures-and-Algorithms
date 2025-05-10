def Bubble_Sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                
l=[24,58,11,67,92,43]
Bubble_Sort(l)
print(l)
print()

def Modified_Bubble_Sort(data_list):
    flag=False
    for r in range(1,len(data_list)):
        flag=False
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
                
l1=[24,58,11,67,92,43]
Modified_Bubble_Sort(l1)
print(l1)



