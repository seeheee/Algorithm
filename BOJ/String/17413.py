num = input()
check_num = input()

list1 = []
list1.append(num)

list2 = []
list2.append(check_num)

print(list1)
print(list2)


for i in list2:
    if i in list1:
        print("YSE")
    else:
        print("NO")



