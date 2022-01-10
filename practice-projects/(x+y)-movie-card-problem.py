# X+Y movie card problem
# Twenty random cards are placed in a row all face down.
# A turn consists of taking two adjacent cards where the left one is face up and the right one can be face up or face down and flipping them both.
# Show that this process must terminate.


import time
def binaryTransform(b):
    for i in range(len(b)-1):
        if b[i] == '1':
            b[i] = '0'
            if b[i+1] == '0':
                b[i+1] = '1'
            else:
                b[i+1] = '0'
    return b

if __name__ == "__main__":
    c = input("Enter any number in binary form : ")
    a = list(c)
    print(a)
    init = time.time()
    while a != binaryTransform(a.copy()):
        a = binaryTransform(a.copy())
    print(a)
    print(f"it took {time.time() - init} seconds.")