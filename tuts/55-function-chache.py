import time
from functools import lru_cache

@lru_cache(maxsize=3)
def word(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("Now running")
    word(3)
    word(1)                 # this will chache, since max-size = 3
    word(2)                 # this will chache, since max-size = 3
    word(4)                 # this will chache, since max-size = 3
    print("Running again")
    word(3)
    print("Done.")