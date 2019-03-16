def PrintEven(no):
    no2 = no * 2;
    for i in range(1,no2+1):
        # print("i :",i)
        if(i % 2 == 0):
            print(i);
            i += 1;
        else:
            i += 1;

PrintEven(6);