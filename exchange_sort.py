class ExChangeSort():
    def exchange(n, list1):
        i = 0
        j = 0
        for i in range(n):
            j = j + i
            for j in range(n):
                if list1[i] < list1[j]: 
                    temp = 0
                    temp = list1[i]
                    list1[i] = list1[j]
                    list1[j] = temp
        
        i = 0
        for i in range(n):
            print(list1[i])

    def list_input(n, list1):
        i = 0
        for i in range(n):
            list1_append= int(input(f"Number {i} : "))
            list1.append(list1_append)
        return list1

    n = 5
    total = 0
    list_ = []
    
    li = list_input(n, list_)
    print(li)
    exchange(n, li)

