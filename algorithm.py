print("Welcome to the robot!")

def robot(a,b):
    n=eval(input("Enter order of square matrix for the robot to run : "))
    inst=input("Enter direction : ")
    for i in range(1000000):
        if inst=="up":
            a=a-1      
        elif inst=="down":
            a=a+1
        elif inst=="left":
            b=b-1       
        elif inst=="right":
            b=b+1
        elif inst=="stop":
            if a<=n-1 and b<=n-1:
                print("The current position of the robot is:","(",a,b,") in the",n,"x",n,"matrix")
                return None
            else:
                print("Oops! Robot fell out of the matrix. Please restart the program to run robot again.")
                return None
        else:
            print("invalid syntax")
        inst=input("Enter next direction : ")

robot(0,0)
