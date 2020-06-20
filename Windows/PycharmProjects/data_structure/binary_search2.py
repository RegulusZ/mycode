# coding:utf-8


def binary_search(a_list, key):
    n = len(a_list)
    if n == 0:
        return False
    start = 0
    end = n-1
    while end >= start:
        mid = (end+start)//2
        if a_list[mid] == key:
            return True
        elif a_list[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return False


if __name__ == "__main__":
    test_list = [1,1,2,3,5,8,13,21,34,55,89,144]
    print(binary_search(test_list, 24))

