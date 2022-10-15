

def generate_Magic_Square(size):
    magicSquare=[[0 for x in range(size)] for y in range(size)]

    # Initializing first position of matrix
    i=size/2
    j=size-1

    # Fill the magic square by placing values at appropriate position
    num=1
    while num<=(size*size):
        if i==-1 and j==size:  # 3rd Condition
            j=size-2
            i=0
        else:
            # next number goes out of right side of square
            if j==size:
                j=0

            # next number goes out of upper side
            if i<0:
                i=size-1

        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[int(i)][int(j)]=num
            num=num+1

        j=j+1
        i=i-1  # 1st condition

    # Printing of magic square
    sum=size*(size*size+1)/2
    print("Sum of each row or column is : ",sum)
    print("Magic Square of size",size,"*",size,"is : \n")

    for i in range(0,size):
        for j in range(0,size):
            print(' %2d ' % (magicSquare[i][j]),end=' | ')

            # To display magic square in matrix form
            if j==size-1:
                print()

#<------------------------------------------------------------------------------------------------->

def DoublyEven(n):

     

    # 2-D matrix with all entries as 0

    arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)]
 

    # Change value of array elements at fix location 

    # as per the rule (n*n+1)-arr[i][[j]

     

    # Corners of order (n/4)*(n/4)

    # Top left corner

    for i in range(0,n//4):

        for j in range(0,n//4):

            arr[i][j] = (n*n + 1) - arr[i][j];

     

    # Top right corner

    for i in range(0,n//4):

        for j in range(3 * (n//4),n):

            arr[i][j] = (n*n + 1) - arr[i][j];
 

    # Bottom Left corner

    for i in range(3 * (n//4),n):

        for j in range(0,n//4):

            arr[i][j] = (n*n + 1) - arr[i][j];

     

    # Bottom Right corner

    for i in range(3 * (n//4),n):

        for j in range(3 * (n//4),n):

            arr[i][j] = (n*n + 1) - arr[i][j];

             

    # Centre of matrix,order (n/2)*(n/2)

    for i in range(n//4,3 * (n//4)):

        for j in range(n//4,3 * (n//4)):

            arr[i][j] = (n*n + 1) - arr[i][j];

    print("Magic Square of size",n,"*",n,"is : \n")

    for i in range(n):

        for j in range(n):

            print ('%2d ' %(arr[i][j]),end=" ")

        print()
#Main function

flag=1
while flag==1:
    n=int(input("\nEnter the size of the MAGIC SQUARE : "))
    if n%2==0:
        DoublyEven(n)
        
    else:
        generate_Magic_Square(n)
    a=input("\nDo you want to print Magic Square of some other size (yes/no) : ")
    if a=='yes':
        flag=1
    else:
        flag=0
        print("\nThanks for using this program!")
