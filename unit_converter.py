a=input("Enter a number: ")
print("1. Decimal to Binary")
print("2. Octal to Binary")
print("3. Hexadecimal to Binary")
print("Enter your choice: ")
ch=int(input())
c=0
copy=a
flag=0
len1=len(a)
result=[]
i=0
result2=""
if a=="0":
    print("000")
elif a=="1":
    print("001")
elif a=="2":
    print("010")
elif ch==1:
    a=int(a)
    while a!=1:
        rem=a%2
        result.append(rem)
        a=int(a/2)
    result.append(1)
    print("The binary equivalent of",copy,"is",end=" ")
    for x in range(len(result)-1,-1,-1):
        print(result[x],end="")
elif ch==2:
    while i<len1:
        digit=a[i]
        if digit == '0':
            result2 = result2 + "000"
        elif digit == '1':
            result2 = result2 + "001"
        elif digit == '2':
            result2 = result2 + "010"
        elif digit == '3':
            result2 = result2 + "011"
        elif digit == '4':
            result2 = result2 + "100"
        elif digit == '5':
            result2 = result2 + "101"
        elif digit == '6':
            result2 = result2 + "110"
        elif digit == '7':
            result2 = result2 + "111"
        else:
            print("Invalid Input",digit)
        i=i+1
    print("The binary equivalent of", copy, "is",result2)
elif ch==3:
    while i<len1:
        if a[i]=='0':
            result2=result2+"0000"
        elif a[i]=='1':
            result2=result2+"0001"
        elif a[i]=='2':
            result2=result2+"0010"
        elif a[i]=='3':
            result2=result2+"0011"
        elif a[i]=='4':
            result2=result2+"0100"
        elif a[i]=='5':
            result2=result2+"0101"
        elif a[i]=='6':
            result2=result2+"0110"
        elif a[i]=='7':
            result2=result2+"0111"
        elif a[i]=='8':
            result2=result2+"1000"
        elif a[i]=='9':
            result2=result2+"1001"
        elif a[i]=='a' or a[i]=='A':
            result2=result2+"1010"
        elif a[i]=='b' or a[i]=='B':
            result2=result2+"1011"
        elif a[i]=='c' or a[i]=='C':
            result2=result2+"1100"
        if a[i]=='d' or a[i]=='D':
            result2=result2+"1101"
        if a[i]=='e' or a[i]=='E':
            result2=result2+"1110"
        if a[i]=='f' or a[i]=='F':
            result2=result2+"1111"
        i=i+1
    print("The binary equivalent of", copy, "is",result2)
else:
    print("Incorrect Choice")