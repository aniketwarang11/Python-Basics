try :
    n = int(input("Enter the no of apples Harry have :- "))
    print("Harry have ",n,"apples")
    mn = int(input("Enter the minimum value :- "))
    mx = int(input("Enter the maximum value :- "))
    i = 1
    # if n < mn | n < mx :
    #     print("Either Maximum or Minimum is grater than ",n)

    if mn > mx :
        print("not a range ",mn, "is grater than ",mx)

    elif mn != mx :
        for i in range(mn,mx+1):
            if n%i == 0:
                print(i,' is divisor of ',n)
            else:
                print(i,' is not a divisor of ',n)

    else:
        print("This is not a range ",mn," and ",mx," both are same")
        if n % mn == 0:
            print(mn, ' is divisor of ', n)
        else:
            print(mn, ' is not a divisor of ', n)

except Exception as e :
    print("Enter Integers only")









