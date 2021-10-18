from time import sleep


def therteentimes():
    n = 0
    
    while n < 38:
        print("13 x",n,"= ",13*n) # print the thirteen-times table
        n = n+1
        sleep(0.5)
    
    else:
        print("n is no longer less than 37")
        

print("Call Function")
therteentimes()
print("End")
