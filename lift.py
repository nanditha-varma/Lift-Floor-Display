import time #inporting the time module
n=int(input("Enter the floor the lift is in:"))
while 2>1:#infinite loop
    a=int(input("Enter the floor you are in"))
    if a>n:
        for i in range(n,a+1):
            time.sleep(2)#the lift takes 2 seconds to go from one floor to the consecutive one
            print(i)#displays the floor number
    elif a<n:
        for i in range(n,a-1,-1):
            time.sleep(2)#the lift takes 2 seconds to go from one floor to the consecutive one
            print(i)#displays the floor number
    time.sleep(1)
    print("Opens the door")
    time.sleep(1)
    print("Enter")
    n=int(input("Enter the floor you want to go"))
    if a>n:
        for i in range(a,n-1,-1):
            time.sleep(2)
            print(i)
    elif a < n:
        for i in range(a,n+1):
            time.sleep(2)
            print(i)
    time.sleep(1)
    print("Opens the door")
    time.sleep(2)
    print("leave")
    print("Closes the door")