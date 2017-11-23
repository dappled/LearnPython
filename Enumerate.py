import itertools

if __name__ == "__main__":
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 2):
     print(c, value)

    a = itertools.combinations(tuple(range(4)), int(4 / 2))
    print(list(a))