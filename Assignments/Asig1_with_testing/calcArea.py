def calcArea(str , num1 , num2=1):
    area=1
    if str == "t":
        area = 0.5 * num1 * num2
    elif str == "r":
        area = num1 * num2
    elif str == "s":
        area = num1 * num1
    elif str == "c":
        area = (22/7)* num1 * num1
    return area


    print(calcArea("r" , 2 ,3))

    # if __name__ == '__main__':
    # pass
