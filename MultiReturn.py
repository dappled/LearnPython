def multi_return():
    return "a", "b"


if __name__ == "__main__":
    ret = multi_return()
    print(type(ret))
