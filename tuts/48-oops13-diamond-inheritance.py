class A:
    def met(self):
        print("This is a method from class A")

class B(A):                                 # inherited by Class A
    def met(self):
        print("This is a method from class B")

class C(A):                                 # inherited by Class A
    def met(self):
        print("This is a method from class C")

    def jet(self):
        print("This is a unique method from class C")

class D(B, C):                              # inherited by Class B & C - simultaniously
    pass

# class D(C,B):                             # inheritance order changed to C than B - simultaniously
#     def met(self):                        # if class D has its own 'met' method, it will surpass all others for D
#         print("This is a method from class D")

a = A()
b = B()
c = C()
d = D()

d.met()
d.jet()