rows = int(input("Enter the number of rows: "))  

for i in range(1, rows+1):  
    
    for j in range(rows-i):
        print(" ", end="")
    
    for j in range(i*2-1):
        print("*", end="")
    print()  
