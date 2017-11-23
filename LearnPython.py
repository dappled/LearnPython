def square(start, end):
    for i in range(start, end):
        yield i * i


if __name__ == "__main__":

    noprimes = [j for i in range(2, 8) for j in range(i * 2, 50, i)]

    gen = square(0, 10)
    for i in gen:
        print(i)
    gen2 = [i*i for i in range(0, 10)]
    print(gen2)