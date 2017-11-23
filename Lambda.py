import random
from pprint import pprint

if __name__ == "__main__":
    list1 = [i for i in range(1, 10)]
    list2 = [i for i in range(1,10)]
    random.shuffle(list1)
    random.shuffle(list2)
    print(list1)
    print(list2)

    whole = list(zip(list1, list2))
    print(whole)
    whole.sort(key=lambda x:x[1])
    print(whole)

    list3, list4 = map(lambda x: list(x), zip(*whole))
    print(list3)
    print(list4)

    my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
    pprint(my_dict)
