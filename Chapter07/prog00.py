import datetime
import sys

print("Commencing Execution of the program...")
print(datetime.datetime.now())

for i in [1, 2, 3, 4, 5]:
    print("Iteration " + str(i) + " ...")

print("Done...")
print(datetime.datetime.now())
sys.exit(0)
