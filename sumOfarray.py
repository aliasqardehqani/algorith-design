class SumOfList():
    def list_input(n, list1):
        i = 0
        for i in range(n):
            list1_append= input(f"Number {i} : ")
            list1.append(list1_append)
        return list1
            
    n = 5
    total = 0
    list_ = []
    
    li = list_input(n, list_)

    for i in range(n):
        total = total + float(li[i])

    print(total)
