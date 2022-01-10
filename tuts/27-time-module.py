# get programme execution time
import time

initial1 = time.time()
# print(initial1)
for i in range(10):
    print("This is for loop.")
    time.sleep(1)
print(f"for loop ran in {time.time() - initial1} seconds.")


initial2 = time.time()
a = 0
while a<10:
    print("This is while loop.")
    time.sleep(1)
    a +=1
print(f"while loop ran in {time.time() - initial2} seconds.")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)