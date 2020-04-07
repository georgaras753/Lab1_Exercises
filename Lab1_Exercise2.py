n = int(input("Enter number of values : "))
a_dict = {}

for i in range(n):
    text = input().split()
    a_dict[text[0]] = int(text[1])

def removeDuplicates(a_dict):
    b_dict = {}
    n = 0
    m = 0
    first = 0
    for key1 in a_dict:
        if first == 0:
            b_dict[key1] = a_dict[key1]
            first = 1
        else:
            for key2 in b_dict:
                m = m + 1
                if a_dict[key1] != b_dict[key2]:
                    n = n + 1

            if n == m:
                b_dict[key1] = a_dict[key1]
            n = 0
            m = 0

    return b_dict

def sortDict(b_dict):
    c_dict = {}
    while b_dict:
        key_min = min(b_dict, key=b_dict.get)
        c_dict[key_min] = b_dict[key_min]
        del b_dict[key_min]

    return c_dict                                      

b_dict = removeDuplicates(a_dict)
print(b_dict)

c_dict = sortDict(b_dict)
print("\nsortDict : ", c_dict)