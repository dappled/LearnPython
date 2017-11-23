class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        print("go B go!")
        super(B, self).go()


class C(A):
    def go(self):
        print("go C go!")
        super(C, self).go()

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        print("go D go!")
        super(D, self).go()

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

if __name__ == "__main__":
    D().go()
