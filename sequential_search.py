class SequentialSearch():
    def seq_search(key, n, list1):
        i = 0
        while i < n:
            if list1[i] == key:
                return i 
                break
            i += 1
    def list_input(n, list1):
        i = 0
        for i in range(n):
            list1_append= int(input(f"Number {i} : "))
            list1.append(list1_append)
        return list1

    n = 5
    list1 = []
    key = input("Enter key : ") 
    list_input(n, list1)
    print(seq_search(key, n, list1))         