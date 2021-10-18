from time import sleep


def therteentimes(times,total):
    n = 0
    
    while n < total:
        print(times,"x",n,"= ",13*n) # print the times-times table
        n = n+1
        sleep(0.5)
    
    else:
        print("n is no longer less than",total)
        

print("Call Function")
therteentimes(3,10)
print("End of program")

