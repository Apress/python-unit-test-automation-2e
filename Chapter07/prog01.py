import datetime
import sys

logfile = open('mylog.log', 'w')
msg = "Commencing Execution of the program...\n" + str(datetime.datetime.now())
print(msg)
logfile.write(msg)

for i in [1, 2, 3, 4, 5]:
    msg = "\nIteration " + str(i) + " ..."
    print(msg)
    logfile.write(msg)

msg = "\nDone...\n" + str(datetime.datetime.now())
logfile.write(msg)
print(msg)
logfile.close()
sys.exit(0)
