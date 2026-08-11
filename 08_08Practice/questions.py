list = [1,-3,4,6,-2,19]
pos =[]
neg = []
for i in range(0,len(list)):
    if list[i] >=0:
        pos.append(list[i])
    else:
        neg.append(list[i])

print(f'the postive no are {pos} \n the negative no are {neg} ')

sum = 0
for i in list:
    sum+=i

print(f'the mean of {list} is {int(sum/len(list))}')

high_ele = list[0]

for i in list:
    if i>high_ele:
        high_ele = i
print(f'The highest element in {list} is {high_ele} present at index {list.index(high_ele)}')

high_ele = list[0]
sec_high = list[0]

for i in list:
    if i>high_ele:
        sec_high=high_ele
        high_ele = i
    elif sec_high<i<high_ele:
        sec_high=i

print(f'The second highest element in {list} is {sec_high} ')


list_sorted = list.sort()
if list==list_sorted:
    print("List is sorted")
else :
    print("List is not sorted")


















