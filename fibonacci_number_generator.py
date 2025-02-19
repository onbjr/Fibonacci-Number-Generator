import time
import math

fibo = int(input("Enter the fibonnaci number that you want: "))

start_time = time.time()


a = 0
b = 1
i = 0

fibo = fibo + 1


while True:
    if i < fibo:
        a = a + b
        i = i + 1
        if i < fibo:
            b = a + b
            i = i + 1
    elif i == fibo:    
        try:
            print("--- %s seconds ---" % (time.time() - start_time))
            print(b)
        except:
            print("--- %s seconds ---" % (time.time() - start_time))
            print("Your number is too big for printing.")
        break

    

