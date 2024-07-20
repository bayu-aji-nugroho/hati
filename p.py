import time
import sys

var = 4

for i in range(5):
    for x in range(var):
        print(" ",end="")
        sys.stdout.flush()
        time.sleep(0.03)
        
    for y in range(i+1):
        print("*",end="")
        sys.stdout.flush()
        time.sleep(0.03)
    
    for y in range(i+1):
        print("*",end="")
        sys.stdout.flush()
        time.sleep(0.03)
    
    for x in range(var):
        print(" ",end="")
        sys.stdout.flush()
        time.sleep(0.03)
        
    for x in range(var):
        print(" ",end="")
        sys.stdout.flush()
        time.sleep(0.03)
    
    for y in range(i+1):
        print("*",end="")
        sys.stdout.flush()
        time.sleep(0.03)
    
    for y in range(i+1):
        if (y ==10):
            break
        print("*",end="")
        sys.stdout.flush()
        time.sleep(0.03)
    var -= 1
    print(end="\n")
var = 9
    
for i in range(10):
    for y in range(i+1):
        print(" ",end="")
        sys.stdout.flush()
        time.sleep(0.03)
        
    for x in range(var):
        print("*",end="")
        sys.stdout.flush()
        time.sleep(0.03)
        
    for x in range(var):
        print("*",end="")
        sys.stdout.flush()
        time.sleep(0.03)
    print(end="\n")
    var -= 1
    
        