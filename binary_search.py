"""
arra = [1, 2, 3, 4, 5, 6, 7]
        0  1  2  3  4  5  6


"""

class BinarySearch():

    def binary_search(key, list1):
        i = 0
        mid = len(list1) / 2
        middle = int(mid)
        if list1[middle] == key:
            return middle   

        elif list1[middle] > key:
            print('--------------11')
            i =  len(list1)
            for i in range(middle):
                if list1[i] == key:
                    return i
                    break
                else:
                    i = i - 1
        elif list1[middle] < key:
            print('----------------22')
            i = 0
            for i in range(list1[middle]):
                if list1[i] == key:
                    return i
                    break


    key = int(input("Enter Key for Search : "))
    print(type(key))
    list1 = [1, 2, 3, 4, 5]
    print("Key is in : ", binary_search(key, list1))