import sys
from time import sleep


print("djaf")
print("djaf")
print("djaf")
print("djaf")
for i in range(1,5):
    if i % 2 ==0:
        sys.stdout.write("\rdasafasfas")
    else:
        sys.stdout.write("\rm")
    sys.stdout.flush()
    sleep(1)