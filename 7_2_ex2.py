num1 = int(input())
ten = num1//10
one = 0

if num1-ten*10>5:
    ten +=1
elif 0<num1-ten*10<=5:
    one +=1


print(ten)
print(one)
print(num1 + ten*8 + one*5)
