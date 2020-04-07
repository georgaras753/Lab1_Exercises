n = int(input("Enter number of elements : "))
a_list = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

def removeDuplicates(a_list):
    b_list = []
    n = 0
    m = 0
    first = 0
    for item1 in a_list:
        if first == 0:
            b_list.append(item1)
            first = 1
        else:
            for item2 in b_list:
                m = m + 1
                if item1 != item2:
                    n = n + 1

            if n == m:
                b_list.append(item1)
            n = 0
            m = 0

    return b_list

def sortList(b_list):
    c_list = []
    while b_list:
        min = b_list[0]
        for item1 in b_list:
            if item1 < min:
                min = item1
        c_list.append(min)
        b_list.remove(min)

    return c_list                                      

b_list = removeDuplicates(a_list)
print(b_list)

c_list = sortList(b_list)
print("\nsortList : ", c_list)