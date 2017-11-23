from functools import wraps

def new_dec(fun):
    @wraps(fun)
    def dummy():
        print("before dec")
        fun()
        print("after dec")

    return dummy

@new_dec
def func():
    a = 33
    print(f"real function{a}")

if __name__ == "__main__":
    func()
